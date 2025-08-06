---
linkTitle: "Software management"
title: "ReproNim Principle 3: Software management"
type: docs
weight: 80
---

Software management is crucial for reproducibility in neuroimaging because it ensures that complex analysis pipelines can be precisely replicated across different research environments. Neuroimaging studies typically involve multiple processing steps—from image acquisition to statistical analysis—each dependent on specific software versions, parameters, and dependencies. Without rigorous software management through version control systems, containerization (e.g., Docker), and package managers, subtle differences in software implementations can lead to significantly different results despite using identical raw data ([Kennedy et al., 2019](https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2019.00001/full)). This "hidden variance" undermines scientific validity and hinders progress in the field. Properly documented software environments also facilitate knowledge transfer between researchers, including lab members and collaborators, enable independent verification of findings, and support longitudinal studies where consistent analysis methods must be maintained over extended periods—all essential components for establishing neuroimaging as a robust scientific discipline.

1. **Use released versions of open source software**  
   Building reproducible pipelines requires that the code itself is stable and reliable.  So although those beta versions in GitHub might be tempting, it is better to utilize stable releases for any applications.  Released versions generally:  
    * Have undergone **systematic testing and validation**, making them more stable and reliable than development branches. In neuroimaging, where analysis errors can lead to incorrect scientific conclusions, this stability is essential.  
    * Have specific version numbers that can be precisely **cited in methods sections**, enabling other researchers to replicate your exact analysis environment. Using unversioned development code means your analysis might be running on an ephemeral state of the software that others cannot reproduce.  
    * Include **detailed release notes** documenting changes, known issues, and compatibility information. This documentation helps researchers understand potential impacts on their analysis pipelines and interpret results appropriately.
    * Define **software dependencies** more clearly defined for released versions, reducing the likelihood of incompatibility issues that can silently alter results or cause processing failures.  
    * Supports the **sustainability of open-source projects** by following their intended usage patterns and allowing developers to maintain organized development cycles with clear boundaries between experimental and production-ready features.  
    
