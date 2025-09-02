---
linkTitle: "Data management"
title: "ReproNim Principle 2: Data and Metadata Management"
type: docs
weight: 90
---
Data and metadata management is essential for scientific reproducibility as they provide the foundation for understanding, validating, and building upon research findings. Through comprehensive documentation of experimental conditions, data collection methods, and analysis workflows, researchers can capture the critical context needed to understand and replicate their work ([Borghi and Van Gulick, 2018](https://riojournal.com/articles.php?id=26439)). Management includes preserving both raw and processed data in accessible formats, maintaining clear version control, and implementing standardized metadata schemas. When data is properly managed with detailed documentation, researchers can access, understand, and work with the exact same dataset, well beyond the initial time frame in which the data were produced

1. **Use standard data formats and extend them to meet your needs**
   Standardized approaches for data and metadata management provide a common framework that ensures consistency in how data is documented, organized, and shared across the laboratory and with colleagues. This standardization makes it easier for you, your lab mates, your collaborators and colleagues to understand and use data, as they can quickly interpret the metadata structure and data organization. Adopting established, i.e., community, standards streamlines data integration, enables automated processing, and facilitates long-term preservation by ensuring that data remains accessible and interpretable even as technology evolves. Use of community standards is explicitly called out in the FAIR data principles ([Wilkinson et al., 2016](https://pubmed.ncbi.nlm.nih.gov/26978244/)) as a key requirement for reusability. Whether through standardized metadata schemas, controlled vocabularies, or common file formats, these practices ultimately enhance data quality, research efficiency, and the potential for data reuse.

* ***ReproNim resources***
  * [BIDS](/resources/tools/bids/):  Brain Imaging Data Structure, a community standard for organizing and describing neuroimaging data
  * [NIDM](/resources/tools/nidm/):  Neuroimaging Data Model, a community metadata standard for neuroimaging studies
  * [ReproIn](/resources/tools/reproin/): Convention and helpers for naming and organization of MRI sequences for turnkey DICOM to BIDS conversion.
  * Neuroimaging CDEs:
  * [ReproSchema](/resources/tools/reproschema/): A standardized framework for organizing and annotating behavioral assessment data
    * Tutorial: [Setting Up a Data Collection and Annotation Framework for Multi-Site Behavioral Studies](/resources/tutorials/reproschema/)



* ***Other resources***:
  * [BIDS Website](https://bids.neuroimaging.io/):  Official BIDS website, includes related BIDS standards and a catalog of tools that work with BIDS
  * [INCF Standards and Best Practices portfolio](https://www.incf.org/resources/sbps#:~:text=The%20Standards%20and%20Best%20Practices,the%20process%20of%20being%20endorsed.):  A catalog of standards and best practices for neuroscience that have been vetted by the INCF and community review
  * GO-FAIR:  C[ommunity standards and FAIR](https://www.go-fair.org/fair-principles/r1-3-metadata-meet-domain-relevant-community-standards/)

2. **Use version control from start to finish**
   Versioning provides a systematic way to track changes and maintain the integrity of research data over time. When data is versioned properly, researchers can trace the evolution of their datasets, understanding exactly what changes were made, when they occurred, and who made them. When errors are discovered, teams can easily revert to previous versions or identify when and where any issues were introduced. Versioning also supports collaboration by allowing multiple researchers to work with the same dataset while maintaining a clear record of modifications and preventing conflicting changes. In addition, version control ensures reproducibility by enabling researchers to reference and access specific versions of datasets that were used for particular analyses or publications. So even as datasets continue to be updated and refined, the exact data state used for any given research output can be preserved and accessed, making it possible to verify and build upon previous findings with confidence.

* ***Some things you can do***
  * ***Learn more:***
    * Tutorial:  [Version control systems](https://www.repronim.org/module-reproducible-basics/02-vcs/)
    * [**Yoda Principles**](https://handbook.datalad.org/en/latest/basics/101-127-yoda.html):  Version everything and build everything off these versions. Three simple rules for making it easier to track versions across datasets and code through consistent directory names and structures.

  * ***Some things you can try:***
    * Git-based approaches: Adapts Git (with Git-LFS for large files) to version data alongside code. Benefits from familiar branching and merging workflows but can struggle with very large datasets.
    * [DVC (Data Version Control)](https://dvc.org/): Purpose-built for data science, storing large files in cloud storage while tracking metadata in Git. Integrates with ML pipelines and tracks experiments while efficiently handling large datasets.
    * [Pachyderm](https://docs.pachyderm.com/products/mldm/latest/learn/basic-concepts/): Container-based system that versions both data and processing code together, ensuring reproducibility and providing automatic lineage tracking in data pipelines.
    * [**DataLad**](/resources/tools/datalad/): Advanced software platform for managing and sharing data.  DataLad automatically tracks all versions of data
3. **Annotate data using standard, reproducible procedures**
   Data annotation is the systematic process of adding labels, tags, or descriptive information to raw data to make it more meaningful and usable for analysis. Using standardized annotation practices, i.e., using common vocabularies and well documented annotation guidelines,  creates a consistent framework for documenting research data, making it easier for other lab members and colleagues to annotate, understand and interpret the information correctly. When annotations follow established procedures, they provide clear, unambiguous descriptions of data elements, experimental conditions, and methodological choices. This standardization reduces the risk of misinterpretation and makes it possible to compare data across different studies or time periods reliably.  Standardized annotations are a cornerstone of FAIR, as they make the data more findable, interoperable and reusable. When annotations follow well-defined standards used across the broader community, they create a reliable foundation for data sharing, reuse, and long-term preservation, ultimately contributing to the broader goals of open science and research reproducibility.

* ***ReproNim resources***:

  ReproNim provides a suite of tools and standards for annotating and querying key steps in a neuroimaging study to common standards, e.g.,  [NIDM](/resources/tools/nidm/)

  * Tools:
    * [PyNIDM](/resources/tools/neurobagel/):
      * Tutorial: [Creating a BIDS Data Dictionary and Adding Semantics](/resources/tutorials/data-dictionary/).  How to create a data dictionary to document and annotate *participant metadata* in a BIDS formatted dataset, and add semantic, i.e., meaning,  to variables collected using the [NIDM](/resources/tools/nidm/) standard.
    * [ReproSchema](/resources/tools/reproschema/): A standardized framework for organizing and annotating *behavioral assessment data*
      * Tutorial: [Setting Up a Data Collection and Annotation Framework for Multi-Site Behavioral Studies](/resources/tutorials/reproschema/)
    * [Neurobage](/resources/tools/neurobagel/)l: A system for distributed data sharing and discovery built on common annotations across the workflow
      * Tutorial: [Sharing and Searching Metadata Using a ReproPond and the ReproLake](/resources/tutorials/pond-lake/)
