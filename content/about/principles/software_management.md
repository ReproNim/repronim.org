---
linkTitle: "Software management"
title: "ReproNim Principle 3: Software management"
type: docs
weight: 100
---

Software management is crucial for reproducibility in neuroimaging because it ensures that complex analysis pipelines can be precisely replicated across different research environments.
Neuroimaging studies typically involve multiple processing steps—from image acquisition to statistical analysis—each dependent on specific software versions, parameters, and dependencies.
Without rigorous software management through version control systems, containerization (e.g., Docker), and package managers, even subtle differences in software can lead to significantly different results even when using identical raw data ([Kennedy et al., 2019](https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2019.00001/full)).
This "hidden variance" undermines scientific validity and hinders progress.
Properly defined software environments also facilitate knowledge transfer between researchers, enable independent verification of findings, and support consistent analysis methods; all essential for neuroimaging to function as a robust scientific discipline.

**3a. Use released versions of open source software**

Building reproducible pipelines requires that the code itself is stable and reliable.
Released versions generally:
  * Have undergone **systematic testing and validation**, making them more stable and reliable than development branches.
    In neuroimaging, where analysis errors can lead to incorrect scientific conclusions, this stability is essential.
  * Have specific version numbers that can be precisely **cited in methods sections**, enabling other researchers to replicate your exact analysis environment.
    Unversioned development code means your analysis may be more difficult to reproduce.
  * Include **detailed release notes** documenting changes, known issues, and compatibility information.
    This documentation helps researchers understand potential impacts on their analysis pipelines and interpret results appropriately.
  * Define **software dependency versions** more clearly, reducing the likelihood of incompatibility issues that can cause processing failures or silently alter results.
  * Supports the **sustainability of open-source projects** by following their intended usage patterns and allowing developers to maintain organized development cycles with clear boundaries between experimental and production-ready features.

**3b. Use version control from start to finish**

Version control creates a transparent history of all code changes, allowing researchers to trace exactly when and why modifications were made.
This is particularly valuable when troubleshooting unexpected results or when revisiting analyses months or years later.
Version control also:

  * Enables **precise replication of analyses** at any point in the project timeline.
    If a reviewer questions a specific analysis step, you can recover the exact code state used to generate those results.
  * Facilitates **collaboration among team members** by providing structured ways to merge contributions while maintaining code integrity.
    Multiple researchers can work simultaneously without risking unintentional overwriting of each other's work.
  * Serves as an **automatic backup system**, protecting against data loss from hardware failures or human error.
    Every committed version remains recoverable, creating a safety net for the entire analytical process.
  * Document the **evolution of your analytical thinking**, preserving the scientific narrative of how analyses were refined in response to data characteristics, literature findings, or peer feedback.
  * Promotes open science by making it easier to **share complete analysis histories**, enhancing transparency and trustworthiness of neuroimaging research.

