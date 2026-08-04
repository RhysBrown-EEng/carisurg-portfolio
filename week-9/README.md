# Week 9 - Designing & Prototyping Human-Centred System (HCI/HRI)

## Overview

This week started the process of prototyping to build our final triaging system. We explore two major system types for implementation in the emergency department: a Human-Computer Interface (HCI) and a Human-Robot Interface (HRI).

## Final Decision
> [!IMPORTANT]
>It was decided to use a HCI-based kiosk paired with the final machine learning model developed in previous weeks.

### Details:
The HCI allows patients to self-register and assigns a triage level based on vitals and chief complaints. It guides the user through placing a wearable appropriately to take their own vitals in an accurate manner. 

This system is not meant to be used for the highest acuity ESI-1 patients as they are so ill and require urgent 

## What this folder contains

The structure of this folder is as follows:
```text id="structure"
week-9/
│
├── hci-co-canvas.pdf
├── hri-co-canvas.pdf
├── hci-mockup-screenshot.png
├── hci-mockup-sketch.jpeg
├── system-requirements.md
├── Emergency Triage Kiosk UI.make
└── README.md
```

| File | Description |
|------------|-------------|
| `hci-co-canvas.pdf` | Datasets required to reproduce the analyses. Specific data files are not included in this repository. See [Data](#data) and [How to Use](#how-to-use) for more details.|
| `hri-co-canvas.pdf` |  Reports, proposals and written assignments completed during the programme. |
| `hci-mockup-screenshot.png` | Jupyter notebooks containing data preprocessing, data analysis and other exploratory project-related code. |
| `hci-mockup-sketch.jpeg` | Source code and reusable Python scripts for building and evaluating the finalized models. |
| `system-requirements.md` | Folder that contains `train.py`, the entry-point to this repo. |
| `Emergency Triage Kiosk UI.make` | Folder that contains pytests for final macine learning pipeline. |
| `README.md` | Folder that contains pytests for final macine learning pipeline. |

