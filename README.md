# **Carisurg AI Healthcare Training Program:**
## **Overview:**
<p>This repo shows the various assignments done in the Carisurg AI Healthcare Training Program. </p>

## **Week 0 Assignments:**
All assignments listed below can be found in the `week-0` folder :

1. **Assignment 1** - This code cleans the gender column of the Emergency Triage Dataset. The dataset had various inconsistencies which were corrected. Other gender identities beyond male and female are encoded via an "Other" category. I have 2 implementations in the notebook: one for simple mapping and one which uses dummy variables. <br>
Found under file name: `Assignment_1_Rhys_Brown.ipynb` <br>
Note: 1 represents male, 0 represents female, and 2 represents other for the simple mapping. <br>
2. **Assignment 2** - This code builds on assignment 1. The assignment 1 code for gender encoding with 1 and 0 was used (dummy variables were **not** used in this assignment). SBP and GCS were cleaned based on method used in tutorial 2. DBP was the chosen column which was also cleaned to remove all non-number values. The median was used for imputing all NaNs and out-of-range values. <br>
Found under file name: `Assignment_2_Rhys_Brown.ipynb` <br>
Note: All unique/missing variables that did not meet the desired format were removed in the columns: Gender, SBP, DBP and GCS. <br>
3. **Assignment 3** - This assignment focuses on data visualization. It takes the cleaned data (all columns) and uses it to evaluate several clinical questions. These are: <br>
     * What is the distribution of MAP that patients come to the ED with? Based on this, how patients can be said to be exhibiting symptoms of hypotension & hypertension? - done using a histogram.
     * Is there a relationship between FIO2 and Respiratory Rate in these patients? - done using a scatter plot.
     * Is there a relationship between MAP and Age in these patients? Does MAP increase/decrease with age on average? - done using a scatter plot.
Found under file name: `Assignment_3_Rhys_Brown.ipynb` <br>
4. **Assignment 4** -  This assignment describes the Glasgow Comma Scale, its use, calculations and overall cinical relevance in triaging.
   Found under file name: `Assignment_4-Rhys_Brown.pdf` <br>
6. **Assignment 5** -  This assignment describes an unconsidered metric that would be crucial in triage, SpO2. This assignment discusses its use, calculations and overall cinical relevance in triaging.
   Found under file name: `Assignment_5-Rhys_Brown.pdf` <br>
 
