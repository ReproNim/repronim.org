---
title: Tutorials
type: docs
weight: 5 
---

To help you get started with ReproNim, we have created a set of  tutorials to show how ReproNim's tools and services support best practices laid out in [ReproNim's principles of reproducible neuroimaging](/about/principles/#repronims-four-core-principles) and [ReproNim's four core actions](/about/principles/#repronims-four-core-actions).

The tutorials are designed in a modular fashion, showing how individual steps to improve reproducibility can be fit together into an [overall reproducible workflow](/about/repronim-approach/).  

Tutorials cover basic and more advanced approaches as noted below. Each tutorial is organized in a similar fashion,  providing a list of tools, necessary skills and system requirements, and step-by-step instructions to implement and use the tools.

For an alternative approach to finding the right tutorial for you, see our [user types and use cases](/resources/getting-started/#user-types-and-use-cases).

For additional tutorials on the use of specific tools, see our [Tools page](https://repronim.org/resources/tools/).

## Principle 1: Study planning

_[Actions](/about/principles/#repronims-four-core-actions): Annotation and provenance_

- [Estimating Costs](/resources/tutorials/estimating-costs/): A guide to estimating costs and required resources for implementing reproducible practices.
- [Creating a Data Management and Sharing Plan](/resources/tutorials/data-management-and-sharing/): Tips for creating an NIH Data Management and Sharing Plan.

## Principle 2: Data and metadata management

_[Actions](/about/principles/#repronims-four-core-actions): Use of standards, 
Annotation and provenance, Version control_

- [Converting DICOM to BIDS](/resources/tutorials/dicom-to-bids/): Use ReproNim tools to convert DICOM data to the BIDS standard (*basic*).
- [Creating a Data Dictionary](/resources/tutorials/data-dictionary/): Create a data dictionary for a BIDS dataset (*basic*).
- [Annotating FreeSurfer Data](/resources/tutorials/freesurfer/): Annotate FreeSurfer data (*basic*).
- [Annotating FSL Data](/resources/tutorials/fsl/): Annotate FSL data (*basic*).
- [Planning a Distributed Project Using ReproSchema](/resources/tutorials/reproschema/): Set up a data collection and annotation framework for a multi-site study.
- [Searching Across Studies Using ReproPond and ReproLake](/resources/tutorials/pond-lake/): Search and share metadata through ReproPond and ReproLake (*advanced*).

Forthcoming:

* Add standards and semantics to data dictionaries to promote data harmonization and findability (*basic+).
* Put your derived data into BIDS derivatives and creating a semantically-enriched data dictionary using NIDM, a standard for annotating neuroimaging data (*advanced*).
  
## Principle 3: Software management

_[Actions](/about/principles/#repronims-four-core-actions): Annotation and provenance Version control, Use of containers_

- [Basic Software Versioning Using Git](/resources/tutorials/git/): Use Git to manage workflow and pipeline versions (*version control: basic*).
- [Using Neurodocker to containerize computational workflows](/resources/tutorials/neurodocker/): Use Neurodocker to automatically generate custom Dockerfiles and Singularity recipes for neuroimaging applications. (*containers: basic*)
- [Advanced Containerization Using DataLad](/resources/tutorials/repronim-containers/): Use containers within DataLad for software, data, and metadata management. (*containers: advanced*).
- [Streamlining Neuroimaging Processing with Nipoppy](/resources/tutorials/nipoppy/): Curate and process a single study to generate standardized, analysis-ready data for distributed projects (*annotation: basic+*).

## Principle 4: Publishing everything

- [Publish all of your work as a "re-executable paper"](/resources/tutorials/publish-everything/) that includes data, code, and text.
