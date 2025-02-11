---
title: Getting Started with ReproNim
weight: 2
---

ReproNim's philosophy is to incorporate reproducible practices into the typical neuroimaging workflow.  These practices ensure more robust, well documented studies at the end for you, your colleagues, and your peers.

ReproNim offers best practices, tools, and training to implement reproducible neuroimaging in your lab.

Our website provides a number of resources:

* An introduction to reproducible neuroimaging: We provide an [overview of reproducible neuroimaging](/about/why/), including exactly what we mean by the term and why it's important.  We follow it by showing [how to apply reproducible neuroimaging in practice](/about/in-practice/) and introduce principles of reproducible neuroimaging and actions for their application.
* An overview of the [ReproNim approach](/about/repronim-approach/), describing how ReproNim supports reproducible neuroimaging.
* An overview of how ReproNim applies to you: Meet our [exemplary user personas](/resources/getting-started/#user-personas) below and read about the issues they face in running neuroimaging studies.  Then browse our [tools](/resources/tools/) to find one that serves your needs and follow one our our [tutorials](/resources/tutorials/), showing how to use the tools to support reproducible neuroimaging.
* Training resources: We provide an [online training course](https://www.repronim.org/teach.html) on a range of basic and more advanced topics related to reproducible neuroimaging.  And learn about the [ReproNim/INCF Fellowship](/fellowship/), our innovative and successful train-the-trainer program.

## User personas

To introduce you to ReproNim, we have created a set of exemplary personas that cover some typical interests and needs and have given each a face (through the magic of AI) and a set of skills and interests. We then produced a set of basic use cases that showcase how adopting the principles of neuroimaging and ReproNim tools can help them in their goals.

Who would you like to hear from?

<link rel="stylesheet" href="/css/personas.css">
<div class="persona">
    <a href="#Early/mid career researcher">
        <img src="/images/sarah.jpg" alt="Sarah">
    </a>
    <p>
        Hi, I'm Sarah.  I'm an early- to mid-career researcher.  I'm  interested in applying best practices to my day-to-day research workflow.  <a href="#sarah">Read more.</a>
    </p>
</div>

<div class="persona">
    <a href="#Software engineer">
        <img src="/images/richard.jpg" alt="Richard">
    </a>
    <p>
        Hi, I'm Richard.  I'm a research software engineer.  I want to incorporate more standards into the technical operations of my lab and learn more about how to effectively share workflows with my clients.  <a href="#richard">Read more.</a>
    </p>
</div>

<div class="persona">
    <a href="#Computational neuroscientist/teacher">
        <img src="/images/john.jpg" alt="John">
    </a>
    <p>
        Hi, I'm John.  I'm a university-based computational neuroscientist and teacher.  I would like to see what resources are available for my teaching about rigor and reproducibility. <a href="#john">Read more.</a>
    </p>
</div>

<div class="persona">
    <a href="#Multi-center project director">
        <img src="/images/evelyn.jpg" alt="Evelyn">
    </a>
    <p>
      Hi, I'm Evelyn.  I'm the director of a multi-center distributed project.  My interest is in harmonizing the research being performed at several sites. <a href="#evelyn">Read more.</a>
    </p>
</div>

### Sarah

<img src="/images/sarah.jpg" alt="Sarah" style="width: 250px; height: auto;">

I'm Sarah, an early- to mid-career researcher.  I'm interested in applying best practices to my day-to-day research workflow.

I'm fluent in modern technologies and comfortable both at the bench and behind a computer, and I spend my days engaged in the hands-on aspects of studies. As I build my career, I want to keep up-to-date with the latest trends and tools, but I don't dwell on technology for its own sake. Efficiency is important, but not if it sacrifices rigor.

I would like support for making my workflow development more efficient: How do I go from my "garden path" workflow development, lock into a final workflow, and then efficiently apply this workflow to my complete dataset? My workflow might change, so I'd like to efficiently update and re-apply the new workflow. I've heard versioning will be important for this, but I'm not handy with these technologies. Publishing my data would be nice for some additional impact and for complying with the NIH data sharing mandate.

#### How ReproNim can help

ReproNim can help Sarah learn more about data and software management and other best practices for reproducible neuroimaging as well as introduce her to tools and practices for versioning workflows. When data and software are managed throughout the neuroimaging workflow, effectively and efficiently publishing data and the pipelines that produced it is much easier to do..

Tutorials that might be interesting to Sarah include:

* For study planning, [Creating a Data Management and Sharing Plan](/resources/tutorials/data-management-and-sharing/).
* For data management, [Converting DICOM to BIDS](/resources/tutorials/dicom-to-bids/) and [Creating a Data Dictionary](/resources/tutorials/data-dictionary/).
* For software management, [Basic Software Versioning Using Git](/resources/tutorials/git/).

### Richard

<img src="/images/richard.jpg" alt="Richard" style="width: 250px; height: auto;">

Hi, I'm Richard, a research software engineer.  I want to incorporate more standards into the technical operations of my lab and also learn more about how to effectively share workflows with my clients.

I'm responsible for developing the software in support of my lab's research. I'm given high-level requirements but I then have freedom to decide how to implement solutions. I don't code exclusively and spend time researching and planning my work since I have to balance software engineering best practices with the limited resources available for research software engineering.

I would like to generate software products that incorporate community standards for data ingestion and export. I'm aware of BIDS for standard data representation, but I need to learn about output standards like BIDS derivatives and standardized output descriptions like NIDM.  I have heard that containerizing software can make it easier to deliver it to my local clients (and for them to share with others who want to reproduce their work) and easier to support compared to a bare metal software solution.

#### How ReproNim can help

ReproNim can help Richard learn how standards such as BIDS and NIDM can help with better data management.  ReproNim can provide Richard with demos and use cases to show why containerization is worth the effort.

Tutorials that might be interesting to Richard include:

* For data management, [Creating a Data Dictionary](/resources/tutorials/data-dictionary/).
* For software management, [Advanced Containerization Using DataLad](/resources/tutorials/repronim-containers/).

### John

<img src="/images/john.jpg" alt="John" style="width: 250px; height: auto;">

Hi, I'm John.  I'm a university-based computational neuroscientist and teacher.  I would like to see what resources are available for teaching about rigor and reproducibility.

I have both lab and teaching responsibilities. I'd like my lab members to understand and utilize principles of re-executable annotated workflows.  I also wonder whether whether the ReproNim fellowship program might be appropriate for someone in my lab (perhaps as a way to train others in the lab thereafter). As a teacher, I'm interested in broadly educating my students on reproducibility and exposing them to key concepts, tools, and educational materials.

I'm interested in whether ReproNim provides up-to-date teaching materials that I can use in my own teaching.  I'm also interested in resources that might help my students and/or lab.

#### How ReproNim can help

Educational resources that might be interesting to John and his students:

This site's [Why Reproducible Neuroimaging](/about/why/) and [Reproducible Neuroimaging in Practice](/about/in-practice/) provide a high-level overview of reproducible neuroimaging and the issues around it.

The [tutorials](/resources/tutorials/) provided here give opportunities for hands on experience in a number of areas.

For more in depth training, ReproNim has created a [modular online course](/resources/training/) that covers basic and advanced topics in reproducible neuroimaging.  Each module contains tutorials and hands on exercises.

John might also be interested in the [ReproNim/INCF Fellows Program](/fellowship/), a one year train-the-trainer program in reproducible neuroimaging.

### Evelyn

<img src="/images/evelyn.jpg" alt="Evelyn" style="width: 250px; height: auto;">

Hi, I'm Evelyn.  I'm the director of a multi-center distributed project.  My interest is in harmonizing the research being performed at several sites.

I've been a researcher my whole career, and now I direct a multi-center distributed project. My responsibilities include oversight for integrated data sharing and cross-site analyses within the project, as well as ultimately making all data publicly accessible and reusable. I'm interested in options for facilitating and streamlining data acquisition, use, and reuse for varied purposes, both within and beyond the bounds of the project itself. I have the authority and responsibility to make recommendations for infrastructure that would serve a multidisciplinary multi-site project well.

I think ReproNim might address many of my priorities, but I'd really like an end-to-end platform for data acquisition, data management, and dissemination. I need to distribute common analysis methods to all of the project's sites. I'd like it to be easy for the sites to give me results from these analyses and for these results to be easy to aggregate and harmonize. The sites are also collecting their own subjects, so I need common demographic, clinical, and behavioral data to be collected and shared in a way that is also easy to aggregate and harmonize.

#### How ReproNim can help

ReproNim is not an end-to-end platform but does have several tools that can apply to Evelyn's current data workflow to make it easy to share FAIR data and analyses across multiple sites.

Tutorials that might be of interest to Evelyn include:

* For data management, [Planning a Distributed Project Using ReproSchema](/resources/tutorials/reproschema/), [Creating a Data Dictionary](/resources/tutorials/data-dictionary/), and [Searching Across Studies Using ReproPond and ReproLake](/resources/tutorials/pond-lake/).
* For software management, [Streamlining Neuroimaging Processing with Nipoppy](/resources/tutorials/nipoppy/).
