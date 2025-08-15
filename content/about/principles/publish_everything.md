---
linkTitle: "Publish everything"
title: "ReproNim Principle 4: Publishing everything"
type: docs
weight: 80
---

The scientific publication is a main outcome of our research endeavor. Scientific publications, by definition, are supposed to convey the necessary information for someone to replicate the observation. We have learned over the past decades that words like “...acquire a structural MRI scan…” and “...use software package X…” do not sufficiently capture the necessary information for someone to replicate the observation. In order to convey a neuroimaging finding in a replicable fashion, one needs to include *precise and complete* information about the data, software, workflow, and derived results that comprise the publication ([Kennedy et al., 2019](https://pubmed.ncbi.nlm.nih.gov/30792636/)). Fortunately, there are methods for sharing each of these types of information in the context of a publication, rendering the publication more replicable.  And if you implement the practices recommended in principles 1-3, “publishing everything” is straightforward.

1. **Share plans (pre-registration)**

See write up for [principle 1.5](/about/principles/planning/)

2. **Share software**
   Ideally, the **software being used was containerized** so that your complete software environment can be shared. This container can be shared using DockerHub (Principle 3\.
    * We assume that the **processing script (**i.e. the set of commands that uses the above container) was managed using Git, and can be shared via  GitHub. As GitHub repositories can evolve from what was the version actually used in a publication, the state of the GitHub repository that matches that used in the publication can be snapshotted and archived using Zenodo, which will also generate a DOI. Instructions can be found [here](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).
    * The **results of running the workflow** on the data can be added to the BIDS/derivatives representation of the dataset (a discussion of BIDS/Derivatives can be found [here](https://bids-specification.readthedocs.io/en/stable/derivatives/introduction.html)). This can be shared (or version updated if the original data was already shared) to OpenNeuro.
    * If separate **statistical analysis** was performed, this can be managed using Git, and can be shared at GitHub, and archived using Zenodo, as indicated above.

3. **Share data**
   Upload your data to a trusted repository, ideally one specialized for sharing neuroimaging data, e.g., [Open Neuro](https://openneuro.org/).  The National Library of Medicine maintains a [searchable list of data repositories](https://www.nlm.nih.gov/NIHbmic/domain_specific_repositories.html) for biomedical data.

4. **Make all research objects FAIR**
   The publication should include FAIR pointers, i.e., a reference to the DOI or equivalent identifier,  to each of the critical elements that went into the observations and conclusions that it reaches, facilitating the replication and generalizability of its findings. These pointers should be included in the methods section and/or the data and tool availability section and should resolve to the exact version of the data or software you are using.
    * **Datasets** submitted to a trusted repository will receive a DOI or equivalent identifier.
    * Detailed **protocols** can be published in [Protocols.io](http://Protocols.io) to receive a DOI
    * Additional **supplementary data** or materials necessary to understand and replicate the findings of a study can be deposited in generalist repositories like [Zenodo](https://zenodo.org/) or [Figshare](http://figshare.org/) to receive a DOI.
    * For **software maintained in GitHub**, you can create a snapshot of the repository and a DOI in Zenodo using [automated routines](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).  Zenodo archives your repository and issues a new DOI each time you create a new GitHub [release](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases). Follow the steps at [Managing releases in a repository](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) to create a new one.
