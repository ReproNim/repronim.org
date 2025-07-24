---
title: Using NeuroDocker to containerize computational workflows
type: docs
weight: 5
---

[**Reproducible neuroimaging principles**](/about/principles/#repronims-four-core-principles)**: 3f: Software management: Use containers when reasonable**

[**Actions**](https://repronim.netlify.app/about/principles/#repronims-four-core-actions)**:  Use of containers**

**Tools:** [Docker](https://docs.docker.com/), [Neurodocker](/resources/tools/neurodocker/)

## Challenge

Ensuring reproducible data processing requires a clear understanding of the software environment used in the analysis.
The outcome of an analysis depends on three main components: data, analysis scripts, and analysis environment (software and hardware).

Modern operating systems are complex, and analysis software often depends on numerous system components, including:

- System libraries bundled with the operating system
- User-installed software packages and libraries
- Environment variables and settings that influence execution
- Hardware interactions (e.g., multicore processing, GPU acceleration)
- Schedulers and computing clusters that manage resource allocation

Given the complexity of the environment, it is crucial to:

- Document software and hardware dependencies for accurate reproducibility
- Identify which components impact results to avoid unintended variability
- Recreate the original analysis environment for consistent execution

Containers provide a robust solution by encapsulating software dependencies into isolated, consistent environments that can be easily shared and executed across different systems.

Docker is the most widely used containerization platform, enabling users to create, share, and deploy containerized applications efficiently.
Docker containers are lightweight, portable, and ideal for cloud computing and development environments.
However, most High-Performance Computing (HPC) centers do not support Docker due to security concerns.

Singularity (now Apptainer) is a container platform specifically designed for HPC and scientific research.
Singularity does not require root privileges, making it more secure and suitable for shared computing environments such as HPC clusters.
It allows researchers to run containerized workflows while maintaining compatibility with cluster-based systems.
Apptainer is the open-source continuation of Singularity and is now maintained by the Linux Foundation.

To create a Docker or Singularity/Apptainer container, users must write a recipe file that specifies the environment's dependencies, configurations, and installation steps.
However, writing a recipe file for complex software can be challenging and time-consuming.

Neurodocker addresses this issue by automating the process.
It is a command-line tool that generates custom Dockerfiles and Singularity recipes for neuroimaging applications and can also minify existing containers to reduce their size.

## Exercise:

In this exercise we show how you can create your first docker recipe file using Neurodocker and build your container using the file.

## Before you start

If you’re new to containers, you may want to read more about their motivation and use cases.
A good starting point is the [What is Docker website](https://docs.docker.com/get-started/docker-overview/).
For insights into scientific applications and HPC, check out the [Introduction to Singularity](https://apptainer.org/user-docs/master/introduction.html).

You could also watch a video that was a part of the [ABCD-ReproNim training](https://www.abcd-repronim.org/index.html): [Introduction to Container Technology](https://www.youtube.com/watch?v=UHw-DVgm-pE) (the slides could be found [here](https://drive.google.com/file/d/1lRfo30076maHOPLd4M2TMvRfB833mELI/view)).
The video is divided into three main parts, allowing you to choose based on your needs:

- Introduction of the containers and Docker/Singularity in case you need more overview and motivation: minutes 1–10.
- Explanation on how to use containers with Demo: minutes 10–30.
- How to use Neurodocker and create an image (this is also a topic of the guide below, but you can watch it as an additional material either before or later): minutes 30-44

In this tutorial we will be using Docker software, be sure to install Docker before starting.
If you are using Linux system you can install only a lightway [Docker Engine](https://docs.docker.com/engine/), for other platforms you should install [Docker Desktop](https://docs.docker.com/desktop/).

## Step by step guide

#### **Step 1: Installing Neurodocker**

Neurodocker is a python package that can be installed from PyPI.

```
pip install neurodocker
```

However, you can also get a container with neurodocker installed inside.

```
docker pull repronim/neurodocker:latest
```

You can check if neurodocker is working properly by running help:

```
neurodocker --help
```

Equivalent command if you run the container.

```
docker run -rm repronim/neurodocker --help
```

#### **Step 2: Generating Dockerfile using Neurodocker**

If you successfully run the `--help` command, you'll see that one of the available commands is `generate`.
Running `neurodocker generate --help` will show you that Neurodocker can generate either a Dockerfile or a Singularity recipe.
In this exercise, we will focus on creating a Dockerfile.

To generate a custom Dockerfile, you need to specify a set of options—such as the base image, the software to install, and any commands to run inside the container.
Neurodocker streamlines this process by providing support for widely used neuroimaging tools like FSL, ANTs, and SPM, as well as general-purpose software such as Python, which can be installed via Miniconda.
The full list of supported software can be found on [Neurodocker webpage](https://www.repronim.org/neurodocker/user_guide/cli.html#neurodocker-generate-docker), or by running `neurodocker generate docker --help`.

Two options are required for each Dockerfile, `--pkg-manager` and `--base-image`.
We can use `debian:buster-slim` as a base image, and `apt` is the package manager that is used by debian.
The very basic example would look like:

```
neurodocker generate docker \
    --pkg-manager apt \
    --base-image debian:buster-slim
```

In the output you should see the content of Dockerfile required to create an image, as well as the neuroodocker specification used in the example.

In order to save it in the Dockerfile, redirect the output:

```
neurodocker generate docker \
    --pkg-manager apt \
    --base-image debian:buster-slim \
    > Dockerfile
```

#### **Step 3: Installing FSL software**

If we want to install specific neuroimaging software, e.g., FSL, we can check the arguments for this package.
The only mandatory argument is `version`, so you can add FSL to the image by adding `--fsl version=6.0.7.1.`

```
neurodocker generate docker \
   --pkg-manager apt \
   --base-image debian:bullseye-slim \
   --yes \
   --fsl version=6.0.7.1 \
   > fsl6071.Dockerfile
```

You might have noticed that, in addition to the `--fsl` option, there is also a new flag: `--yes`.
This flag is related to the FSL license agreement, which requires you to acknowledge that the software is not free.
By including `--yes`, you are automatically accepting the license terms, allowing Neurodocker to proceed without prompting for manual confirmation.

#### **Step 4: Building Docker Image**

Once you have created Dockerfile using Neurodocker, you could build the Docker Image using the standard Docker command:

```
docker build --tag fsl:6.0.7.1 --file fsl6071.Dockerfile .
```

#### **Step 5: Generating Singularity recipe file**

If you want to use Singularity, you’ll need to create a Singularity image.
This can be done in two ways: either by converting an existing Docker image or by creating a Singularity recipe file and building the image directly from it.

As mentioned earlier, Neurodocker can also assist with generating a Singularity recipe.
To do this, simply run `neurodocker generate singularity`, you should run `neurodocker generate docker`, e.g.:

```
neurodocker generate singularity \
  --pkg-manager apt \
  --base-image debian:bullseye-slim \
  --yes \
  --fsl version=6.0.7.1 \
  > fsl6071.Singularity.def
```

# Next Step

The has been pretty brief introduction from to Neurodocker.
If you would like to learn more, you should review the [Neurodocker documentation](https://www.repronim.org/neurodocker/index.html), especially the [example section](https://www.repronim.org/neurodocker/user_guide/examples.html), where you can see examples of various neuroimaging packages.

You could also learn how Neurodocker can help you to [minify containers](https://www.repronim.org/neurodocker/user_guide/minify.html) using ReproZip.
