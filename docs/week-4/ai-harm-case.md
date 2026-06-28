# Week 4: Interim Deliverable
Scholar Name: Rhys Brown

CariSurg MedTech Pathways Programme, Healthcare AI Cohort (2026) <br>


## AI Harm Case

Early-warning systems for sepsis have been associated with reduced mortality leading to the creation of various implementations to do this task. The Epic Sepsis Model (ESM) is a widely used sepsis early-warning deployed across hundreds of hospitals in the United States. The proprietary model was developed and validated by Epic Systems Corporation using data from 405,000 patient encounters (1).

The model was advertised by Epic Systems Corporation to have an area under the operating curve (AUC) of 0.76 to 0.83. In this case, the AUC score measured how accurately an AI model tells the difference between a patient with sepsis and a healthy one on a scale from 0.50 (completely guessing) to 1.00 (perfectly accurate). However, the researchers validated the model on 27,697 patients who collectively had 38,455 hospitalizations. It was found that the model could predict the onset of sepsis with real world AUC of only 0.63. Moreover, the model failed to identify 67% of patients with sepsis, 60% of whom then failed to receive timely antibiotics. Simultaneously, sepsis was falsely identified in 18% of the hospitalizations. Due to the various patients who had late antibiotics in part due to the model’s failure, ESM caused operational harm which risked patient health outcomes. (1)

As a proprietary model, ESM did not undergo a rigorous peer-review nor did it have the ability to have its internal structure examined by clinicians. Furthermore, the model was widely used despite a lack of independent external validation (1). This lack of external validation was the immediate cause for the harm as the model should not have been used without said validation. 

The root cause for this incident could be defined as a governance failure. The model should have been externally verified by an independent American health organization. In the absence of this external data, the bundling of ESM into already used electronic health record systems nation-wide made widespread implementation inevitable. Without proof to the contrary, the system was assumed to be safe and accurate across various clinical contexts. This failure was mostly technical. The model was not externally verified across enough clinical contexts and likely suffered from distribution shift. The rate of sepsis as well as its presentation differed enough in the real-world to cause the model to produce consistent false positives and negatives. ‘

One specific design safeguard that would have prevented the documented harm would be stronger government safeguards as well as strict adherence to the WHO principles for Artificial Intelligence (AI) in a  clinical setting (2). If proper government standards were implemented, the model could not have been employed without the necessary external validation. The 2 main WHO clinical AI  principles of note are that the AI must be transparent and focus on ensuring equity. Focus on these principles would not have allowed a black box clinical system to be developed and circulated without external validation. More inclusive datasets would have increased the equity of the model and reduced the likelihood of distribution shift. Finally, mandatory real-world silent testing of the model across at least 10 hospitals nationwide would have determined algorithmic accuracy in the background without risking active patient care.
 
## References 

1.	Wong A, Otles E, Donnelly JP, Krumm A, McCullough J, DeTroyer-Cooley O, et al. External Validation of a Widely Implemented Proprietary Sepsis Prediction Model in Hospitalized Patients. JAMA Intern Med. 2021 Aug 1;181(8):1065. doi:10.1001/jamainternmed.2021.2626 
2.	Ethics and Governance of Artificial Intelligence for Health: WHO Guidance. 1st ed. Geneva: World Health Organization; 2021. 1 p. 
