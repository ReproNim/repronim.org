---
title: "Why Reproducible Neuroimaging"
type: docs
date: 2024-10-25T14:41:08-04:00
---

## Why reproducible imaging?

First, let’s ask what is reproducibility?

- Material from What is reproducibility”
- Scientific reproducibility is built on methodological reproducibility
    - Major sources of variability:  N, statistics, tools:  Cover the entire gamut through training and best practices but our tools are the cool thing.

Reproducible research is transparent. Transparency is achieved through being able to know precisely ‘what operations’ were performed on ‘what data’ in a fashion that could potentially be re-executed by:
- You
- Future you
- Your lab
- Your colleagues
- Reviewers
- Other neuroimagers
- Data scientists
- AI

## So what is reproducible imaging?

Reproducible neuroimaging encompasses a comprehensive approach to research practices that prioritizes transparency, rigor, and the ability to share and re-execute neuroimaging data, analyses and results,  ensuring that findings are robust and can be independently validated. (NotebookLM+MM)

Every neuroimager who utilizes neuroimaging in their laboratory or center has the basic components available to acquire, store, process and analyze data and publish their results.

![](/images/data_flow.jpeg)

But how well are the data, code and workflows managed during this process? How easy is it for you to understand and reconstruct what you have done when it comes time to analyze your data or to publish?   Ask yourself these questions:

- How do I plan for my experiments?
    - How many subjects do I need?
    - Given the new NIH mandate, how will I manage and share my data?
    - Did I talk to a statistician?
    - Is there existing data I can use?
- How have I implemented version control across the laboratory?
    - So that you and your lab members know what you did, when and why you changed what you did
    - Poor version control leads to confusion in analysis, publication and re-use.  It greatly increases the resources required to analyze your results
- How does my lab annotate data, code and workflows?
    - So that you can understand what you did and reuse the data more easily, now and in the future
    - Poor annotation is a huge money-sink because unless you use the data right away, you are unlikely to remember the key details needed to analyze and understand the data
- What standards have I implemented in the lab?
    - So that I can access and analyze my data more easily by using tools developed by my lab mates and the wider community;  so that I can share data with my collaborators and use other datasets acquired with the same standards
    - When everyone has their own way of doing things in a lab, it is difficult to reuse others data and code;  standards also enforce certain good behaviors such as metadata capture that make it easier to use your data
- Are my software environments packaged in containers?
    - How easily can I or others replicate my work?
    - If an external service or 3rd party software disappears, is my code broken and my work unverifiable?
    - Containers have a learning curve, but they help preserve the value of your hard-earned results despite the chaos of software churn.
- When it comes time to publish, how easy is it for me that meet data and code sharing requirements of journals and funders?
    - So that you can easily assemble all the data and code that are utilized within a submitted study without having to spend weeks or months trying to remember what you did and where to find it
    - One of the reasons that data sharing mandates are perceived as onerous on the submitter is that data are not well versioned, annotated, standardized and containerized.  Implementing these steps in the laboratory makes it much easier to meet requirements.

## Vignette 1: Has this happened to you?

You submit your study to your favorite highly competitive journal and the review comes back:  
- Your N is too small…  
- This seems more of an exploratory study.  What were your hypotheses?
- Can you re-run this analysis using X?
- You need to make your data and code available

## Get started

ReproNim’s goal is to improve the reproducibility of neuroimaging science, while making the process of capturing and precisely describing all essential/necessary experimental details both easier and more efficient for investigators. Supporting re-executability is a challenging and multifaceted problem. 

[Ready to get started?](/getting-started/index.html)
