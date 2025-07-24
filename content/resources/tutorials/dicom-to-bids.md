---
title: Converting DICOM Data to BIDS
linkTitle: Converting DICOM to BIDS
type: docs
weight: 5 
---

**[Reproducible neuroimaging principles](/about/principles/#repronims-four-core-principles)**: 2. Data and metadata management.

**[Actions](/about/principles/#repronims-four-core-actions)**: Standards, Annotation and provenance.

**Standards**: [BIDS](/resources/tools/bids/index.html).

**Tools** [HeuDiConv](/resources/tools/heudiconv/index.html), [ReproIn](/resources/tools/reproin/index.html).

## Challenge

Using standardized file organization and naming schemes form the basis of basic data management, making it easy to understand, work with and find data files. Using *the* standard way of organizing your data that is shared by other members of the field is even better.  Why?  Because a community standards means that it is much easier to adopt new tools and share your data with your labmates and colleagues. Community standards are integral to the new NIH Data Management and Sharing requirements. Neuroimaging has such a standard:  the Brain Imaging Data Structure or BIDS.  BIDS has been adopted widely and is the standard required by the OpenNeuro database.  Implementing a standard is worthwhile but can be challenging ([see Bush et al., 2022](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2022.988084/full)).

## Exercise

Here we will learn how to convert data coming off the scanner as **DICOM** files into **nifti** format organized according to **BIDS** using **HeuDiConv**, a tool that maps DICOM file information into organized BIDS directories. HeuDiConv **(Heuristic DICOM Converter)** utilizes Python scripts called **heuristics** that provide a set of rules to guide the conversion and organization of DICOM files into BIDS. The use of custom heuristics makes  HeuDiConv a versatile and highly configurable tool.

![Diagram showing the contents of a DICOM dataset and its structure in BIDS.](/images/dicom-bids-inverted.png)
[DICOM (left) to BIDS (right)](https://bids.neuroimaging.io/assets/img/dicom-reorganization-transparent-white_1000x477.png)

## Before you start

Before diving into the conversion process, it's important to familiarize yourself with the following:

* **DICOM (Digital Imaging and Communications in Medicine):** The standard format for medical imaging data, including neuroimaging. DICOM files store both image data and metadata in a complex structure, making it challenging to work with directly for analysis.
* **BIDS (Brain Imaging Data Structure):** A widely adopted standard for organizing neuroimaging data. BIDS enforces a specific directory structure and file naming conventions, promoting data organization, shareability, and compatibility with various analysis tools.  We recommend visiting the [BIDS website](https://bids.neuroimaging.io/index.html) and browsing the [BIDS starter kit](https://bids-standard.github.io/bids-starter-kit/)
* **Python**:  HeuDiConv requires creating a script in Python.

## Step by step guide

### Step 1: Install the necessary tools

* **HeuDiConv:** Installation instructions can be found on the HeuDiConv GitHub page. You may want to verify the installation instructions on this website are up to date.
* **dcm2niix:** HeuDiConv utilizes dcm2niix to convert DICOM files to the NIfTI format, required by BIDS. You'll need to install dcm2niix,  separately. You can find installation instructions on the [dcm2niix](https://github.com/rordenlab/dcm2niix) website.

### Step 2: Create a heuristic file

Heuristics are the heart of HeuDiConv's flexibility. They provide the instructions for mapping your specific DICOM data into the desired BIDS structure. You have two options:

* **Create Your Own Heuristic:** This provides maximum control and is often necessary for retrospective studies with inconsistent DICOM organization or use one of the existing HeuDiConv templates..
* **Analyze Your DICOM Data:** Carefully examine your DICOM dataset, understanding its directory structure, file naming patterns, and relevant metadata within the DICOM headers.
* **Design the Output Structure:** Define your desired output structure, aligning with BIDS specifications if aiming for BIDS compatibility.
* **Write the Python Script:** Create a Python file (e.g., heuristic.py) with functions that parse the DICOM metadata and determine the output file names and directory placements.

Here's a basic example heuristic, heuristic.py:

```python
def infotodict(seqinfo):
   """Heuristic function to map DICOM sequences to BIDS format."""
   info = {
       't1w': [],  # T1-weighted images
       'bold': [],  # Functional BOLD scans
       'dwi': []  # Diffusion-weighted images
   }
   for s in seqinfo:
       if 'T1w' in s.protocol_name:
           info['t1w'].append(s.series_id)
       elif 'BOLD' in s.protocol_name:
           info['bold'].append(s.series_id)
       elif 'dwi' in s.protocol_name:
           info['dwi'].append(s.series_id)
   return info
```

**Customization Tips for Working with Heuristics**:

* **Protocol Names:** Adjust 'T1w', 'BOLD', and 'dwi' to match the protocol names used in your DICOM data.
* **Scan Types:** Add more keys to the info dictionary (e.g., 'flair') for other image types present in your dataset.
* **Use a Template Heuristic:** A more convenient option for prospective studies or datasets that adhere to specific acquisition conventions.

| RePROtip:  You can avoid dealing with writing a heuristic altogether by using the ReproIn protocol naming conventions when you are configuring the imaging protocol on your scanner.   |
| :---- |

Example:  Instead of calling your structural imaging protocol “mp\_rage”, call it “T1w”.

Implementing these naming conventions means that you do not have to use a custom heuristic file, as HeuDiConv recognizes the ReproIn conventions.

### Step 3: Run the conversion

Once you have your heuristic file ready, use the following command to initiate the conversion:

heudiconv \-d DICOM\_DIR\_TEMPLATE \-o BIDS\_OUTDIR \-f HEURISTIC\_FILE \-c dcm2niix \-b \--minmeta

* **\-d DICOM\_DIR\_TEMPLATE:** The path to your DICOM directory, using wildcards (\*) if needed to match file patterns.
* **\-o BIDS\_OUTDIR:** The desired output directory where your BIDS-formatted data will be stored.
* **\-f HEURISTIC\_FILE:** The path to your chosen heuristic file (-f heuristic.py). If you are using the ReproIn convention (see RePROtip above), simply indicate ‘-f reproin’.
* **\-c dcm2niix:** Specifies dcm2niix as the conversion tool to convert DICOM into nifti file format.  The BIDS specification requires nifti format for MRI data.
* **\-b:** Enables BIDS compatibility mode.
* **\--minmeta:** Minimizes the amount of metadata written to the output files. You can adjust this based on your requirements.

### Step 4: Validate

After the conversion completes, carefully validate your BIDS output using the BIDS Validator tool. The BIDS Validator helps identify any deviations from the BIDS specification, ensuring your data is properly formatted for future analysis and sharing. You can find the BIDS Validator online. You may want to verify that the website is up to date.

## Next steps

Remember, HeuDiConv offers significant flexibility. Exploring its documentation and seeking help from the community can further enhance your understanding and utilization of this tool.

While HeuDiConv is certainly the tool with the most flexibility, you can also use a number of other DICOM to BIDS tools (e.g., EasyBIDS) through Nipoppy, another ReproNim tool.
