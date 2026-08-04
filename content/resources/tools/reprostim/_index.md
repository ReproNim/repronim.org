---
title: "ReproStim"
---

*Automated capture of audio-visual stimuli into BIDS datasets.*

ReproStim is a video/audio capture and recording system for neuroimaging and psychology research.  It runs silently in the background during data collection to produce a complete, high-fidelity record of the audio-visual stimuli actually delivered to the subject, so that sessions can be reproduced and irregularities can be diagnosed after the fact.

ReproStim is one component of the wider ReproFlow ecosystem:

<figure>
  <object type="image/svg+xml" data="/images/reproflow.svg" width="100%" style="max-width: 100%; height: auto;">
    <img src="/images/reproflow.svg" alt="ReproFlow ecosystem diagram showing ReproStim's role alongside DataLad, HeuDiConv, ReproIn, ReproMon, ReproEvents, and related components." />
  </object>
  <figcaption>
    ReproFlow ecosystem diagram — this is an interactive SVG; boxes link to the respective sub-projects.
    Source: <a href="https://github.com/ReproNim/artwork/blob/master/posters/ReproFlow-OHBM2024-poster.svg">ReproNim ReproFlow, OHBM 2024 #2277</a>.
  </figcaption>
</figure>

## Development status

ReproStim is actively developed and used in production.

## Innovation

Experimental stimuli are typically documented only by the code that was intended to run, not by what was actually presented to the subject.  ReproStim closes that gap by recording the true audio-visual signal delivered to the subject and integrating those recordings into the corresponding BIDS dataset, with time-synchronization markers (e.g. QR codes) that make it possible to align capture with acquisition.

## Requisite knowledge to use

- Command line familiarity
- Basic BIDS familiarity
- Familiarity with Docker or Singularity (for containerized use)

## Requisite technical requirements

- A capture device supported by ReproStim (see the [hardware](https://reprostim.readthedocs.io/) section of the docs)
- A system with Python installed, or
- A system with Docker or Singularity installed

## Links

- Home page: https://github.com/ReproNim/reprostim/
- Full documentation: https://reprostim.readthedocs.io/en/latest/
- Installation: https://reprostim.readthedocs.io/en/latest/install/index.html
- Singularity containers: https://datasets.datalad.org/?dir=/repronim/containers/images/repronim (files named `repronim-reprostim--*.sif`, distributed via [ReproNim/containers](https://github.com/ReproNim/containers))
- How to get help:
  - https://github.com/ReproNim/reprostim/issues
  - https://neurostars.org/tag/reprostim

## Representative publications
