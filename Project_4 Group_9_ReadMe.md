**Alzheimer's Disease Prediction and Visualization Project**

**Project Structure:**  
Project-4-group-9/ 
├── App3/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   ├── logic.js
│   │   │   ├── tableau_ap1.js
│   │   │   └── tableau_ap2.js
│   │   └── writeup/
│   ├── templates/
│   │   ├── about_us.html
│   │   ├── home.html
│   │   ├── index.html
│   │   ├── predictor.html
│   │   ├── tableau1.html
│   │   └── tableau2.html
│   ├── Alzheimers_model_pipeline.h5
│   ├── Alzheimers_model_pipeline.pkl
│   ├── app.py
│   └── modelHelper.py
├── Notebooks/
│   ├── Machine Learning.ipynb
│   ├── Predictions.ipynb
│   └── cleaned_data.ipynb
├── Project Documents/
│   ├── Project_4_Group_9_Presentation.pdf
│   ├── Project_4_Group_9_proposal.pdf
│   └── Project_4_Group_9_write_up.pdf
├── Resources/
│   ├── alzheimers_disease_data.csv
│   ├── cleaned_alzheimers_disease_data.csv
│   └── tableau_alzheimers_disease_data.csv
├── virtual_documents/
│   └── Resources/
│       └── cleaned_data.csv
├── .gitignore
├── License
├── Project_4_group_9_ReadMe.md

**Overview**

Alzheimer’s Disease is a progressive neurological disorder that affects memory, thinking, and behavior. As one of the most common forms of dementia, it impacts millions worldwide, making early diagnosis and understanding of risk factors essential.

This project uses a combination of **machine learning** and **data visualization** to identify patterns and risk factors that may influence the onset and progression of Alzheimer’s Disease. The [Alzheimer's Disease Prediction 🧠🔍📈](https://www.kaggle.com/code/adhamtarek147/alzheimer-s-disease-prediction) dataset from kaggle was used as our frame of reference in building the machine learning model and Tableau Dashboards.

---

**Project Objectives**

We sought to answer the following high-level questions:

1. What is the average age that Alzheimer's symptoms begin to appear?

2. Is there a correlation between ethnicity and a higher risk of Alzheimer's?

3. Do lifestyle factors influence Alzheimer’s risk?

---

**Data Visualization with Tableau**

Using Tableau, we created interactive charts to explore the data and uncover patterns. These included:

* Bubble and bar charts showing demographic influences (age, gender, ethnicity, family history)

* The number of diagnosis cases based on age.

* A comprehensive dashboard displaying memory complaints across a range of ages.

---

## **Data Cleaning**

Before analysis, extensive cleaning was performed:

* Loaded data into a Pandas DataFrame and assessed structure using .info()

* Removed irrelevant columns like “education level” or “doctor in charge”.

* Converted numeric binary fields into categorical Yes/No labels

* Mapped “Gender” and “Ethnicity” codes to generic terms. Eg. (0: male, 1: female)

---

**Machine Learning Models**

We tested four models to predict Alzheimer's diagnosis:

* Linear Regression

* Decision Tree

* Random Forest

* XGBoost

Each model was evaluated using common classification metrics (accuracy, AUC, and F1-score). Data was split into training and test sets, and preprocessed appropriately to ensure model validity.

---

**Limitations and Biases**

* Missing or incomplete data may have reduce model performance

* The dataset may not be representative across all ethnic or socioeconomic groups

* Diagnosis methods and healthcare access could vary by region, introducing systemic bias

---

 

**Conclusion**

Through the combination of machine learning and data visualization techniques, this project provided valuable insights into the factors contributing to Alzheimer's Disease. The machine learning models demonstrated the potential for predicting diagnoses, based on current symptoms and should be used as medical advice. Please refer to your healthcare provider. Meanwhile, Tableau visualizations helped uncover the complex relationships between age, gender, ethnicity, and family history in the context of Alzheimer's risk. These findings highlight the importance of genetic factors, socioeconomic conditions, and family history in understanding and predicting Alzheimer’s, offering promising avenues for future research and early intervention strategies. 

