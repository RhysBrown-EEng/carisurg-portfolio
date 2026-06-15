# CariSurg AI Healthcare Training Programme Portfolio

## Overview

This repository contains assignments completed as part of the CariSurg AI Healthcare Training Programme. The work focuses on clinical data analysis, alongside an exploration of the implementation and potential effectiveness of AI-assisted emergency triage systems. This project explores digital healthcare solutions for the Caribbean context, with a focus on improving emergency department triage and patient prioritisation.


This project is intended for programme tutors, clinical and technical reviewers, recruiters, and others interested in the application of AI in emergency triage and healthcare more broadly. It is structured to remain accessible to non-technical clinical reviewers.


## Project Structure
```text id="structure"
carisurg-portfolio/
│
├── data/
├── docs/
├── notebooks/
├── src/
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
```

| Directory | Description |
|------------|-------------|
| `data/` | Datasets required to reproduce the analyses. Specific data files are not included in this repository. See [Data](#data) and [How to Use](#how-to-use) for more details.|
| `docs/` |  Reports, proposals and written assignments completed during the programme. |
| `notebooks/` | Jupyter notebooks containing data preprocessing, data analysis and other project-related code. |
| `src/` | Source code and reusable Python scripts. |

## Installation
1. Clone the repository and open it:
```
git clone https://github.com/RhysBrown-EEng/carisurg-portfolio.git
cd carisurg-portfolio
```
2. Create a virtual environment and then activate it:

| Step | Windows | macOS / Linux | Git Bash      |
|------|--------|----------------|----------------|
| Create virtual environment | `python -m venv .venv` | `python3 -m venv .venv` | `python -m venv .venv` |
| Activate virtual environment | `.venv\Scripts\activate` | `source .venv/bin/activate` | `source .venv/bin/activate` |

3. Install the dependencies:
```
pip install -r requirements.txt
```

## How to Use
The notebooks can be run using either Jupyter Notebook or Google Colab. Follow the instructions corresponding to your preferred environment. 
<br> <br>
Using Jupyter Notebook:
1. Launch Jupyter Notebook:
```
jupyter notebook
```
2. Navigate to `notebooks/` directory in this repository.
3. Select from the available sub-folders and open your desired notebook.
4. Run all cells sequentially.

<br>

Using Google Colab:
1. Navigate to `notebooks/` directory in this repository.
2. Select from the available sub-folders and open your desired notebook.
3. Upload the notebook file to Google Colab (or open directly from GitHub). 
4. Open the notebook and run all cells sequentially.

**NOTE:** Notebooks are designed to be independent of one another and can be run in any order unless otherwise specified.

## Data
The datasets used in this project were provided by the [CariSurg](https://carisurg.com/) team. They are not included in this repository due to privacy and governance reasons. 

To reproduce the analysis, users must provide the dataset separately and place it in the `data/` directory prior to execution of the notebooks.

## Contributing
This repository represents a personal portfolio within the CariSurg AI Healthcare Training Programme.  
Consequently, contributions are not being accepted at this time.

However, feedback and suggestions from tutors, clinical or technical reviewers, or any other interested party are always welcome.

## License
This project is licensed under the MIT License.

See the `LICENSE` file for full details.

## Author
Rhys Brown <br>
rhysdzbrown@gmail.com
<br>
CariSurg MedTech Pathways Programme, Healthcare AI Cohort (2026)<br>
https://carisurg.com/

 
 
