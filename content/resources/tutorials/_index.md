---
title: Tutorials
type: docs
weight: 5 
---

To help you get started with ReproNim, we have created a set of  tutorials to show how ReproNim's tools and services support best practices laid out in [ReproNim's principles of reproducible neuroimaging](/about/principles/#repronims-four-core-principles) and [ReproNim's four core actions](/about/principles/#repronims-four-core-actions).

The tutorials are designed in a modular fashion, showing how individual steps to improve reproducibility can be fit together into an [overall reproducible workflow](/about/repronim-approach/).  

Tutorials cover basic and more advanced approaches as noted below. Each tutorial is organized in a similar fashion,  providing a list of tools, necessary skills and system requirements, and step-by-step instructions to implement and use the tools.

For an alternative approach to finding the right tutorial for you, see our [user types and use cases](/resources/getting-started/#user-types-and-use-cases).

## Principle 1: Study planning

_[Actions](/about/principles/#repronims-four-core-actions): Annotation and provenance_

- [Estimating Costs](/resources/tutorials/estimating-costs/): A guide to estimating costs and required resources for implementing reproducible practices.
- [Creating a Data Management and Sharing Plan](/resources/tutorials/data-management-and-sharing/): Tips for creating an NIH Data Management and Sharing Plan.

## Principle 2: Data and metadata management

_[Actions](/about/principles/#repronims-four-core-actions): Use of standards, 
Annotation and provenance, Version control_

- [Converting DICOM to BIDS](/resources/tutorials/dicom-to-bids/): Use ReproNim tools to convert DICOM data to the BIDS standard (*basic*).
- [Creating a Data Dictionary](/resources/tutorials/data-dictionary/): Create a data dictionary for a BIDS dataset (*basic*).
- [Planning a Distributed Project Using ReproSchema](/resources/tutorials/reproschema/): Set up a data collection and annotation framework for a multi-site study.
- [Searching Across Studies Using ReproPond and ReproLake](/resources/tutorials/pond-lake/): Search and share metadata through ReproPond and ReproLake (*advanced*).

Forthcoming:

* Add standards and semantics to data dictionaries to promote data harmonization and findability (*basic+).
* Put your derived data into BIDS derivatives and creating a semantically-enriched data dictionary using NIDM, a standard for annotating neuroimaging data (*advanced*).
  
## Principle 3: Software management

_[Actions](/about/principles/#repronims-four-core-actions): Annotation and provenance Version control, Use of containers_

- [Basic Software Versioning Using Git](/resources/tutorials/git/): Use Git to manage workflow and pipeline versions (*basic*).
- [Streamlining Neuroimaging Processing with Nipoppy](/resources/tutorials/nipoppy/): Curate and process a single study to generate standardized, analysis-ready data for distributed projects (*basic+*).
- [Advanced Containerization Using DataLad](/resources/tutorials/repronim-containers/): Use containers within DataLad for software, data, and metadata management. (*advanced*).

## Principle 4: Publishing everything

Forthcoming:

- Publish all of your work as a "re-executable paper" that includes data, code, and text.
