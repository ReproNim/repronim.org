---
title: Advanced Containerization Using DataLad
type: docs
weight: 5
---

**[Reproducible neuroimaging principles](/about/in-practice/#repronims-principles-of-reproducible-neuroimaging)**: 2a: Use standard data formats, 2b: Use data version control, 2c: Annotate data, 3: Software management.

**[Actions](/about/in-practice/#repronims-four-core-actions)** Standards, Annotation and provenance, Version control, Containers.

**Standards**: [BIDS](/resources/tools/bids/index.html).

**Tools**: [DataLad](/resources/tools/datalad/index.html), [Singularity/Apptainer](https://apptainer.org/).

## Challenge

Using version control and automation to execute procedures can produce re-executable and provenance-rich results, but the task can appear daunting.
Following best-practices for file layouts (DataLad + YODA Principles) provide clear connections (via subdatasets) between the source data and the derivative data that is produced.
Additionally, utilizing `datalad run` with `repronim-containers` preserves the provenance of exactly what software versions were used and how, leaving a detailed trail for future work.

## Exercise

Let's assume that our goal is to do Quality Control of an MRI dataset
(which is available as DataLad dataset ds000003). We will create a new
dataset with the output of the QC results (as analyzed by mriqc
BIDS-App).

- create a new dataset which would contain results and everything needed
    to obtain them
- install/add subdatasets(code, other datasets, containers)
- perform the analysis using **only** materials available within the reach of this dataset.

This would help to guarantee reproducibility in the future because all the
materials would be *reachable* within that dataset.

Note: This exercise is based on the [ReproNim/containers README](https://github.com/ReproNim/containers/), which should be referenced for more information.

## Before you start

Required knowledge:

 - Basics of operating in a terminal environment

Though it is not strictly necessary to be familiar with all of the tools used
to complete the tutorial, knowledge of the following will be helpful for adapting this tutorial to
your usecase:

- [Datalad](https://datalad.org)
- [datalad-container extension](http://docs.datalad.org/projects/container/en/latest/index.html)
- [YODA Organigram](https://github.com/myyoda/poster/blob/master/ohbm2018.pdf)
- [Singularity/Apptainer](https://apptainer.org/)

## Step by step guide

### Step 1: Install the necessary tools

The following tools should be installed:

- [Datalad](https://handbook.datalad.org/en/latest/intro/installation.html)
- [Singularity/Apptainer](https://apptainer.org/docs/admin/main/installation.html)

Additionally, the `datalad-container` extension should also be installed.

```bash
pip install datalad-container
```

### Step 2: Start a DataLad dataset

Following YODA, our dataset for the results is **the** dataset that will contain everything needed to produce those results.

```bash
mkdir ~/my-experiments
cd ~/my-experiments
datalad create -d ds000003-qc -c text2git
cd ds000003-qc
```
### Step 3: Install source data

Next we install our source data as a subdataset.

```bash
datalad install -d . -s https://github.com/ReproNim/ds000003-demo sourcedata
```

### Step 4: Install ReproNim/containers

Next we install the `ReproNim/containers` collection.

```bash
datalad install -d . -s ///repronim/containers code/containers
```

Now let's take a look at what we have.

```
/ds000003-qc # The root dataset contains everything
 |--/sourcedata # we call it source, but it is actually ds000003-demo
 |--/code/containers # repronim/containers, this is where our non-custom code lives
```

### Step 4: Freeze container image versions

`freeze_versions` is an optional step that will record and "freeze" the
version of the container used. Even if the `///repronim/containers` dataset is
upgraded with a newer version of our container, we are "pinned" to the
container we explicitly determined. Note: To switch version of the container
(e.g., to upgrade to a new one), rerun `freeze_versions` script with the version
specified.

The container version can be "frozen" into the clone of the `///repronim/containers`
dataset, **or** the top-level dataset.


**Option 1: Top level dataset (recommended)**

```bash
# Run from ~/my-experiments/ds000003-qc
datalad run -m "Downgrade/Freeze mriqc container version" \
  code/containers/scripts/freeze_versions --save-dataset=. bids-mriqc=0.16.0
```

**Option 2: ///repronim/containers**

```bash
# Run from ~/my-experiments/ds000003-qc/
datalad run -m "Downgrade/Freeze mriqc container version" \
    code/containers/scripts/freeze_versions bids-mriqc=0.16.0
```

Note: It is recommended to freeze a container image version into the
top-level dataset to simplify reuse. If `///repronim/containers` is
modified in any way, the author must ensure that their altered fork of
`///repronim/containers` is publicly available and that its URL
specified in the `.gitmodules`. By freezing into the top-level dataset
instead, authors do not need to host a modified version of
`///reporonim/containers`.

#### Fixup datalad config

The version of mriqc we are using does not have an option  `--no-datalad-get` which is hardcoded
into mriqc config, so we should remove it.

```bash
datalad run -m "Remove ad-hoc option for mriqc for older frozen version" sed -i -e 's, --no-datalad-get,,g' .datalad/config
```

### Step 5: Run the containers

When we run the bids-mriqc container, it will need a working directory
for intermediate files. These are not helpful to commit, so we will
tell `git` (and `datalad`) to ignore the whole directory.

```bash
echo "workdir/" > .gitignore && datalad save -m "Ignore workdir" .gitignore
```

Now we use `datalad containers-run` to perform the analysis.

```bash
datalad containers-run \
        -n bids-mriqc \
        --input sourcedata \
        --output . \
        '{inputs}' '{outputs}' participant group -w workdir
```

If everything worked as expected, we will now see our new analysis, and
a commit message of how it was obtained! All of this is contained within
a single (nested) dataset with a complete record of how all the data was
obtained.

```shell
(git) .../ds000003-qc[master] $ git show --quiet
Author: Austin <austin@dartmouth.edu>
Date:   Wed Jun 5 15:41:59 2024 -0400

    [DATALAD RUNCMD] ./code/containers/scripts/singularity_cm...

    === Do not change lines below ===
    {
     "chain": [],
     "cmd": "./code/containers/scripts/singularity_cmd run code/containers/images/bids/bids-mriqc--0.16.0.sing '{inputs}' '{outputs}' participant group -w workdir",
     "dsid": "c9c96ab9-f803-43ba-83e2-2eaec7ab4725",
     "exit": 0,
     "extra_inputs": [
      "code/containers/images/bids/bids-mriqc--0.16.0.sing"
     ],
     "inputs": [
      "sourcedata"
     ],
     "outputs": [
      "."
     ],
     "pwd": "."
    }
    ^^^ Do not change lines above ^^^
```

This record could later be reused (by anyone) using [datalad rerun] to rerun
this computation using exactly the same version(s) of input data and the
singularity container. You can even now [datalad uninstall] sourcedata and even containers
sub-datasets to save space - they will be retrievable at those exact versions later
on if you need to extend or redo your analysis.

## Notes

- aforementioned example requires DataLad >= 0.11.5 and datalad-containers >= 0.4.0;
- for more elaborate example with use of [reproman] to parallelize execution on
  remote resources, see [ReproNim/reproman PR#438](https://github.com/ReproNim/reproman/pull/438);
- a copy of the dataset is made available from [`///repronim/ds000003-qc`](http://datasets.datalad.org/?dir=/repronim/ds000003-qc)
  and [ds000003-qc](https://github.com/ReproNim/ds000003-qc).

[reproman]: http://reproman.repronim.org
[datalad rerun]: http://docs.datalad.org/en/stable/generated/man/datalad-rerun.html
[datalad uninstall]: http://docs.datalad.org/en/stable/generated/man/datalad-uninstall.html
