# Brain emulation and consciousness: a resource guide

This guide separates theories of consciousness, structural connectomics, computational simulation, tissue preservation and philosophical questions about identity. These are different research problems. None of the listed works establishes successful human mind uploading.

## Questions to carry through the reading

- What is the target: task performance, neural dynamics, conscious access, or continuity of a particular person?
- Which biological detail is measured, which is modeled, and which is assumed away?
- Does the result concern a fly, mouse, tissue fragment, simulated circuit, or living human?
- What observation could falsify the central claim?

## First useful projects

1. Build a cross-paper assumptions matrix: measurement scale, modeled state variables, validation task and known missing biology. Cite the relevant methods section before filling a cell.
2. Reproduce one small neural simulation with a fixed random seed and a declared version. Do not label matching a neural trace as evidence of consciousness.
3. Add a source-backed dataset card for a connectome, including species, sampling, reconstruction errors and access terms. A connectome is not a preserved person's mind.

## Scope and provenance

Prepared 17 November 2026 from a selected 66-work reading library: 17 mind/emulation, 18 BCI/neurotechnology and 31 aging/rejuvenation works. The underlying selection covers foundational work and selected publications through 2025. This is not an exhaustive, latest or systematic review.

The source library checked journal bibliographic records and abstracts and direct repository abstracts for the six arXiv entries. Reading notes are short original summaries, not full-text critical appraisals. This guide preserves those limits; it does not imply every full text was read. Paper full texts are linked, not redistributed. Source titles and author names remain attributed to their authors.

`papers.json` is the reusable source, `papers.bib` is a citation export, and `validate.py` checks local metadata. Validation is structural, not a scientific peer review or a live link check. No clinical datasets or participant-level records are included.

## Evidence labels

- **Theory / review / philosophy / roadmap:** synthesis or argument, not an experimental demonstration of uploading or rejuvenation.
- **Computational:** simulation or modeling; judge the model's measured validation target, not its name.
- **Animal / tissue:** results for the stated organism or preparation, not proof of a human outcome.
- **Human cells / in vitro:** experiments on cells, not treatment of a person.
- **Human feasibility / pilot:** limited early human evidence; do not infer population-wide effectiveness.
- **Human trial / RCT:** inspect population, controls, sample size, endpoints and harms. A randomized biomarker analysis is still a biomarker analysis.
- **arXiv / report:** repository-hosted work; the label alone does not establish journal peer review.

## Use and improve this guide

```sh
python3 validate.py papers.json
python3 -m unittest -v test_validate.py
```

Keep limitations attached to the result they qualify. See `CONTRIBUTING.md` for the review checklist. Repository documentation and code are private review material at this stage. No license grant is made for third-party papers. Before a wider release, choose terms for the original guide/code separately from rights in cited works.

## Suggested reading path

