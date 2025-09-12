---
title: Creating an NIH Data Management and Sharing Plan
linkTitle: Creating a Data Management and Sharing Plan
type: docs
weight: 5
---

**[Reproducible neuroimaging principles](/about/principles/#repronims-four-core-principles)**: 1c. Create a DMSP.

An [NIH Data Management and Sharing Plan](https://grants.nih.gov/grants-process/write-application/forms-directory/data-management-and-sharing-plan-format-page) (DMSP) currently comprises 6 elements covering 1\) the type of data and metadata that will be collected and preserved, 2\) software tools and code required to use the data, 3\) standards used for collecting and organizing data, 4\) long term data preservation and access, 5\) distribution, reuse, and privacy considerations, and 6\) oversight.

In the following, we give some high level suggestions on creating an effective DMSP using ReproNim principles, tools, and practices and provide some sample DMSPs that utilize these practices.  In some cases we provide several options, ranked from good/basic to best/advanced.  Generally the more advanced options require additional effort to implement.  We also provide some guidance on preparing a DMSP budget for implementing the plan.

Below, we reproduce the template from the [Data Management and Sharing Plan Format Page](https://grants.nih.gov/sites/default/files/uploaded/DMS-Plan-blank-format-page.docx) (DOCX, 36 KB), including numbered elements, lettered subsections, and instructions (in italics).  Bullet points contain ReproNim suggestions.

### Element 1: Data Type

**A. Types and amount of scientific data expected to be generated in the project**

*Summarize the types and estimated amount of scientific data expected to be generated in the project.*

- ReproNim’s [principles and core actions](/about/principles/) are appropriate to all types of data.
- The tools and standards developed or promoted by ReproNim are appropriate for all types of MRI data including sMRI, fMRI, and DTI.
- Share both imaging and behavioral data acquired.  Share all raw imaging data as well as derived imaging results.
- Use public data to augment your own data collection.
- Use power analyses or other methods to determine the number of subjects needed to power the study.

**B. Scientific data that will be preserved and shared, and the rationale for doing so**

*Describe which scientific data from the project will be preserved and shared and provide the rationale for this decision.*

- **Raw MRI data**: We always recommend storing the raw data because different environments, tools, and workflows can lead to different results (see [ReproNim Principle 4: Publishing everything](/about/principles/publish_everything/)).  For most neuroimaging studies, sharing the DICOM files is sufficient as the transformation from K-space to imaging space is fairly standard.  DICOM files should be shared even if the scans are subsequently translated into other formats. The good news is that properly formatted BIDS, e.g., using HeuDiConv/ReproIn, maintains the source data alongside the transformed data.
    - If using newer multiband techniques, we recommend sharing the rawest data (K-space) as there are still methodological evolutions occurring for the reconstruction from K-space to imaging space.  In BIDS there is a framework for the rawest data.
- **Transformed data**: BIDS requires that MRI imaging data be in NIfTI format as it is an open standard format.
- **Derived data**: Statistical maps, surface maps, and volumes should also be shared (see [BIDS derivatives](https://bids-specification.readthedocs.io/en/stable/derivatives/introduction.html)).
- **Behavioral data**: Share results from any behavioral tests administered, e.g., handedness assessments, Hamilton Depression Scale.  We recommend sharing both total scores as well as scores on individual items.  Using BIDS, total scores can be shared via the participant TSV file.  More granular data, e.g., individual elements of a 40 item scale, can go into the phenotype directory.

**C. Metadata, other relevant data, and associated documentation**

*Briefly list the metadata, other relevant data, and any associated documentation (e.g., study protocols and data collection instruments) that will be made accessible to facilitate interpretation of the scientific data.*

- **Study protocols**: We recommend pre-registering the study protocol using a platform such as the [Open Science Framework](https://osf.io).  Pre-registering your study design, including planned outcome measures, increases transparency and accountability.
- **Metadata for imaging and behavioral raw data**.  Using BIDS and NIDM provides the means to associate metadata with imaging raw data. Use ReproSchema to prospectively create a reusable schema for structured behavioral data capture.  Use NeuroBagel to annotate behavioral data retrospectively.
- **Data dictionary**:
  - **Good**: Create a data dictionary to define your variables.
  - **Best**: Use NIDM to create or map the data dictionary to standard variable names and value sets.  NIDM also provides additional semantics, i.e., the necessary human knowledge for both humans and machines to interpret and relate data elements.  NIDM utilizes community ontologies to provide this knowledge in the form of a common vocabulary and relationships between terms, e.g., FreeSurfer variable *caudate\_left\_volume* maps to the term “caudate nucleus” in the Uberon anatomical ontology, and "caudate nucleus" is part of the "striatum" and "telencephalic nucleus."
- **Metadata for processing pipelines**: Metadata is also important for understanding how the data were processed, e.g., when using FreeSurfer to generate a volume of the caudate nucleus, information on the FreeSurfer run such as what flags were set should be recorded. NIDM provides a standards-compliant way to capture these details.  ReproNim has integrated NIDM into major neuroimaging packages, currently FreeSurfer, ANTS, SFL, and SPM, so that metadata is automatically captured and formatted according to NIDM.

### Element 2: Related Tools, Software and/or Code

*State whether specialized tools, software, and/or code are needed to access or manipulate shared scientific data, and if so, provide the name(s) of the needed tool(s) and software and specify how they can be accessed.*

- By putting data into the BIDS format, users can use [BIDS Apps](https://bids-website.readthedocs.io/en/latest/tools/bids-apps.html).  BIDS Apps represent a growing collection of containerized environments (typically Docker or Singularity) and are generally guaranteed to run on BIDS compliant data.
- Metadata represented in NIDM can be read using NeuroBagel.
- Good software management practices, specifically versioning and containerization, are essential for sharing code and workflows effectively.
    - **Good**: Scripts are versioned and managed in GitHub and a snapshot of the code used to generate published data will be created in Zenodo using the GitHub-Zenodo integration.  All packages used are identified in metadata for each step using NIDM.
    - **Better**: Final workflows and environments are containerized using Neurodocker and shared via GitHub, Docker Hub, or via DataLad/containers, a repository of neuroimaging ReproNim containers.
    - **Most advanced**: DataLad provides complete versioning of data, code, and containerized environments (via the container player functionalities), associating all elements of data, code, and environment for every operation.

### Element 3: Standards

*State what common data standards will be applied to the scientific data and associated metadata to enable interoperability of datasets and resources, and provide the name(s) of the data standards that will be applied and describe how these data standards will be applied to the scientific data generated by the research proposed in this project.  If applicable, indicate that no consensus standards exist.*

- As described in the previous elements, the use of standards greatly simplifies managing and sharing data in the broadest possible way.  ReproNim tools are built on a set of community standards for neuroimaging, including:
    - **BIDS** for organizing primary and derived data.
    - **NIDM** for recording the data and processing workflows.  NIDM is built on top of the Prov model, a W3C standard.  The W3C sets the standards for the World Wide Web.
    - **Common data elements** (CDEs) for capturing data in a standardized way.  Many of the common instruments used for behavioral data have [NIH CDEs](https://cde.nlm.nih.gov/home) available. ReproNim has created a set of CDEs (aka Federated data elements) that provide a standard for the most common neuroimaging packages.

### Element 4: Data Preservation, Access, and Associated Timelines

**A. Repository where scientific data and metadata will be archived**

*Provide the name of the repository(ies) where scientific data and metadata arising from the project will be archived; see [Selecting a Data Repository](https://grants.nih.gov/policy-and-compliance/policy-topics/sharing-policies/dms/selecting-a-data-repository)).*

- ReproNim recommends the following repositories for MRI data:
    - **[OpenNeuro](https://openneuro.org/)** for open sharing of MRI data.  The use of ReproNim tools, principles and best practices makes public sharing of data (as well as code and workflows) via OpenNeuro efficient as the data will already be compliant with OpenNeuro requirements.
    - **ReproLake** for harmonized standards-compliant subject level metadata.  ReproLake is maintained by ReproNim and its data is available for query by NeuroBagel.
    - **[NIMH Data Archive (NDA)](https://nda.nih.gov/) or [FITBIR](https://fitbir.nih.gov/)** for data that requires access control.  Data in BIDS can be converted to NDA format using the [bids2nda](https://github.com/bids-standard/bids2nda) script.

**B. How scientific data will be findable and identifiable**

*Describe how the scientific data will be findable and identifiable, i.e., via a persistent unique identifier or other standard indexing tools.*

- Both OpenNeuro and NDA issue each dataset a Digital Object Identifier.
- Both repositories support the addition of rich metadata, including a title and description, to aid searching.  Findability is enhanced by giving each dataset a descriptive title that provides key details, e.g., data type, and study protocol details, along with a detailed abstract that provides additional details such as the type of cognitive tests used.
- All code and containers are given identifiers and descriptive metadata by snapshotting in Zenodo.

**C. When and how long the scientific data will be made available**

*Describe when the scientific data will be made available to other users (i.e., no later than time of an associated publication or end of the performance period, whichever comes first) and for how long data will be available.*

- Uploading data to a repository can take a while depending on the size and complexity of the data.  We recommend that the data upload process be started when the manuscript is prepared or when the study is completed.  OpenNeuro supports an embargo period if the data are not to be released immediately.  OpenNeuro also supports reviewer tokens so that reviewers can be given access to the data.
- Utilizing a trusted repository like OpenNeuro can ensure that data will be available for the long term.

### Element 5: Access, Distribution, or Reuse Considerations

**A. Factors affecting subsequent access, distribution, or reuse of scientific data**

*NIH expects that in drafting Plans, researchers maximize the appropriate sharing of scientific data. Describe and justify any applicable factors or data use limitations affecting subsequent access, distribution, or reuse of scientific data related to informed consent, privacy and confidentiality protections, and any other considerations that may limit the extent of data sharing. See [Frequently Asked Questions](https://grants.nih.gov/faqs#/data-management-and-sharing-policy.htm) for examples of justifiable reasons for limiting sharing of data.*

- To ensure that clinical data can be shared to the greatest extent possible, utilize [Open Brain Consent](https://open-brain-consent.readthedocs.io/en/stable/) when designing your study, even if you plan to fully anonymize your data for open sharing.  Anonymized data is not considered human data and may be freely shared.  However, sharing of clinical data requires authorization by your IRB, and IRBs don’t always agree on what constitutes anonymization.  In addition, anonymization is a moving target.  If data access control is required, the repository will ensure that data was consented for broad sharing.

**B. Whether access to scientific data will be controlled**

*State whether access to the scientific data will be controlled (i.e., made available by a data repository only after approval).*

- Consult with your IRB.

**C. Protections for privacy, rights, and confidentiality of human research participants**

*If generating scientific data derived from humans, describe how the privacy, rights, and confidentiality of human research participants will be protected (e.g., through de-identification, Certificates of Confidentiality, and other protective measures).*

- Consult with your IRB.

### Element 6: Oversight of Data Management and Sharing

*Describe how compliance with this Plan will be monitored and managed, frequency of oversight, and by whom at your institution (e.g., titles, roles).*

- Adhering to ReproNim best practices for managing your data and tools ensures that your institutional official can easily assess whether you are in compliance with your DMSP.

## Preparing a budget for implementing the DMSP

The NIH expects that a budget is provided to cover the costs of implementing your plan.  NDA publishes [a general guide](https://nda.nih.gov/nda/data-contribution#cost) on efforts required to prepare data for submission.  Estimating the exact costs of implementing ReproNim recommendations is difficult because they depend on your current capacities, processes, and expertise.  Changing your current workflow to incorporate BIDS, for example, may require significant effort up front, but once the switch has been made, it will likely lower costs overall.  We have prepared [some basic questions](/resources/tutorials/estimating-costs/) to help determine what resources and effort may be needed.
