# Handover Document

## 1. Project Summary
This project is a machine learning model trained to triage patients. It uses patient vitals in order to classify acuity on the Emergency Severity Index (ESI) scale.


## 2. Final-Model Decision
The Ensemble Model won due to it having the highest recall and the highest aggregate accuracy across ESI class 2-5.

## 3. How to Run
1. Clone the repository and open it:
```
git clone https://github.com/RhysBrown-EEng/carisurg-portfolio.git
cd carisurg-portfolio
```
2. Create a virtual environment and then activate it:

| Step | Windows | macOS / Linux | Git Bash      |
|------|--------|----------------|----------------|
| Create virtual environment | `python -m venv .venv` | `python3 -m venv .venv` | `python -m venv .venv` |
| Activate virtual environment | `.venv\Scripts\activate` | `source .venv/bin/activate` | `source .venv/Scripts/activate` |

3. Install the dependencies:
```
pip install -r requirements.txt
```

4. Run `train.py`:

| Environment | Command |
|---|---|
Windows | `python scripts/train.py --config config.yaml` |
| macOS / Linux | `python3 scripts/train.py --config config.yaml`| 


## 4. Where the Data Lives
The data is stored in `data/` however it is not tracked via Git due to restrictions regarding medical data. 


## 5. Known Limitations
- Model still unverified on a Caribbean cohort.
- Demographics almost entirely unconsidered.
- ESI-1 recall still modest.

## 6. Who to Ask
Refer questions to
Rhys Brown. <br>
rhysdzbrown@gmail.com
<br> <br>
CariSurg MedTech Pathways Programme, Healthcare AI Cohort (2026)<br>
https://carisurg.com/