2. **Use version control from start to finish**  
   Version control creates a transparent history of all analysis code changes, allowing researchers to trace exactly when and why modifications were made. This is particularly valuable when troubleshooting unexpected results or when revisiting analyses months or years later.  Version control also:

   * Enables **precise replication of analyses** at any point in the project timeline. If a reviewer questions a specific analysis step, you can recover the exact code state used to generate those results, even if you've since modified your approach.  
   * Facilitates **collaboration among team members** by providing structured ways to merge contributions while maintaining code integrity. Multiple researchers can work simultaneously without risking unintentional overwriting of each other's work.  
   * Serves as an **automatic backup system**, protecting against data loss from hardware failures or human error. Every committed version remains recoverable, creating a safety net for the entire analytical process.  
   * Document the **evolution of your analytical thinking**, preserving the scientific narrative of how analyses were refined in response to data characteristics, literature findings, or peer feedback.  
   * Promotes open science by making it easier to **share complete analysis histories** with collaborators or the broader scientific community, enhancing transparency and trustworthiness of neuroimaging research.

      * ***Some things you can do***:  
        * Tutorial:  [Version control systems](https://www.repronim.org/module-reproducible-basics/02-vcs/)  
        * Tutorial: [Basic software versioning using Git](https://repronim.netlify.app/resources/tutorials/git/)  
        * Version control your containers and execution, too: DataLad Tutorial  
        * Version control your scripts   
        * Version control your analysis plan    
        
3. **Automate the installation of your code and its dependencies**  
   Automating the installation of code and dependencies means creating standardized, programmatic methods that can set up the complete software environment required for your analysis without manual intervention.  Benefits:  

    * Eliminates the "works on my machine" problem by ensuring that all researchers can **set up identical computational environments** regardless of their starting configuration. Manual installation inevitably introduces human errors and undocumented steps that undermine reproducibility.  
    * Captures the **complete dependency graph** including specific versions of libraries, frameworks, and system components. Neuroimaging analysis often relies on complex interdependent software stacks where slight version differences can significantly alter results.  
    * Preserves **institutional knowledge** about the computational environment. When researchers leave a project or when revisiting analyses years later, automated installation scripts serve as executable documentation of the exact environment required.  
    * Makes **validation by other researchers** practical and efficient. Reviewers or collaborators can quickly establish the required environment without extensive troubleshooting or correspondence with the original authors.  
    * **Reduces the expertise barrier** for reproducing research. Junior researchers or scientists from adjacent fields can successfully run analyses without deep knowledge of the underlying computational infrastructure.  
    * Ensures **consistent environments** across different computing contexts—from local workstations to high-performance clusters to cloud computing platforms—maintaining result consistency regardless of where the analysis runs.  
    * **Future-proofs research** against software evolution by explicitly codifying dependencies that might otherwise become unavailable or incompatible as operating systems and package repositories change over time.

       * ***Some things you can do:***
           * Package your script  
           * Tutorial:  [Package managers and distributions](https://www.repronim.org/module-reproducible-basics/03-packages/)  
    
4. **Automate the execution of your data analysis**  
   Automating the execution of data analysis in neuroimaging means creating scripts, workflows, or pipelines that can run your entire analysis from raw data to final results without manual intervention.  It is essential for computational reproducibility across different researchers, within and across labs, as it explicitly codifies all the transformations from raw data to published results in a way that can be shared and verified. Other benefits:  
    * Creates a **complete, executable record** of your analysis pipeline, documenting not just what was done but exactly how it was done. This executable documentation is more precise and reliable than written descriptions that might omit crucial details.  
    * Enforces **standardized data handling** across all subjects and sessions, preventing ad-hoc adjustments that can introduce bias or inconsistency into results. This is particularly important in neuroimaging where researchers may process hundreds of scan sessions.  
    * Enables **systematic validation** through unit tests and integration tests, increasing confidence in the correctness of the analysis and allowing quick identification of errors when they occur.  
    * Facilitates **parameter sweeps and sensitivity analyses** by making it easy to run the same pipeline with different settings, helping researchers understand how analytical choices affect outcomes.  
    * Makes it possible to **rerun analyses** efficiently when new data arrives or when bugs are discovered, ensuring that all data is processed with the corrected methods.

      * ***Some things you can do***:   
          * Develop **executable scripts** that handle each step of your analysis pipeline, from data preprocessing to statistical modeling and visualization.  
          * Create **master scripts or workflow managers** that coordinate the execution sequence, ensuring steps occur in the correct order with proper data handoffs between stages.  
          * Implement **parameter and configuration files** that separate analytical settings from execution code, making your analysis both customizable and transparent.  
          * Include input **validation** to ensure data quality and format consistency before processing begins.  
          * Establish **error handling protocols** that respond appropriately to problems rather than silently continuing with potentially compromised data.  
          * Use **workflow management tools** like [Nipype](https://nipype.readthedocs.io/en/latest/), [BIDS Apps](https://bids-apps.neuroimaging.io/), [Snakemake](https://snakemake.github.io/), or [NextFlow](https://training.nextflow.io/latest/) that are designed specifically for complex scientific pipelines.  
          * Create **reproducible execution environments** through containers or virtual machines that ensure consistent behavior across computing systems (see principle 3f).  
      
5. **Annotate your code and workflows using standard, reproducible procedures**  
   Annotating code and workflows using standard, reproducible procedures transforms implicit knowledge into explicit documentation, ensuring that the rationale behind analytical choices is preserved. Without proper annotation, critical decisions may appear arbitrary to other researchers or even to your future self. Standardized annotations create a common language across the research community, enabling easier collaboration and review. When everyone follows similar documentation patterns, it's much simpler to understand unfamiliar code.  Annotations also serve as a form of scientific provenance, connecting analysis steps to specific hypotheses, literature references, or methodological requirements. This creates an auditable trail for scientific decisions and facilitates troubleshooting and debugging. They lower the barrier to entry for new researchers by providing contextual information that might otherwise require extensive domain expertise or direct training from the original authors.   
    * ***ReproNim resources***:  
      * ReproNim provides [annotation wrapper software](https://repronim.org/resources/tools/#additional-associated-tools) for many common tools (such as FreeSurfer, SPM, FSL, ANTS, etc.)  
      * If you are developing your own software (or using software that does not have an annotation wrapper) ReproNim provides support for building such wrappers for your applications (and to share with others using your applications\!). 


6. **Use containers where reasonable**  
   A container is a lightweight, standalone, executable software package that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings. Containers encapsulate the entire computational environment necessary for analysis in a portable format that can run consistently across different computing platforms. They simplify deployment across diverse computing environments \- from personal laptops to high-performance clusters to cloud computing platforms \- without requiring complex installation procedures at each site. Containers are vital for reproducible neuroimaging because they:  
    * **Create complete isolation from the host system**, ensuring that neuroimaging analyses run in identical environments regardless of the underlying hardware or operating system. This eliminates the "it works on my machine" problem that often undermines reproducibility.   
    * **Capture all dependencies** with their exact versions, including specialized neuroimaging software (like FSL, AFNI, or FreeSurfer), ensuring that analyses performed years apart use identical computational tools. Each container maintains its own isolated dependency tree, providing a solution for software conflicts that often arise in complex neuroimaging pipelines. .  
    * Are immutable and **can be versioned**, allowing researchers to precisely document which environment was used for specific analyses and ensuring that others can access exactly that environment.  
    
        * **ReproNim resources**:  
          * Tutorial: [Create and maintain reproducible computational environments](https://www.repronim.org/module-dataprocessing/04-containers/)  
          * [Neurodocker](https://repronim.netlify.app/resources/tools/neurodocker/): a command line program for generating Dockerfiles and Singularity recipes for neuroimaging software  
          * Tutorial:  [Advanced containerization using DataLad](https://repronim.netlify.app/resources/tutorials/repronim-containers/).  Shows how to use datalad run with repronim-containers to preserve the provenance of exactly what software versions were used and how, leaving a detailed trail for future work.

    

        * **Other resources**:  
          * [Docker](https://www.docker.com/):  popular platform for building, deploying, and managing applications within standardized units called "containers  
          * [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/introduction.html): popular platform for building, deploying, and managing applications within standardized units called "containers  
          * [BIDS Apps](https://bids-apps.neuroimaging.io/): leverages containers to standardize neuroimaging workflows across the research community.

