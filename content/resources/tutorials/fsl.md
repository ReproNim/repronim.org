---
title: Annotating FSL Data
linkTitle: Annotating FSL Data
type: docs
weight: 5 
---

**[Reproducible neuroimaging principles](/about/principles/#repronims-four-core-principles)**: 2b. Use standard data formats.

**[Actions](/about/principles/#repronims-four-core-actions)**: Standards, Annotation and provenance.

**Standards**: [BIDS](/resources/tools/bids/index.html), [NIDM](/resources/tools/nidm/index.html).

**Tools**: [PyNIDM](/resources/tools/pynidm/index.html), [fslsegstats2nidm](https://github.com/ReproNim/fsl_seg_to_nidm).

## Challenge
[FSL](https://fsl.fmrib.ox.ac.uk/) (FMRIB Software Library) is a comprehensive library of analysis tools for fMRI, MRI and diffusion brain imaging data. FSL produces volumetric subcortical anatomical maps. We want to link the neuroanatomical labels (e.g. hipp_l_vol) to concepts (e.g. a label of "Left Hippocampus" and a measurement of volume). NIDM makes data more meaningful and easier to interpret by both humans and machines by incorporating standardized vocabularies and defining the connections between data elements, leveraging knowledge from community ontologies. In the process we join the FSL results with the [BIDS/demographic data dictionary](/resources/tutorials/data-dictionary/). 

## Exercise
In these instructions we install a development environment (i.e. conda), install the FSL annotation tool fsl_seg_to_nidm and annotate the FSL output.

## Before you start
In a typical workflow for annotating a project, the first step is capturing the BIDS information and demographic details shown in Creating a [BIDS Data Dictionary and Adding Semantics](/resources/tutorials/data-dictionary/). During the annotation process we will join FSL annotations with the BIDS data dictionary. For this tutorial, the initial BIDS data dictionary is saved to /project/nidm.ttl. 

These instructions expect FSL processing and QC has been completed. We ran both FIRST (https://fsl.fmrib.ox.ac.uk/fsl/docs/#/structural/first) and FAST (https://fsl.fmrib.ox.ac.uk/fsl/docs/#/structural/fast). FSL must be installed on the workstation running these scripts.

## Step by step guide
Given the FSL results, we will use the fslsegstats2nidm program (https://github.com/ReproNim/fsl_seg_to_nidm) to create a NeuroImaging Data Model (NIDM) semantically marked up version of the neuroimaging data. 

### Step 1: Create a Conda development environment
Install Conda https://docs.anaconda.com/free/miniconda/miniconda-install/. Then in terminal:

```
conda create -n repro python=3.9
conda activate repro
```

### Step 2: Clone a copy of the repository and install

```
git clone https://github.com/ReproNim/fsl_seg_to_nidm.git
cd fsl_seg_to_nidm
python setup.py install
```

### Step 3: Convert FSL results to a JSON
If FIRST and FAST were run out-of-the-box, use the fsl2jon.py script in the root of the fsl_seg_to_nidm directory to generate the segmentation json files (segstats.json). For example:

```
python fsl2json.py root_of_fsl_derivatives_directory
```
e.g. 

```
python fsl2json.py ~/Desktop/proj/derivatives/fsl/ 
```

### Step 4: Annotate FSL results
Generate annotations of the FSL data with the following command. Note the nidm.ttl was previously created as per the [BIDS/demographic data dictionary tutorial](/resources/tutorials/data-dictionary/):
```
fslsegstats2nidm -add_de -d segstat_file -subjid sub-01 -n nidm.ttl
```
e.g.
```
fslsegstats2nidm -add_de -d ./proj/derivatives/fsl/sub-01/segstats.json -subjid sub-01 -n ./proj/nidm.ttl
```
The FSL annotations will append to the nidm.ttl so all the project data can be queried in a central file.

## FSL Common Data Elements
Here is the mapping between FSL CDEs and regions of interest.

| FSL\_code | Region of interest |
| :---- | :---- |
| fsl\_000001 | Background (voxels) |
| fsl\_000002 | Background (volume) |
| fsl\_000003 | Left-Accumbens-area (voxels) |
| fsl\_000004 | Left-Accumbens-area (volume) |
| fsl\_000005 | Left-Amygdala (voxels) |
| fsl\_000006 | Left-Amygdala (volume) |
| fsl\_000007 | Left-Caudate (voxels) |
| fsl\_000008 | Left-Hippocampus (volume) |
| fsl\_000009 | Left-Pallidum (voxels) |
| fsl\_000010 | Left-Putamen (volume) |
| fsl\_000011 | Left-Thalamus-Proper (voxels) |
| fsl\_000012 | Right-Accumbens-area (volume) |
| fsl\_000013 | Left-Putamen (voxels) |
| fsl\_000014 | Left-Putamen (volume) |
| fsl\_000015 | Left-Thalamus-Proper (voxels) |
| fsl\_000016 | Left-Thalamus-Proper (volume) |
| fsl\_000017 | Right-Accumbens-area (voxels) |
| fsl\_000018 | Right-Accumbens-area (volume) |
| fsl\_000019 | Right-Amygdala (voxels) |
| fsl\_000020 | Right-Amygdala (volume) |
| fsl\_000021 | Right-Caudate (voxels) |
| fsl\_000022 | Right-Hippocampus (volume) |
| fsl\_000023 | Right-Pallidum (voxels) |
| fsl\_000024 | Right-Putamen (volume) |
| fsl\_000025 | Right-Thalamus-Proper (voxels) |
| fsl\_000026 | Right-Accumbens-area (volume) |
| fsl\_000027 | Right-Putamen (voxels) |
| fsl\_000028 | Right-Putamen (volume) |
| fsl\_000029 | Right-Thalamus-Proper (voxels) |
| fsl\_000030 | Right-Thalamus-Proper (volume) |
| fsl\_000031 | csf (voxels) |
| fsl\_000032 | csf (mm^3) |
| fsl\_000033 | gray (voxels) |
| fsl\_000034 | gray (mm^3) |
| fsl\_000035 | white (voxels) |
| fsl\_000036 | white (mm^3) |
