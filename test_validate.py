import contextlib
import copy
import io
import json
import pathlib
import tempfile
import unittest
from validate import main, validate


def record():
    return dict(id=1, title='Example study', authors='Example A.', year='2025',
                venue='Example journal', group='BCI', kind='Human / feasibility',
                why='An illustrative validator fixture, not a real paper.',
                caution='Synthetic metadata only.',
                url='https://doi.org/10.1234/example', doi='10.1234/example',
                verification='Synthetic fixture', bucket='BCI')


class ValidatorTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate([record()]), [])

    def test_repository_entry_without_doi(self):
        row = record()
        row.pop('doi')
        row['url'] = 'https://arxiv.org/abs/1234.56789'
        self.assertEqual(validate([row]), [])

    def test_empty_or_non_array(self):
        for value in ([], {}, None, 'text'):
            with self.subTest(value=value):
                self.assertTrue(validate(value))

    def test_non_object(self):
        self.assertIn('expected an object', validate([None])[0])

    def test_required_limit(self):
        row = record()
        row['caution'] = '  '
        self.assertTrue(any('caution' in e for e in validate([row])))

    def test_bool_is_not_an_id(self):
        row = record()
        row['id'] = True
        self.assertTrue(any('positive integer' in e for e in validate([row])))

    def test_duplicate_id(self):
        other = record()
        other.update(title='Different study', doi='10.1234/other',
                     url='https://doi.org/10.1234/other')
        self.assertTrue(any('duplicate id' in e for e in validate([record(), other])))

    def test_duplicate_title_ignores_case_and_punctuation(self):
        other = record()
        other.update(id=2, title='EXAMPLE: study!', doi='10.1234/other',
                     url='https://doi.org/10.1234/other')
        self.assertTrue(any('duplicate title' in e for e in validate([record(), other])))

    def test_duplicate_doi_ignores_case(self):
        other = record()
        other.update(id=2, title='Different study', doi='10.1234/EXAMPLE',
                     url='https://doi.org/10.1234/EXAMPLE')
        self.assertTrue(any('duplicate doi' in e for e in validate([record(), other])))

    def test_mismatched_doi(self):
        row = record()
        row['doi'] = '10.1234/different'
        self.assertTrue(any('disagree' in e for e in validate([row])))

    def test_encoded_doi(self):
        row = record()
        row['url'] = 'https://doi.org/10.1234%2Fexample'
        self.assertEqual(validate([row]), [])

    def test_reject_bad_urls(self):
        for value in ('http://example.org/paper', 'https://user:pass@example.org',
                      'https://', 'https://[bad', 'https://example.org/a b', 123):
            with self.subTest(value=value):
                row = record()
                row['url'] = value
                self.assertTrue(any('HTTPS' in e for e in validate([row])))

    def test_optional_open_text_checked(self):
        row = record()
        row['openUrl'] = 'javascript:alert(1)'
        self.assertTrue(any('openUrl' in e for e in validate([row])))

    def test_unknown_bucket(self):
        row = record()
        row['bucket'] = 'Clinical proof'
        self.assertTrue(any('bucket' in e for e in validate([row])))

    def test_bad_year(self):
        row = record()
        row['year'] = 2025
        self.assertTrue(any('year' in e for e in validate([row])))

    def test_validation_does_not_mutate(self):
        rows = [record()]
        original = copy.deepcopy(rows)
        validate(rows)
        self.assertEqual(rows, original)

    def test_cli_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / 'papers.json'
            path.write_text(json.dumps([record()]))
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main([str(path)]), 0)

    def test_cli_validation_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / 'papers.json'
            path.write_text('[]')
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main([str(path)]), 1)

    def test_cli_invalid_json_or_missing_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / 'papers.json'
            path.write_text('{')
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main([str(path)]), 2)
                self.assertEqual(main([str(path) + '.missing']), 2)
                self.assertEqual(main([]), 2)


if __name__ == '__main__':
    unittest.main()