***Some things you can do***:
  * Tutorial:  [Version control systems](https://www.repronim.org/module-reproducible-basics/02-vcs/)
  * Tutorial: [Basic software versioning using Git](/resources/tutorials/git/)
  * Version control your containers and execution, too: [DataLad Tutorial](/resources/tutorials/repronim-containers/)
  * Version control your scripts
  * Version control your analysis plan

**3c. Automate the installation of your code and its dependencies**

Automating the installation of code and dependencies means creating standardized, programmatic methods that can set up the complete software environment required for your analysis without manual intervention.
Benefits:

   * Eliminates the "works on my machine" problem by ensuring that all researchers can **set up identical computational environments**.
     Manual installation inevitably introduces human errors and undocumented steps that undermine reproducibility.
   * Captures the **complete dependency graph** including specific versions of libraries, frameworks, and system components.
     Neuroimaging analysis often relies on complex interdependent software stacks where slight version differences can significantly alter results.
   * Preserves **institutional knowledge** about the computational environment.
     Automated installation scripts serve as executable documentation of the exact environment required.
   * Makes **validation by other researchers** practical and efficient.
     Reviewers or collaborators can quickly establish the required environment without extensive troubleshooting or correspondence with the original authors.
   * **Reduces the expertise barrier** for reproducing research.
     Junior researchers or scientists from adjacent fields can successfully run analyses without deep knowledge of the underlying computational infrastructure.
   * Ensures **consistent environments** across different computing contexts—from local workstations to high-performance clusters to cloud computing platforms—maintaining result consistency regardless of where the analysis runs.
   * **Future-proofs research** against software evolution by explicitly codifying dependencies that might change over time.

***Some things you can do:***
  * Package your script
  * Tutorial:  [Package managers and distributions](https://www.repronim.org/module-reproducible-basics/03-packages/)

**3d. Automate the execution of your data analysis**

Automating the execution of data analysis in neuroimaging means creating scripts, workflows, or pipelines that can run your entire analysis from raw data to final results without manual intervention.
It is essential for computational reproducibility across different researchers, within and across labs, as it explicitly codifies all the transformations from raw data to published results in a way that can be shared and verified.
Other benefits:
  * Creates a **complete, executable record** of your analysis pipeline, documenting not just what was done but exactly how it was done.
    This executable documentation is more precise and reliable than written descriptions that might omit crucial details.
  * Improves **standardized data handling** across all subjects and sessions, discouraging ad-hoc adjustments that can introduce bias or inconsistency.
    This is particularly important in neuroimaging where researchers may process hundreds of scan sessions.
  * Encourages **systematic validation** through unit tests and integration tests, increasing confidence in the correctness of the analysis and allowing quick identification of errors when they occur.
  * Makes it possible to **rerun analyses** efficiently when source data changes or bugs are discovered.

***Some things you can do***:
  * Develop **executable scripts** that handle each step of your analysis pipeline, from data preprocessing to statistical modeling and visualization.
  * Implement **parameter and configuration files** that separate analytical settings from execution code, making your analysis reusable and transparent.
  * Include **input validation** in your pipeline to ensure data quality and format consistency before processing begins.
  * Establish **error handling protocols** that respond appropriately to problems rather than silently continuing with potentially compromised data.
  * Use **master scripts or workflow managers** that coordinate the execution sequence, ensuring steps occur in the correct order with proper data handoffs between stages.
    Some examples include [Nipype](https://nipype.readthedocs.io/en/latest/), [BIDS Apps](https://bids-apps.neuroimaging.io/), [Snakemake](https://snakemake.github.io/), and [NextFlow](https://training.nextflow.io/latest/) that are designed specifically for complex scientific pipelines.
  * Create **reproducible execution environments** through containers or virtual machines that ensure consistent behavior across computing systems (see principle 3f).

**3e. Annotate your code and workflows using standard, reproducible procedures**

Annotating code and workflows using standard, reproducible procedures transforms implicit knowledge into explicit documentation, ensuring that the rationale behind analytical choices is preserved.
Without proper annotation, critical decisions may appear arbitrary to other researchers or even to your future self.
Standardized annotations create a common language across the research community, enabling easier collaboration and review.
When everyone follows similar documentation patterns, it's much simpler to understand unfamiliar code.
Annotations also serve as a form of scientific provenance, connecting analysis steps to specific hypotheses, literature references, or methodological requirements.
This creates an auditable trail for scientific decisions and facilitates troubleshooting and debugging.
They lower the barrier to entry for new researchers by providing contextual information that might otherwise require extensive domain expertise or direct training from the original authors.

**3f. Use containers where reasonable**

A container is a lightweight, standalone, executable software package that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings.
Containers encapsulate the entire computational environment necessary for analysis in a portable format that can run consistently across different computing platforms.
They simplify deployment across diverse computing environments (from personal laptops to high-performance clusters to cloud computing platforms) without requiring complex installation procedures for each host system.
Containers are vital for reproducible neuroimaging because they:
  * **Create complete isolation from the host system**, ensuring that neuroimaging analyses run in identical environments regardless of the underlying hardware or operating system.
    This eliminates the "it works on my machine" problem that often undermines reproducibility.
  * **Capture all dependencies** with their exact versions, including specialized neuroimaging software (like FSL, AFNI, or FreeSurfer), ensuring that analyses performed years apart use identical computational tools.
    Each container maintains its own isolated dependency tree, providing a solution for software conflicts that often arise in complex neuroimaging pipelines.
  * Are immutable and **versioned**, allowing researchers to document which environment was used for specific analyses and ensuring that others can access exactly that environment.

**ReproNim resources**:
  * Tutorial: [Create and maintain reproducible computational environments](https://www.repronim.org/module-dataprocessing/04-containers/)
  * [Neurodocker](/resources/tools/neurodocker/): a command line program for generating Dockerfiles and Singularity recipes for neuroimaging software
  * Tutorial:  [Advanced containerization using DataLad](/resources/tutorials/repronim-containers/).
    Shows how to use datalad run with repronim-containers to preserve the provenance of exactly what software versions were used and how, leaving a detailed trail for future work.

**Other resources**:
  * [Docker](https://www.docker.com/):  popular platform for building, deploying, and managing applications within standardized units called "containers"
  * [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html): popular platform for building, deploying, and managing applications within standardized units called "containers"
  * [BIDS Apps](https://bids-apps.neuroimaging.io/): leverages containers to standardize neuroimaging workflows across the research community.
