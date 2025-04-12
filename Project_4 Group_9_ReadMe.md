**Alzheimer's Disease Prediction and Visualization Project**

**Project Structure:**  
Project-4-group-9/  
├── App3/  
│   ├── static/  
│   │   ├── css/  
│   │   │   └── style.css  
│   │   ├── js/  
│   │   │   ├── logic.js  
│   │   │   ├── tableau\_ap1.js  
│   │   │   └── tableau\_ap2.js  
│   │   └── writeup/  
│   ├── templates/  
│   │   ├── about\_us.html  
│   │   ├── home.html  
│   │   ├── index.html  
│   │   ├── predictor.html  
│   │   ├── tableau1.html  
│   │   └── tableau2.html  
│   ├── Alzheimers\_model\_pipeline.h5  
│   ├── Alzheimers\_model\_pipeline.pkl  
│   ├── app.py  
│   └── modelHelper.py  
├── Notebooks/  
│   ├── Machine Learning.ipynb  
│   ├── Predictions.ipynb  
│   └── cleaned\_data.ipynb  
├── Project Documents/  
│   ├── Project\_4\_Group\_9\_Presentation.pdf  
│   ├── Project\_4\_Group\_9\_proposal.pdf  
│   └── Project\_4\_Group\_9\_write\_up.pdf  
├── Resources/  
│   ├── alzheimers\_disease\_data.csv  
│   ├── cleaned\_alzheimers\_disease\_data.csv  
│   └── tableau\_alzheimers\_disease\_data.csv  
├── virtual\_documents/  
│   └── Resources/  
│       └── cleaned\_data.csv  
├── .gitignore

**Overview**

Alzheimer’s Disease is a progressive neurological disorder that affects memory, thinking, and behavior. As one of the most common forms of dementia, it impacts millions worldwide, making early diagnosis and understanding of risk factors essential.

This project uses a combination of **machine learning** and **data visualization** to identify patterns and risk factors that may influence the onset and progression of Alzheimer’s Disease. The [Alzheimer's Disease Prediction 🧠🔍📈](https://www.kaggle.com/code/adhamtarek147/alzheimer-s-disease-prediction) Dataset from kaggle was used as our frame of reference in building the machine learning model.

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

* Visualizations examining symptoms and comorbidities like sleep issues, memory complaints, and depression

* A comprehensive dashboard displaying illness and symptom breakdowns across different age groups and ethnicities

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

Each model was evaluated using common classification metrics (accuracy, precision, recall, F1-score). Data was split into training and test sets, scaled, and preprocessed appropriately to ensure model validity.

---

**Limitations and Biases**

* Missing or incomplete data may reduce model performance

* The dataset may not be representative across all ethnic or socioeconomic groups

* Diagnosis methods and healthcare access could vary by region, introducing systemic bias

---

 

**Conclusion**

Through the combination of machine learning and data visualization techniques, this project provided valuable insights into the factors contributing to Alzheimer's Disease. The machine learning models demonstrated the potential for predicting diagnoses, while Tableau visualizations helped uncover the complex relationships between age, gender, ethnicity, and family history in the context of Alzheimer's risk. These findings highlight the importance of genetic factors, socioeconomic conditions, and family history in understanding and predicting Alzheimer’s, offering promising avenues for future research and early intervention strategies. 

