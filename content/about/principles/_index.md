---
title: "Reproducible Neuroimaging: Principles and Actions"
weight: 1
type: docs
---

<!--
The style section will cause the sub-lists to be labeled with lowercase
letters.

Use care when modifying the principles since there are hard coded
references to them (by NUMBER.LETTER) on other pages.
-->

## ReproNim's four core principles

Note:  These principles are a reformulation of ReproNim's [5 Steps to Reproducible Neuroimaging](https://legacy.repronim.org/5steps)

<style>
    ol ol li { list-style-type: lower-alpha; }
</style>

<!-- proposed abbreviated principles are in comments (like this one) -->

<!-- 1: Study planning -->
1. **[Study planning](/about/principles/planning/)**
    <!-- 1a: Implement good science -->
    1. Implement good science basics ([power analysis, statistical consults, etc.](https://www.repronim.org/module-stats/)).
    <!-- 1b: Use pre-existing data -->
    2. Use pre-existing data for planning and/or analysis.
    <!-- 1c: Create a DSMP -->
    3. Create an [NIH-compliant data management and sharing plan](https://sharing.nih.gov/data-management-and-sharing-policy/planning-and-budgeting-for-data-management-and-sharing/writing-a-data-management-and-sharing-plan#after).
    <!-- 1d: Adopt open consent -->
    4. Adopt [open consent](https://open-brain-consent.readthedocs.io/en/stable/) to allow broad sharing of data.
    <!-- 1e: Pre-register your study -->
    5. [Pre-register](https://www.cos.io/initiatives/prereg) your study.

<!-- 2: Data and metadata management -->
2.  **[Data and metadata management](/about/principles/data_management/)**
    <!-- 2a: Use standard data formats -->
    1. Use standard data formats and extend them to meet your needs.
    <!-- 2b: Use data version control -->
    2. Use version control from start to finish.
    <!-- 2c: Annotate data -->
    3. Annotate data using standard, reproducible procedures.

<!-- 3: Software management -->
3.  **[Software management](/about/principles/software_management/)**
    <!-- 3a: Use released open source software -->
    1. Use released versions of open source software.
    <!-- 3b: Use software version control -->
    2. Use version control from start to finish.
    <!-- 3c: Automate software installation -->
    3. Automate the installation of your code and its dependencies.
    <!-- 3d: Automate data analysis execution -->
    4. Automate the execution of your data analysis.
    <!-- 3e: Annotate code -->
    5. Annotate your code and workflows using standard, reproducible procedures.
    <!-- 3f: Use containers -->
    6. Use containers where reasonable.

<!-- 4: Publishing everything -->
4.  **[Publishing everything](/about/principles/publish_everything/)** (publishing re-executable publications)
    <!-- 4a: Share research plans -->
    1. Share plans (pre-registration).
    <!-- 4b: Share software -->
    2. Share software.
    <!-- 4c: Share data -->
    3. Share data.
    <!-- 4d: Make all research objects FAIR -->
    4. Make all research objects FAIR.

## ReproNim's four core actions

As indicated by the blue highlights in the figure below, four core actions are key to implementing the above principles.

1. **Use of standards**

    Using standard data formats and extending them to meet specific research needs is important for data and metadata management (Principle 2) in reproducible neuroimaging.

2. **Annotation and provenance**

   Annotating data using standard, reproducible procedures ensures clarity and transparency in data management (Principle 2). _Provenance_ refers to the origin and history of data and processes, enabling researchers to track how data was generated, modified, and analyzed (Principles 2, 3, and 4). This is essential for understanding the context of data and ensuring reproducibility.

3. **Implementation of version control**

   Version control is crucial for both data and software management. It allows researchers to track changes over time, revert to previous versions if necessary, and collaborate effectively.

   For data, version control helps manage different versions of datasets and track modifications made during processing and analysis (Principle 2).

   For software, version control helps track code changes, manage different versions of analysis scripts, and ensure that the correct version of the code is used for each analysis (Principle 3).

   And even publications can be versioned (Principle 4).

4. **Use of containers**

   Containers provide a portable and self-contained environment for running software, ensuring that the analysis can be executed consistently across different computing environments (Principle 3). Containers encapsulate all of the software dependencies needed to run an analysis, making it easier to share software (Principle 4) and reproduce results.

![A diagram showing how ReproNim's principles and core actions work together to reproducible neuroimaging.](/images/principles-of-neuroimaging.jpg)
