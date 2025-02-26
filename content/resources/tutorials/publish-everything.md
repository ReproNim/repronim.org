---
title: "Publishing Everything: Publishing re-executable papers"
linkTitle: Publishing Everything
type: docs
weight: 5
---

**[Reproducible neuroimaging principles](/about/in-practice/#repronims-principles-of-reproducible-neuroimaging)**:

4\. Publishing everything: publishing re-executable publications  
4a\. Plans should be shared (pre-registration)  
4b\. Software should be shared  
4c\. Data should be shared  
4d\. All research objects should be FAIR  

**[Actions](/about/in-practice/#repronims-four-core-actions)**: Use Standards, Provide Annotation and Provenance

**Standards**: [BIDS](/resources/tools/bids/index.html)

## Challenge

The scientific publication is a main outcome of our research endeavor.
Scientific publications, by definition, are supposed to convey the necessary information for someone to replicate the observation.
We have learned over the past decades, that words like “...acquire a structural MRI scan…” and “...use software package X…” do not sufficiently capture the necessary information for someone to replicate the observation.
In order to convey a neuroimaging finding in a replicable fashion, one needs to include *precise and complete* information about the data, software, workflow, and derived results that comprise the publication.
Fortunately, there are methods for sharing each of these types of information in the context of a publication, rendering the publication more replicable.

## Exercise

This ‘exercise’ builds on the prior tutorial exercises.
Each of these tutorials created a shareable product that will comprise the re-executable paper.
If these steps were followed, then “sharing everything” is as straightforward as uploading your primary and derived data to a trusted community repository, e.g., OpenNeuro, and including links to the workflow that created it.

1. We assume that the MRI data collection was converted to BIDS, and that the data dictionary was generated.
   This **BIDS representation of the raw data** for the publication can be shared to a resource such as OpenNeuro.
   OpenNeuro will keep track of versioning and DOI generation for this source data.
2. We assume that the **software being used was containerized**.
   This container can be shared using DockerHub.
3. We assume that the **processing script (**i.e. the set of commands that uses the above container) was managed using Git, and can be shared via  GitHub.
   As GitHub repositories can evolve from what was the version actually used in a publication, the state of the GitHub repository that matches that used in the publication can be snapshotted and archived using Zenodo, which will also generate a DOI.
   Instructions can be found [here](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).
4. The **results of running the workflow** on the data can be added to the BIDS/derivatives representation of the dataset (a discussion of BIDS/Derivatives can be found [here](https://bids-specification.readthedocs.io/en/stable/derivatives/introduction.html)).
   This can be shared (or version updated if the original data was already shared) to OpenNeuro.
5. If separate **statistical analysis** was performed, this can be managed using Git, and can be shared at GitHub, and archived using Zenodo, as indicated above.
6. Now the publication can include FAIR pointers, i.e., a reference to the DOI or equivalent identifier,  to each of the critical elements that went into the observations and conclusions that it reaches, facilitating the replication and generalizability of its findings.
   These pointers should be included in the methods section and/or the data and tool availability section.

## Examples

There are a number of published examples that embody this publication of a complete re-executable paper concept.
Of particular note is Ghosh SS, Poline JB, Keator DB et al.
A very simple, re-executable neuroimaging publication, F1000Research 2017, 6:124 ([https://doi.org/10.12688/f1000research.10783.2](https://doi.org/10.12688/f1000research.10783.2)).
In that paper, the authors document this set of procedures, which include supplemental additions to a manuscript, that unambiguously define the data, workflow, execution environment and results of a neuroimaging analysis, in order to generate a verifiable re-executable publication.
As indicated in the “Software and data availability” section of that publication:

* Workflow and results are available on GitHub at: [https://github.com/ReproNim/simple\_workflow](https://github.com/ReproNim/simple_workflow).
* Archived workflow and results as at time of publication: doi, [10.5281/zenodo.800758](https://zenodo.org/records/800758) (Ghosh et al., 2017).
* Shared Docker image: [https://hub.docker.com/r/repronim/simple\_workflow/tags/](https://hub.docker.com/r/repronim/simple_workflow/tags/)
* The data used in this publication are available at NITRC-IR (project, fcon\_1000; image collection: doi, [10.18116/C6C592](http://iaf.virtualbrain.org/slp/10.18116/C6C592) \- Kennedy, 2017).
  These data were originally gathered from the NITRC-IR, 1000 Functional Connectomes project, Ann Arbor and New York sub-projects.

All resources were released with the permissive Apache License, Version 2.0.

From these linked resources, one can identify the used data exactly; access a identical containerized version of the processing workflow, operating system and environment, and access the complete results from the original analysis, thus supporting the potential to re-execute the original work, and, more importantly, providing the opportunity to extend that work to other (or additional) data or variations of the workflow design.
Do YOU know of other re-executable publications?
[Let us know,](mailto:info@repronim.org) we’d love to collect more examples\!
