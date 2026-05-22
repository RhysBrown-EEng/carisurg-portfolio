
## **Overview:**
<p>This repo shows the various assignments done in Week 0 of the Carisurg AI Healthcare Training Program. </p>

## **Assignments:**

1. **Assignment 1** - This code cleans the gender column of the Emergency Triage Dataset. The dataset had various inconsistencies which were corrected. Other gender identities beyond male and female are encoded via an "Other" category. I have 2 implementations in the notebook: one for simple mapping and one which uses dummy variables. <br>
Note: 1 represents male, 0 represents female, and 2 represents other for the simple mapping. <br>
2. **Assignment 2** - This code builds on assignment 1. The assignment 1 code for gender encoding with 1 and 0 was used (dummy variables were **not** used in this assignment). SBP and GCS were cleaned based on method used in tutorial 2. DBP was also cleaned to remove all non-number values. The median was used for imputing all NaNs and out-of-range values. <br>
Note: All unique/missing variables that did not meet the desired format were removed in the columns: Gender, SBP, DBP and GCS. <br>
