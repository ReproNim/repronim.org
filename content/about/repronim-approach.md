---
title: The ReproNim Approach
type: docs
weight: 90
---
## How does ReproNim help support reproducible neuroimaging?

Now that we have defined the [4 principles and 4 actions](/about/in-practice/) that support reproducible neuroimaging, we describe how ReproNim helps researchers put these into action. 

ReproNim's goal is to improve the reproducibility of neuroimaging science while making the process of capturing and precisely describing all essential study details both easier and more efficient.
ReproNim focuses on practices and tools that support researchers and software engineers in integrating reproducible principles and actions into their own neuroimaging workflow.

![A diagram showing the flow of data through an imaging study.](/images/reprosystem.png)

As outlined this figure, ReproNim's system takes the full cycle of neuroimaging data acquisition, analyses, and publication into account. Each of these steps requires planning, data/metadata management and software management so that in the end you can publish everything! ([the 4 principles](/about/in-practice/#repronims-principles-of-reproducible-neuroimaging)).  ReproNim provides the tools and best practices for using standards, annotating data and workflows and recording provenance, implementing version control and using containers ([the 4 actions](/about/in-practice/#repronims-four-core-actions)) to put these principles into practice.

The Reprosystem explicitly includes both data entering into an analysis (data of various types including scanner acquisitions, data converted to BIDS, behavioral data, and outputs of prior analyses), and the metadata and provenance of the analysis (software versions and computer operating system versions used, processing scripts, subject demographics, results descriptions, etc.).

The metadata maintains a link to its associated data, permitting flexibility in how each of these information sources can be used.
To the familiar components of data and analysis environments we also add a means to store and retrieve machine-readable descriptions of metadata associated with the tools in both a local/private store (which we refer to as a _ReproPond_) and a shared/public repository (_ReproLake_).

To get started, see:

* [Getting started with ReproNim](/resources/getting-started/)
* [ReproNim's core tools](/resources/tools/)
* [ReproNim's tutorials](/resources/tutorials/)
