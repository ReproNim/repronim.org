---
title: "Tools"
date: 2024-10-28T15:14:39-04:00
weight: 10
---

This section describes core tools and standards produced by ReproNim. Each tool page has a description of the tool, the [principles and actions](/about/principles/) to which it applies and provides information on how to access the tool along with links to help materials, useful references and [tutorials](/resources/tutorials/). 

For a general orientation to ReproNim resources, we suggest reviewing the [Getting started with ReproNim](/resources/getting-started/) and [Resources](/resources/) overviews.

## Core Standards

- The Brain Imaging Data Structure ([BIDS](bids/index.html)): A standard for organizing neuroimaging data and metadata on disk.
- The Neuroimaging Data Model ([NIDM](nidm/index.html)): A Semantic Web extension for neuroimaging concepts.

## Core Tools

- [DataLad](datalad/index.html): Software for data versioning and distribution.
- [HeuDiConv](heudiconv/index.html): A DICOM to BIDS converter.
- [Neurobagel](neurobagel/index.html): A set of tools to query and share clinical and brain imaging data.
- [Neurodocker](neurodocker/index.html): A tool to generate custom Dockerfiles and Singularity recipes to containerize neuroimaging tools.
- [Nipoppy](nipoppy/index.html): A command line tool to manage a complete neuroimaging processing workflow.
- [PyNIDM](pynidm/index.html): A command line tool for working with NIDM data.
- [ReproSchema](reproschema/index.html): A tool for defining, sharing, and reusing structured research protocols, enabling versioning and interoperability across studies.

## Infrastructure

- [ReproLake](reprolake/index.html): A public triplestore of neuroimaging metadata.

## Best Practices

- [ReproIn](reproin/index.html): Convention and helpers for naming and organization of MRI sequences for turnkey DICOM to BIDS conversion.

## Additional Associated Tools

In addition to our [Core Tools](#core-tools), ReproNim has developed an extensive set of additional tools that serve more specialized purposes. These include:

* [BABS](https://github.com/PennLINC/babs) \- BIDS App Bootstrap System for streamlining neuroimaging processing workflows with containerized BIDS Apps ([paper](https://doi.org/10.1162/imag_a_00074))
* [con/duct](https://github.com/con/duct) \- A helper to run a command, capture stdout/stderr and execution metadata
* [ReproMan](https://github.com/ReproNim/reproman) \- Simplify creation and management of computing environments in Neuroimaging
* [Open Brain Consent](https://open-brain-consent.readthedocs.io/en/stable/) \- Make open data sharing a no-brainer for ethics committees
* [repromon](https://github.com/ReproNim/repromon) \- A service to monitor data acquisition etc to alert if anything goes wrong
* [testkraken](https://github.com/ReproNim/testkraken) \- Generalized regression testing of scientific workflows
* [reprostim](https://github.com/ReproNim/reprostim) \- Automated capture of audio-visual stimuli into BIDS datasets
* [reproflow](https://github.com/ReproNim/reproflow) \- Materials for ReproFlow: ReproNim tools to establish scalable and automated MRI and behavioral data acquisition and QC
* [reprozip](https://github.com/ReproNim/reprozip) \- ReproZip is a tool that simplifies the process of creating reproducible experiments from command-line executions, a frequently-used common denominator in computational science.


### NIDM Converters

The following tools support conversion of the outputs of specific tools into the NIDM representation.
* FreeSurfer
  * [segstats\_jsonld](https://github.com/ReproNim/segstats_jsonld) \- Script to Export Freesurfer-based Parcellation/Segmentation Stats and Provenance as JSON-LD and NIDM
* FSL
  * [fsl\_seg\_to\_nidm](https://github.com/ReproNim/fsl_seg_to_nidm) \- Converts structural segmentation outputs from FSL's FIRST and FAST tool to NIDM
* ANTS
  * [ants\_seg\_to\_nidm](https://github.com/ReproNim/ants_seg_to_nidm) \- ANTS-based structural segmentation exporter to NIDM