1. [Theories of consciousness](https://doi.org/10.1038/s41583-022-00587-4) (2022) - Theory / review. Compares major consciousness theories and how to test their differences. Limitation: The theories disagree; no agreed test here proves an uploaded mind retains identity.
2. [Conscious Processing and the Global Neuronal Workspace Hypothesis](https://doi.org/10.1016/j.neuron.2020.01.026) (2020) - Theory / review. How the global neuronal workspace explains conscious access. Limitation: One theory of consciousness, not an uploading method.
3. [The human connectome: A structural description of the human brain](https://doi.org/10.1371/journal.pcbi.0010042) (2005) - Theory / roadmap. Sets out the human-connectome research program and its rationale. Limitation: An influential structural roadmap, not a completed human synapse map.
4. [Neuronal wiring diagram of an adult brain](https://doi.org/10.1038/s41586-024-07558-y) (2024) - Animal / connectome. Maps the adult female fruit-fly brain at synapse scale. Limitation: A wiring map is not a conscious emulation or a human brain upload.
5. [A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution](https://doi.org/10.1126/science.adk4858) (2024) - Human tissue. Reconstructs a cubic millimeter of human cortex at nanoscale resolution. Limitation: A small surgically removed tissue sample, not a whole human brain.
6. [Reconstruction and Simulation of Neocortical Microcircuitry](https://doi.org/10.1016/j.cell.2015.09.029) (2015) - Computational. Reconstructs and simulates a detailed juvenile-rat cortical microcircuit. Limitation: A modeled microcircuit, not an entire rat or a transferred mind.
7. [State of Brain Emulation Report 2025](https://arxiv.org/abs/2510.15745) (2025) - Report / arXiv. Surveys neural dynamics, connectomics, emulation and embodiment as the building blocks of brain emulation. Limitation: A progress report and research agenda, not evidence of human mind uploading.
8. [The Fallacy of Favoring Gradual Replacement Mind Uploading Over Scan-and-Copy](https://arxiv.org/abs/1504.06320) (2015) - Philosophy / arXiv. Argues that gradual replacement and destructive scan-and-copy are equivalent with respect to personal identity. Limitation: A contested philosophical argument, not an experiment. The arXiv record also lists a 2016 Journal of Consciousness Studies publication.

## Annotated bibliography

### P01. Conscious Processing and the Global Neuronal Workspace Hypothesis

Mashour GA, Roelfsema P, Changeux JP, Dehaene S. (2020). *Neuron*.

**Evidence:** Theory / review.

**Why read:** How the global neuronal workspace explains conscious access.

**Limit:** One theory of consciousness, not an uploading method.

[Primary record](https://doi.org/10.1016/j.neuron.2020.01.026) | [Open-text link](https://europepmc.org/articles/PMC8770991)

Verification: Bibliographic record and abstract checked.

### P02. Neuronal wiring diagram of an adult brain

Dorkenwald S, Matsliah A, Sterling AR, Schlegel P, Yu SC, McKellar CE, Lin A, Costa M, Eichler K, Yin Y, Silversmith W, Schneider-Mizell C, Jordan CS, Brittain D, Halageri A, Kuehner K, Ogedengbe O, Morey R, Gager J, Kruk K, Perlman E, Yang R, Deutsch D, Bland D, Sorek M, Lu R, Macrina T, Lee K, Bae JA, Mu S, Nehoran B, Mitchell E, Popovych S, Wu J, Jia Z, Castro MA, Kemnitz N, Ih D, Bates AS, Eckstein N, Funke J, Collman F, Bock DD, Jefferis GSXE, Seung HS, Murthy M, FlyWire Consortium. (2024). *Nature*.

**Evidence:** Animal / connectome.

**Why read:** Maps the adult female fruit-fly brain at synapse scale.

**Limit:** A wiring map is not a conscious emulation or a human brain upload.

[Primary record](https://doi.org/10.1038/s41586-024-07558-y) | [Open-text link](https://europepmc.org/articles/PMC11446842)

Verification: Bibliographic record and abstract checked.

### P03. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution

Shapson-Coe A, Januszewski M, Berger DR, Pope A, Wu Y, Blakely T, Schalek RL, Li PH, Wang S, Maitin-Shepard J, Karlupia N, Dorkenwald S, Sjostedt E, Leavitt L, Lee D, Troidl J, Collman F, Bailey L, Fitzmaurice A, Kar R, Field B, Wu H, Wagner-Carena J, Aley D, Lau J, Lin Z, Wei D, Pfister H, Peleg A, Jain V, Lichtman JW. (2024). *Science (New York, N.Y.)*.

**Evidence:** Human tissue.

**Why read:** Reconstructs a cubic millimeter of human cortex at nanoscale resolution.

**Limit:** A small surgically removed tissue sample, not a whole human brain.

[Primary record](https://doi.org/10.1126/science.adk4858) | [Open-text link](https://europepmc.org/articles/PMC11718559)

Verification: Bibliographic record and abstract checked.

### P04. Functional connectomics spanning multiple areas of mouse visual cortex

MICrONS Consortium. (2025). *Nature*.

**Evidence:** Animal / connectome.

**Why read:** Links mouse visual-cortex activity to dense electron-microscopy wiring.

**Limit:** Mouse tissue and partial cortex; structure plus activity still leaves modeling gaps.

[Primary record](https://doi.org/10.1038/s41586-025-08790-w) | [Open-text link](https://resolver.sub.uni-goettingen.de/purl?gro-2/148947)

Verification: Bibliographic record and abstract checked.

### P05. Reconstruction and Simulation of Neocortical Microcircuitry

Markram H, Muller E, Ramaswamy S, Reimann MW, Abdellah M, Sanchez CA, Ailamaki A, Alonso-Nanclares L, Antille N, Arsever S, Kahou GA, Berger TK, Bilgili A, Buncic N, Chalimourda A, Chindemi G, Courcol JD, Delalondre F, Delattre V, Druckmann S, Dumusc R, Dynes J, Eilemann S, Gal E, Gevaert ME, Ghobril JP, Gidon A, Graham JW, Gupta A, Haenel V, Hay E, Heinis T, Hernando JB, Hines M, Kanari L, Keller D, Kenyon J, Khazen G, Kim Y, King JG, Kisvarday Z, Kumbhar P, Lasserre S, Le Bé JV, Magalhães BR, Merchán-Pérez A, Meystre J, Morrice BR, Muller J, Muñoz-Céspedes A, Muralidhar S, Muthurasa K, Nachbaur D, Newton TH, Nolte M, Ovcharenko A, Palacios J, Pastor L, Perin R, Ranjan R, Riachi I, Rodríguez JR, Riquelme JL, Rössert C, Sfyrakis K, Shi Y, Shillcock JC, Silberberg G, Silva R, Tauheed F, Telefont M, Toledo-Rodriguez M, Tränkler T, Van Geit W, Díaz JV, Walker R, Wang Y, Zaninetta SM, DeFelipe J, Hill SL, Segev I, Schürmann F. (2015). *Cell*.

**Evidence:** Computational.

**Why read:** Reconstructs and simulates a detailed juvenile-rat cortical microcircuit.

**Limit:** A modeled microcircuit, not an entire rat or a transferred mind.

[Primary record](https://doi.org/10.1016/j.cell.2015.09.029)

Verification: Bibliographic record and abstract checked.

### P06. The Virtual Brain: a simulator of primate brain network dynamics

Sanz Leon P, Knock SA, Woodman MM, Domide L, Mersmann J, McIntosh AR, Jirsa V. (2013). *Frontiers in neuroinformatics*.

**Evidence:** Computational.

**Why read:** Introduces personalized large-scale brain-network simulation software.

**Limit:** Macroscopic brain dynamics do not establish subjective consciousness.

[Primary record](https://doi.org/10.3389/fninf.2013.00010) | [Open-text link](https://europepmc.org/articles/PMC3678125)

Verification: Bibliographic record and abstract checked.

### P07. A large-scale model of the functioning brain

Eliasmith C, Stewart TC, Choo X, Bekolay T, DeWolf T, Tang Y, Rasmussen D. (2012). *Science (New York, N.Y.)*.

**Evidence:** Computational.

**Why read:** Spaun links a large spiking-neuron model to several behavioral tasks.

**Limit:** Task performance in a simplified model does not prove consciousness.

[Primary record](https://doi.org/10.1126/science.1225266)

Verification: Bibliographic record and abstract checked.

### P08. Consciousness and complexity: a consilience of evidence

Sarasso S, Casali AG, Casarotto S, Rosanova M, Sinigaglia C, Massimini M. (2021). *Neuroscience of consciousness*.

**Evidence:** Theory / review.

**Why read:** Reviews converging evidence for complexity-related measures of consciousness.

**Limit:** Markers and theoretical interpretation, not a method for transferring consciousness.

[Primary record](https://doi.org/10.1093/nc/niab023) | [Open-text link](https://europepmc.org/articles/PMC10941977)

Verification: Bibliographic record and abstract checked.

### P09. Theories of consciousness

Seth AK, Bayne T. (2022). *Nature reviews. Neuroscience*.

**Evidence:** Theory / review.

**Why read:** Compares major consciousness theories and how to test their differences.

**Limit:** The theories disagree; no agreed test here proves an uploaded mind retains identity.

[Primary record](https://doi.org/10.1038/s41583-022-00587-4)

Verification: Bibliographic record and abstract checked.

### P10. The human connectome: A structural description of the human brain

Sporns O, Tononi G, Kötter R. (2005). *PLoS computational biology*.

**Evidence:** Theory / roadmap.

**Why read:** Sets out the human-connectome research program and its rationale.

**Limit:** An influential structural roadmap, not a completed human synapse map.

[Primary record](https://doi.org/10.1371/journal.pcbi.0010042) | [Open-text link](https://europepmc.org/articles/PMC1239902)

Verification: Bibliographic record and abstract checked.

### P11. Aldehyde-stabilized cryopreservation

McIntyre RL, Fahy GM. (2015). *Cryobiology*.

**Evidence:** Animal tissue / preservation.

**Why read:** Uses fixation and vitrification to preserve brain ultrastructure in rabbits and pigs.

**Limit:** Chemical fixation preserves anatomy, not living function; no revival or memory recovery demonstrated.

[Primary record](https://doi.org/10.1016/j.cryobiol.2015.09.003)

Verification: Bibliographic record and abstract checked.

### P12. State of Brain Emulation Report 2025

Niccolò Zanichelli; Maximilian Schons; Isaak Freeman; Philip Shiu; Anton Arkhipov (2025). *arXiv*.

**Evidence:** Report / arXiv.

**Why read:** Surveys neural dynamics, connectomics, emulation and embodiment as the building blocks of brain emulation.

**Limit:** A progress report and research agenda, not evidence of human mind uploading.

[Primary record](https://arxiv.org/abs/2510.15745) | [Open-text link](https://arxiv.org/abs/2510.15745)

Verification: Repository page and abstract checked.

### P13. The Fallacy of Favoring Gradual Replacement Mind Uploading Over Scan-and-Copy

Keith B. Wiley; Randal A. Koene (2015). *arXiv*.

**Evidence:** Philosophy / arXiv.

**Why read:** Argues that gradual replacement and destructive scan-and-copy are equivalent with respect to personal identity.

**Limit:** A contested philosophical argument, not an experiment. The arXiv record also lists a 2016 Journal of Consciousness Studies publication.

[Primary record](https://arxiv.org/abs/1504.06320) | [Open-text link](https://arxiv.org/abs/1504.06320)

Verification: Repository page and abstract checked.

### P14. A theory of neural emulators

Catalin C. Mitelut (2024). *arXiv*.

**Evidence:** Theory / arXiv.

**Why read:** Proposes predictive neural emulators as an alternative route to functionally matching biological systems.

**Limit:** Its claims about indistinguishable cognitive states are conjectures, not demonstrated consciousness transfer.

[Primary record](https://arxiv.org/html/2405.13394) | [Open-text link](https://arxiv.org/html/2405.13394)

Verification: Repository page and abstract checked.

### P15. Neuromorphic Simulation of Drosophila Melanogaster Brain Connectome on Loihi 2

Felix Wang; Bradley H. Theilman; Fred Rothganger; William Severa; Craig M. Vineyard; James B. Aimone (2025). *arXiv*.

**Evidence:** Computational / arXiv.

**Why read:** Maps an adult fruit-fly connectome model onto neuromorphic hardware and compares its dynamics with reference simulations.

**Limit:** Simulation of a simplified fly network does not demonstrate consciousness, learned identity or a human upload.

[Primary record](https://arxiv.org/html/2508.16792v1) | [Open-text link](https://arxiv.org/html/2508.16792v1)

Verification: Repository page and abstract checked.

### P16. Continuum of consciousness: Mind uploading and resurrection of human consciousness. Is there a place for physics, neuroscience and computers?

V. Astakhov (2007). *arXiv*.

**Evidence:** Speculative / arXiv.

**Why read:** Uses a toy information-geometric model to explore a hypothetical migration of mental functions.

**Limit:** Highly speculative thought experiment, not biological or clinical evidence for resurrection.

[Primary record](https://arxiv.org/abs/0710.2556) | [Open-text link](https://arxiv.org/abs/0710.2556)

Verification: Repository page and abstract checked.

### P17. Ascribing Consciousness to Artificial Intelligence

Murray Shanahan (2015). *arXiv*.

**Evidence:** Philosophy / arXiv.

**Why read:** Uses neuronal-replacement thought experiments to examine functionalism and integrated information theory.

**Limit:** Conceptual analysis does not settle whether software is conscious or preserves a particular person.

[Primary record](https://arxiv.org/abs/1504.05696) | [Open-text link](https://arxiv.org/abs/1504.05696)

Verification: Repository page and abstract checked.
