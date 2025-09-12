---
title: Annotating FreeSurfer Data
linkTitle: Annotating FreeSurfer Data
type: docs
weight: 5 
---

**[Reproducible neuroimaging principles](/about/principles/#repronims-four-core-principles)**: 2b. Use standard data formats.

**[Actions](/about/principles/#repronims-four-core-actions)**: Standards, Annotation and provenance.

**Standards**: [BIDS](/resources/tools/bids/), [NIDM](/resources/tools/nidm/).

**Tools**: [PyNIDM](/resources/tools/pynidm/index.html), [segstats_jsonld](https://github.com/ReproNim/segstats_jsonld).

## Challenge
[FreeSurfer](https://surfer.nmr.mgh.harvard.edu/) is a software package designed to process, analyze, and visualize magnetic resonance (MR) images of the human brain. FreeSurfer produces cortical and subcortical anatomical maps based on human brain atlases. We want to link the neuroanatomical labels (e.g. stg_thick_l) to concepts (e.g. a label of "Left Superior Temporal Gyrus" and a measurement of thickness). NIDM makes data more meaningful and easier to interpret by both humans and machines by incorporating standardized vocabularies and defining the connections between data elements, leveraging knowledge from community ontologies. Here we annotate the FreeSurfer results for the left cortical map, right cortical map and bilateral subcortical map. In the process we join the FreeSurfer results with the [BIDS/demographic data dictionary](/resources/tutorials/data-dictionary/). 

## Exercise
In these instructions we install a development environment (i.e. conda), install the FreeSurfer annotation tool segstats_jsonld and annotate the FreeSurfer output.

## Before you start
In a typical workflow for annotating a project, the first step is capturing the BIDS information and demographic details shown in Creating a [BIDS Data Dictionary and Adding Semantics](/resources/tutorials/data-dictionary/). During the annotation process we will join FreeSurfer annotations with the BIDS data dictionary. For this tutorial, the initial BIDS data dictionary is saved to /project/nidm.ttl. 

These instructions expect FreeSurfer processing and QC has been completed. An introduction to running FreeSurfer is located at the [FreeSurfer tutorial](https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferBeginnersGuide).

## Step by step guide
Given the FreeSurfer results, we will use the segstats_jsonld program (https://github.com/ReproNim/segstats_jsonld) to create a NeuroImaging Data Model (NIDM) semantically marked up version of the neuroimaging data. 

### Step 1: Create a Conda development environment
Install Conda https://docs.anaconda.com/free/miniconda/miniconda-install/. Then in terminal:

```
conda create -n repro python=3.9
conda activate repro
```

### Step 2: Clone a copy of the repository and install

```
git clone https://github.com/ReproNim/segstats_jsonld.git
cd segstats_jsonld
pip install -e 
```

### Step 3: Annotate FreeSurfer results
Below creates aseg_nidm.ttl (bilateral subcortical map), lh.aparc_nidm.ttl (left cortical parcellation) and rh.aparc_nidm.ttl (right cortical parcellation) for one subject (sub-01) in the listed folder. The nidm.ttl was previously created as per the [BIDS/demographic data dictionary tutorial](/resources/tutorials/data-dictionary/). 

```
segstats2nidm -add_de -s sub-01/ -subjid sub-01 -n nidm.ttl
```
e.g. where sub-01 is the FreeSurfer derivatives folder. 

Tip: Ensure the file paths are fully referenced:

```
segstats2nidm -add_de -s ~/proj/derivatives/freesurfer/sub-01 -subjid sub-01 -n ~/proj/nidm.ttl
```
The FreeSurfer annotations will append to the nidm.ttl so all the project data can be queried in a central file.

