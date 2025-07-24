---
title: Creating an NIH Data Management and Sharing Plan (DMSP)
linkTitle: Creating a Data Management and Sharing Plan
type: docs
weight: 5
---

**[Reproducible neuroimaging principles](/about/principles/#repronims-four-core-principles)**: 1c. Create a DSMP.

The [NIH DMSP](https://grants.nih.gov/grants-process/write-application/forms-directory/data-management-and-sharing-plan-format-page) currently comprises 6 elements covering: 1\)  the type of data and metadata that will be collected and preserved; 2\)  software tools and code required to use the data;  3\) standards used for collecting and organizing data; 4\)  long term data preservation and access;  4\) distribution and reuse considerations; 5\) privacy concerns;  6\)  oversight.

In the following, we give some high level suggestions on creating an effective DMSP using ReproNim principles, tools and practices and provide some sample DMSPs that utilize these practices.
In some cases, we provide several options, ranked from good/basic to best/advanced.
Generally the more advanced options require additional effort to implement.
We also provide some guidance on preparing a DMSP budget for implementing the plan.

## DMSP Plan elements

### Element 1: Data Type

1. **Types and amount of scientific data expected to be generated in the project:**
* The tools and standards developed/promoted by ReproNim are appropriate for all types of MRI data including sMRI, fMRI and DTI
* Share both imaging and behavioral data acquired
  * Share all raw imaging data and derived imaging results
* ReproNim’s principles and core actions are appropriate to all types of data
* Using public data will be used can augment your own data collection.
* Use power analyses or other methods to determine the number of subjects needed to power the study.

2. **Scientific data that will be preserved and shared, and the rationale for doing so:**
* **Raw MRI data**: We always recommend storing the raw data, as different environments, tools and workflows can lead to different results (See:  Everything matters).  For most neuroimaging studies, sharing the DICOM files is sufficient as the transformation from K-space to imaging space is fairly standard.  DICOM files should be shared even if the scans are subsequently translated into other formats. The good news is that properly formatted BIDS, e.g., using Heudiconv/ReproIn maintains the source data alongside the transformed data.
  * If using newer multiband techniques, we recommend sharing the rawest data (K-space) as there are still methodological evolutions occurring for the reconstruction from K-space to imaging space.  In BIDS there is a framework for the rawest data.
* **Transformed data**:  BIDS requires that MRI imaging data be in Nifti format as it is an open standard format
* **Derived data**:  statistical maps, surface maps, volumes should also be shared  (see BIDS derivatives).
* **Behavioral data:**  Results from any behavioral tests administered, e.g., handedness assessments, Hamilton Depression Scale.  We recommend sharing both total scores as well as scores on individual items.  Using BIDS, total scores can be shared via the participant .tsv file.  More granular data, e.g., individual elements of a 40 item scale can go into the [phenotype directory](https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files.html#phenotypic-and-assessment-data).

3. **Metadata, other relevant data, and associated documentation:**

* **Study protocols**: We recommend pre-registering the study protocol using a platform such as the Open Science Framework (osf.io).  Pre-registering your study design, including planned outcome measures,  increases transparency and accountability.
* **Associate relevant metadata with both imaging and behavioral raw data**.  Using BIDS and NIDM provides the means to associate metadata with imaging raw data. Use  ReproSchema to prospectively create a reusable schema for structured behavioral data capture.  Use NeuroBagel to annotate behavioral data retrospectively.
* **Data dictionary:**
  * **Good**: Create a data dictionary to define your variables.  (provide a link to examples)
  * **Best:** Use NIDM to create or map the data dictionary to standard variable names and value sets.  NIDM also provides additional semantics, i.e., the necessary human knowledge for both humans and machines to interpret and relate data elements.  NIDM utilizes community ontologies to provide this knowledge in the form of a common vocabulary and relationships between terms, e.g., FreeSurfer variable *caudate\_left\_volume* maps to the term “caudate nucleus” in the UBERON anatomical ontology.  Caudate nucleus is part of the striatum and telencephalon.
* **Metadata for processing pipelines**:  Metadata is also important for understanding how the data were processed, e.g., when using Freesurfer to generate a volume of the caudate nucleus, information on the Freesurfer run such as what flags were set should be recorded. NIDM provides a standards-compliant way to capture these details.  ReproNim has integrated NIDM into major neuroimaging packages, currently Freesurfer, ANTS, SFL and SPM so that metadata is automatically captured and formatted according to NIDM.

### Element 2: Related Tools, Software and/or Code

What tools can be used to work with shared data?

* By putting data into the BIDS format, users can use BIDS Apps.  [BIDS Apps](https://bids-website.readthedocs.io/en/latest/tools/bids-apps.html) represent a growing collection of containerized environments (typically docker or singularity) the seamless use of applications without the need to install all dependencies, and are generally guaranteed to run on BIDS compliant data.
* Metadata represented in NIDM can be read using NeuroBagel.

Good software management practices are essential for sharing code and workflows effectively, specifically versioning and containerization.

* **Good**:
  * Scripts will be versioned and managed in GitHub and a snapshot of the code used to generate published data will be created in Zenodo using the Git-Hub-Zenodo integration.
  * All  packages used will be identified in metadata for each step using NIDM.
* **Better**: Final workflows and environments are containerized using Neurodocker and shared via GitHub, DockerHub or via DataLad/containers, a repository of neuroimagingReproNim containers.
* **Most advanced**:  DataLad provides complete versioning of data, code and containerized environments via the container player functionalities, associating all elements of data, code and environment for every operation.


### Element 3: Standards

As described in the previous elements, the use of standards greatly simplifies managing and sharing data in the broadest possible way.  ReproNim tools are build on a set of community standards for neuroimaging:

* **BIDS**:  For organizing primary and derived data
* **NIDM** for recording the data and processing workflows.   NIDM is built on top of the Prov model, a W3C standard.  The W3C sets the standards for the World Wide Web.
* **Common data elements**: The NIH is strongly recommending the use of Common Data Elements to capture data in a standardized way.  Many of the common instruments used for behavioral data have CDEs available, e.g., the [Hamilton Depression Scale](https://cde.nlm.nih.gov/cde/search?q=Hamilton%20depression%20scale). ReproNim has created a set of CDEs (aka Federated data elements) that provide a standard for the most common neuroimaging packages.


### Element 4: Data Preservation, Access, and Associated Timelines

1. **Repository where scientific data and metadata will be archived:**

   ReproNim recommends the following repositories for MRI data.
* **OpenNeuro** for open sharing of MRI data.  The use of ReproNim tools, principles and best practices makes public sharing of data (as well as code and workflows) via OpenNeuro efficient as the data will already be compliant with OpenNeuro requirements.
* Harmonized standards-compliant subject level metadata will be stored  in **ReproLake** maintained by ReproNim and made available for query via NeuroBagel.
* **NIMH Data Archive (NDA)/FitBIR** for data that requires access control.  Data in BIDS can be converted to NDA format using the [bids2nda](https://github.com/bids-standard/bids2nda) script.

2. **How scientific data will be findable and identifiable:**

* Both OpenNeuro and NDA issue each dataset a Digital Object Identifier
* Both repositories support the addition of rich metadata to aid in search, including a title and description.  Findability will be enhanced also by giving each dataset a descriptive title that provides key details, e.g., data type, study protocol details, along with a detailed abstract that provides additional details such as the type of cognitive tests used.
* As detailed above, all code and containers will be given identifiers and descriptive metadata via snapshotting in Zenodo.

3. **When and how long the scientific data will be made available:**

Uploading data to a repository can take a while depending on the size and complexity of the data.  We recommend that the data upload process be started when the manuscript is prepared or when the study is completed.  OpenNeuro supports an embargo period if the data are not to be released immediately.  OpenNeuro also supports reviewer tokens so that reviewers can be given access to the data.

* **At time of publication or at completion of study as per NIH requirements**:  Using the ReproNim framework can expedite sharing dramatically (see above)
* Utilizing a trusted repository like OpenNeuro can ensure that data will be available for the long term.

### Element 5: Access, Distribution, or Reuse Considerations

* To ensure that clinical data can be shared to the greatest extent possible, utilize [open consent](https://open-brain-consent.readthedocs.io/en/stable/) when designing your study, even if you plan to fully anonymize your data for open sharing.  Anonymized data is not considered human data and may be freely shared.  However, sharing of clinical data requires authorization by your institutional IRB, and IRBs don’t always agree on what constitutes anonymization. Plus, anonymization is a moving target.  If data access control is required, the repository will ensure that data was consented for broad sharing.

* **Whether access to scientific data will be controlled:**


  Consult with your IRB

* **Protections for privacy, rights, and confidentiality of human research participants:**

	Consult with your IRB

### Element 6: Oversight of Data Management and Sharing

Adhering to ReproNim best practices for managing your data and tools ensures that your institutional official can easily assess whether you are in compliance with your DMSP

## Preparing a budget for implementing the DMSP

The NIH expects that a budget will be provided to cover the costs of implementing your plan.
NDA publishes [a general guide](https://nda.nih.gov/nda/data-contribution#cost) on efforts required to prepare data for submission.
Estimating the exact costs of implementing ReproNim recommendations is difficult because they depend on your current capacities, processes and expertise. 
Changing your current workflow to incorporate BIDS, for example, may require significant effort up front, but once the switch has been made, will likely lower costs overall.
We have prepared [some basic questions](/resources/tutorials/estimating-costs/) to answer that will help determine what resources and effort may be needed.
