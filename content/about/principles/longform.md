# ReproNIM Principle 1: Study planning

Study planning represents a foundational step in ensuring reproducible neuroimaging research.  Many problems that lead to reproducibility issues can be avoided by proper planning 

1. **Implement good science basics, e.g, power analysis, statistical consults**  
   If your study is underpowered or your study design is flawed, you will have trouble publishing your work and, more to the point, your work will likely not be reproducible ([Scuzs and Ioannidis, 2020](https://www.sciencedirect.com/science/article/pii/S1053811920306509#bib24)).   
   * ***ReproNim resources*****:**   
     * [Repronim training module in statistics for neuroimaging](https://www.repronim.org/module-stats/):  covers all aspects of statistics for neuroimaging, including sampling, power analysis and more

   * ***Other resources:***    
     * NINDS-funded [Community for Rigor (C4R)](https://c4r.io/): tools and resources for improving rigor and reproducibility, from basics to advanced

     * Statistical consult: Most universities have statisticians available for consultation. The most important time to consult with a statistician is at the conceptualization phase, ***not*** after the data are collected.

2. **Use pre-existing data for planning and/or analysis**  
   Leveraging pre-existing data, whether your own or data available from public repositories,  can help validate methodological approaches before collecting new data and potentially increase your sample size

   * ***ReproNim resources*****:**   
     ReproNim has tools and approaches to make it easier to find and reuse your own data or publicly available data  
     * [ReproLake](https://repronim.netlify.app/resources/tools/reprolake/): a searchable data store for public neuroimaging data, built on the NIDM and BIDS standards   
     * RepoPond:  A local searchable metadata store for your neuroimaging data, built with the same standards as the ReproLake.  
     * [Neurobage](https://repronim.netlify.app/resources/tools/neurobagel/)l: A system for distributed data sharing and discovery built on common annotations across the workflow  
     * Tutorial: [Sharing and Searching Metadata Using a ReproPond and the ReproLake](https://repronim.netlify.app/resources/tutorials/pond-lake/)

   * ***Other resources:***    
     * OpenNeuro (and other repositories)

3. **Create a data management and sharing plan (DMSP)**  
   A key component of study planning is carefully considering data management needs from the start. By anticipating the volume and types of data that will be generated, researchers can allocate appropriate resources for storage, processing, and sharing. The NIH's requirement for a Data Management and Sharing Plan (DMSP) in all proposals helps formalize this planning process. The DMSP requires researchers to specify crucial details like which data standards will be implemented and where data will ultimately be shared. By addressing these requirements during the planning phase, researchers can integrate data sharing preparations into their workflow from the beginning, rather than treating it as an burdensome afterthought at the study's conclusion.  
     
   * ***ReproNim resources:***  
     * [How ReproNim can help you create an NIH-compliant DMSP](https://repronim.netlify.app/resources/tutorials/data-management-and-sharing/)  
     * [Planning ahead for multi-site data collection using ReproSchema](https://repronim.netlify.app/resources/tutorials/reproschema/)

   * ***Other resources:***  
     * [NIH DMSP website](https://sharing.nih.gov/data-management-and-sharing-policy/planning-and-budgeting-for-data-management-and-sharing/writing-a-data-management-and-sharing-plan#after)  

4. **Adopt open consent to allow broad sharing of data**  
   To ensure that data can be broadly shared, it is important that research participants provide consent for broad public sharing of the data, rather than for narrow purposes.  

   * ***Resources***   
     * The [Open Brain Consent](https://open-brain-consent.readthedocs.io/en/stable/) project provides guidance, tools and templates for incorporating open consent into neuroimaging studies while still providing protections for human subjects through de-identification of data.

5. **Pre-register your study to increase transparency and build trust**  
   Pre-registering a study involves documenting and publishing the research plan, including details about study hypotheses, design and analysis,  before the study begins. Preregistration makes research more transparent and reproducible, helps reduce duplication of research, can improve study design and separates hypothesis-generating (exploratory) from hypothesis-testing (confirmatory) research. Some journals support Registered Reports, a peer reviewed study pre-registration which guarantees the publication of the subsequent results if the study adheres to the protocol, regardless of whether or not the hypothesis was supported.   
* ***Resources***  
  * [Center for Open Science pre-registration site](https://www.cos.io/initiatives/prereg)

  * Lakens, D., Mesquida, C., Rasti, S., & Ditroilo, M. (2024). The benefits of preregistration and Registered Reports. *Evidence-Based Toxicology*, *2*(1). [https://doi.org/10.1080/2833373X.2024.2376046](https://doi.org/10.1080/2833373X.2024.2376046) 

  * Example of publication of a null result after pre-registration:  
    * Kliemann D, Galdi P, Van De Water AL, Egger B, Jarecka D, Adolphs R, Ghosh SS. Resting-State Functional Connectivity of the Amygdala in Autism: A Preregistered Large-Scale Study. Am J Psychiatry. 2024 Dec 1;181(12):1076-1085. [doi: 10.1176/appi.ajp.20230249](https://psychiatryonline.org/doi/10.1176/appi.ajp.20230249). 

