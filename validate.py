"""Validate a resource-guide bibliography offline using the Python standard library.

This checks metadata shape and duplicate identities, not scientific validity,
full-text appraisal, link availability or clinical effectiveness.
"""
import json
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

REQUIRED = ('title', 'authors', 'year', 'venue', 'group', 'kind', 'why',
            'caution', 'url', 'verification', 'bucket')
BUCKETS = {'Mind', 'BCI', 'Aging'}
DOI = re.compile(r'^10\.\d{4,9}/\S+$', re.IGNORECASE)


def title_key(value):
    return ''.join(c for c in unicodedata.normalize('NFKC', value).casefold()
                   if c.isalnum())


def https_url(value):
    if not isinstance(value, str) or any(c.isspace() for c in value):
        return False
    try:
        p = urlsplit(value)
        return (p.scheme == 'https' and bool(p.hostname)
                and not p.username and not p.password)
    except ValueError:
        return False


def validate(records):
    """Return all errors, never change records or make network requests."""
    errors = []
    if not isinstance(records, list) or not records:
        return ['bibliography must be a non-empty JSON array']
    seen = {'id': {}, 'title': {}, 'doi': {}, 'url': {}}
    for index, row in enumerate(records, 1):
        label = f'row {index}'
        if not isinstance(row, dict):
            errors.append(f'{label}: expected an object')
            continue
        for key in REQUIRED:
            value = row.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f'{label}: {key} must be a non-empty string')
        ident = row.get('id')
        if type(ident) is not int or ident <= 0:
            errors.append(f'{label}: id must be a positive integer')
        if row.get('bucket') not in BUCKETS:
            errors.append(f'{label}: unknown bucket')
        if not isinstance(row.get('year'), str) or not re.fullmatch(r'\d{4}', row['year']):
            errors.append(f'{label}: year must be four digits as a string')
        for key in ('url', 'openUrl'):
            value = row.get(key)
            if (key == 'url' or value is not None) and not https_url(value):
                errors.append(f'{label}: {key} must be an HTTPS URL without credentials or whitespace')
        doi = row.get('doi')
        if doi is not None and (not isinstance(doi, str) or not DOI.fullmatch(doi)):
            errors.append(f'{label}: malformed DOI')
        primary = row.get('url')
        if isinstance(primary, str) and https_url(primary):
            parsed = urlsplit(primary)
            if parsed.hostname in {'doi.org', 'dx.doi.org'}:
                from_url = unquote(parsed.path.lstrip('/')).casefold()
                if not isinstance(doi, str) or from_url != doi.casefold():
                    errors.append(f'{label}: DOI URL and doi field disagree')
        keys = {
            'id': ident if type(ident) is int and ident > 0 else None,
            'title': title_key(row['title']) if isinstance(row.get('title'), str) else None,
            'doi': doi.casefold() if isinstance(doi, str) else None,
            'url': primary if isinstance(primary, str) else None,
        }
        for field, value in keys.items():
            if value is None or value == '':
                continue
            if value in seen[field]:
                errors.append(f'{label}: duplicate {field} with row {seen[field][value]}')
            else:
                seen[field][value] = index
    return errors


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print('Usage: python3 validate.py papers.json', file=sys.stderr)
        return 2
    try:
        with open(argv[0], encoding='utf-8') as handle:
            records = json.load(handle)
    except (OSError, ValueError) as exc:
        print(f'Cannot read bibliography: {exc}', file=sys.stderr)
        return 2
    errors = validate(records)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'OK: {len(records)} records; structural validation only, not scientific review.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
