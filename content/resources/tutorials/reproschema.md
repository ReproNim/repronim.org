---
title: Set Up a Data Collection and Annotation Framework for Multi-Site Behavioral Studies
linkTitle: Planning a Distributed Project Using ReproSchema
type: docs
weight: 5 
---

**[Reproducible neuroimaging principles](/about/principles/#repronims-four-core-principles)**: 2c: Annotate data.

**[Actions](/about/principles/#repronims-four-core-actions)** Standards, Annotation and provenance.

**Standards**: [BIDS](/resources/tools/bids/index.html).

**Tools**: [ReproSchema](/resources/tools/reproschema/index.html).

## Challenge

Managing multi-site behavioral research projects presents significant challenges, including:

* Ensuring consistency across diverse data inputs.  
* Harmonizing data collected from multiple sites with varying methodologies.  
* Preparing data for seamless sharing, analysis, and long-term reuse.  
* ReproSchema addresses these challenges by providing a standardized framework and toolkit for organizing and annotating behavioral data. It integrates easily with existing tools, making data management and sharing both efficient and practical.

Researchers often face difficulties integrating diverse data sources while maintaining reusability and collaboration standards. Projects requiring common data standards, such as shared demographic, clinical, or behavioral measures, are particularly vulnerable to these issues. Without a robust framework like ReproSchema, inconsistencies can compromise the reliability of cross-site analyses and long-term data usability.

## Exercise

In this tutorial, you will learn how to use ReproSchema to:

* Understand its capabilities as a powerful tool for simplifying multi-site behavioral data collection.  
* Design a tailored data collection framework to standardize and harmonize inputs.  
* Master strategies for effectively disseminating data while ensuring consistency and interoperability.

By the end of the tutorial, you will be equipped to set up a reusable and interoperable system for managing behavioral data that aligns with best practices for multi-site research. You will also gain practical knowledge on streamlining cross-site data harmonization and aggregation, enabling immediate analyses and future reuse.

## Before you start

Knowledge Assumed:

* Basic GitHub Usage: Familiarity with navigating GitHub repositories, cloning projects, and reading documentation.  
* Basic Bash Commands: Understanding how to use bash to run scripts and manage files in a terminal.

Recommended Preparation:

* GitHub Basics: If you’re new to GitHub, review the [GitHub Getting Started Guide](https://docs.github.com/en/get-started) to learn about cloning repositories and accessing project files.  
* Bash Basics: For a refresher on bash commands, consult resources like the [GNU Bash Manual](https://www.gnu.org/software/bash/manual/) or beginner-friendly guides such as [Bash Command Cheat Sheets](https://github.com/RehanSaeed/Bash-Cheat-Sheet).

## Step by step guide

### Step 1: Know the foundations

ReproSchema is built on a foundation of principles and features that make it a powerful tool for managing behavioral data in multi-site projects. Understanding these foundational aspects will help you appreciate how it simplifies data collection and ensures harmonization across diverse research settings.

This is an example of a typical assessment presented in the reproschema format:

![A diagram of a hypothetical assessment and how it would appear in ReproSchema.](/images/reproschema_1.png)

Essential components in ReproSchema: 

* A foundational schema (reproschema, [https://github.com/ReproNim/reproschema](https://github.com/ReproNim/reproschema)) standardizes the structure and presentation of assessments, defining relationships between data elements and their metadata. It requires each data element, like survey responses or experimental measurements, to be linked with contextual information, including the collection method, timing, and conditions.  
* A library ([https://github.com/ReproNim/reproschema-library](https://github.com/ReproNim/reproschema-library)) of standardized, reusable assessments, each formatted in JSON-LD according to criteria defined by the schema.  
* A Python package ([https://github.com/ReproNim/reproschema-py](https://github.com/ReproNim/reproschema-py)) that supports schema creation and validation, including tools for converting schemas to compatible formats like those used in REDCap and the Fast Healthcare Interoperability Resources (FHIR) standard.  
* A user interface (UI, [https://github.com/ReproNim/reproschema-ui](https://github.com/ReproNim/reproschema-ui)) designed to optimize data collection.  
* A cookiecutter (i.e., template, [https://github.com/ReproNim/reproschema-protocol-cookiecutter](https://github.com/ReproNim/reproschema-protocol-cookiecutter)) that enables the creation of customized research protocols using the library and the UI. 

![A diagram of the connections between the parts of ReproSchema.](/images/reproschema_2.png)

### Step 2: Set up ReproSchema for data collection

Effective setup of ReproSchema begins with careful planning, hands-on configuration, and deployment strategies tailored to your research needs. This section will guide you through each step to create a functional and robust data collection framework.

1. **Planning the Data Collection Framework**: Identify the data types your project requires. This includes shared data fields (e.g., demographics, clinical measures) that all sites will collect and site-specific data that may vary. Collaborate with your team to standardize common elements while allowing flexibility for unique site needs. Use ReproSchema’s templates to create schemas that align with these goals, ensuring they are structured for consistency and scalability.  
2. **Demo Protocol:** Check this demo-protocol ([https://github.com/ReproNim/demo-protocol](https://github.com/ReproNim/demo-protocol)) to have a sense of what type of questions ReproSchema supports and how they look in use  
3. **Create Your Project**: Use this cookiecutter to create your project: [https://github.com/ReproNim/reproschema-protocol-cookiecutter](https://github.com/ReproNim/reproschema-protocol-cookiecutter)   
4. **Library of Assessments:** You don’t have to create your assessments from scratch; we have collected widely used assessments and converted them into ready-to-use reproschema format in this library: [https://github.com/ReproNim/reproschema-library](https://github.com/ReproNim/reproschema-library). You can also contribute to this library by   
5. **Convert from Existing Platforms:** If you have your questionnaire from REDCap and want to convert to ReproSchema, we have a conversion tool here: [https://github.com/ReproNim/reproschema-py](https://github.com/ReproNim/reproschema-py)   
6. **Deploying ReproSchema**: This repository ([https://github.com/ReproNim/reproschema-backend](https://github.com/ReproNim/reproschema-backend)) details how to run ReproSchema locally. 

## Use cases

ReproSchema has been effectively employed in various research contexts, demonstrating its versatility and value for multi-site projects. Here are some practical and inspiring examples:

1. **NIMH-Minimal Initiative**: The [NIMH-Minimal](https://github.com/ReproNim/nimh-minimal) repository converts NIH data elements into the reproschema to create standardized measures for mental health research that can be used across team with tracked changes.  
2. **Adolescent Brain Cognitive Development (ABCD) Study**: The [ABCD study](https://github.com/ReproNim/abcd-redcap2rs) leverages ReproSchema to harmonize behavioral data collected from thousands of participants across numerous sites. This standardization supports complex longitudinal analyses and comparisons.  
3. **HEALthy Brain and Child Development (HBCD) Study**: The [HBCD study](https://github.com/ReproNim/hbcd-redcap2rs) applies ReproSchema to integrate data on child development from diverse locations. The framework simplifies clinical and behavioral data collection coordination.  
4. **Bridge2AI Project**: The [Bridge2AI project](https://github.com/sensein/b2ai-redcap2rs) uses ReproSchema to annotate and manage behavioral data across different teams.  
5. **eCOBIDAS Checklist**: The [Best Practices in Data Analysis and Sharing Checklist (eCOBIDAS)](https://github.com/ohbm/eCOBIDAS) employs ReproSchema to provide researchers with a standardized checklist for ensuring reproducibility and transparency in neuroscience studies. 

## Next steps

If you are a researcher embarking on a multi-site project, this tutorial provides the tools and knowledge to set up and manage your data using ReproSchema confidently. From creating standardized schemas to deploying workflows that ensure consistency, you’re now equipped to tackle the complexities of behavioral data collection and analysis efficiently.

To dive deeper, explore ReproNim’s comprehensive [documentation](https://github.com/ReproNim/reproschema) and connect with its active community for support and collaboration through GitHub. You’ll find many resources to guide your journey, including example schemas and practical templates.

Get started today by setting up your first ReproSchema project. Experiment with its features, integrate it into your existing workflows, and see how it transforms your data management and analysis approach. The possibilities for enhancing research quality and collaboration are endless, and ReproSchema is here to support you every step.
