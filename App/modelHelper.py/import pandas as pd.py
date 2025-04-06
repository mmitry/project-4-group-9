import pandas as pd
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        # model
        self.model = pickle.load(open("model_pipeline.pkl", 'rb'))

    def predictions(unnamed, patient_id, age, gender, bmi, smoking, alcohol_consumption, physical_activity, diet_quality,
              sleep_quality, family_history_alzheimers, cardiovascular_disease, diabetes, depression, head_injury, hypertension,
               functional_assessment, memory_complaints, behavioral_problems, confusion, disorientation, personality_changes, 
               difficulty_completting_tasks, forgetfulness):
        
        df = pd.DataFrame()
        df["Unnamed"] = [unnamed]
        df["PatientId"] = [patient_id]
        df["Age"] = [age]
        df["Gender"] = [gender]
        df["BMI"] = [bmi]
        df["Smoking"] = [smoking]
        df["AlcoholConsumption"] = [alcohol_consumption]
        df["PhysicalActivity"] = [physical_activity]
        df["DietQuality"] = [diet_quality]
        df["SleepQuality"] = [sleep_quality]
        df["FamilyHistoryAlzheimers"] = [family_history_alzheimers]
        df["CardiovascularDisease"] = [cardiovascular_disease]
        df["Diabetes"] = [diabetes]
        df["Depression"] = [depression]
        df["HeadInjury"] = [head_injury]
        df["Hypertension"] = [hypertension]
        df["FunctionalAssessment"] = [functional_assessment]
        df["MemoryComplaints"] = [memory_complaints]
        df["BehavioralProblems"] = [behavioral_problems]
        df["Confusion"] = [confusion]
        df["Disorientation"] = [disorientation]
        df["PersonalityChanges"] = [personality_changes]
        df["DifficultyComplettingTasks"] = [difficulty_completting_tasks]
        df["Forgetfulness"] = [forgetfulness]
        
        
        # columns in order
        df = df.loc[:, ['Unnamed', 'PatientID', 'Age', 'Gender',
        'BMI', 'Smoking', 'AlcoholConsumption',
        'PhysicalActivity', 'DietQuality',
        'SleepQuality', 'FamilyHistoryAlzheimers', 'CardiovascularDisease', 'Diabetes',
        'Depression', 'HeadInjury', 'Hypertension',
        'FunctionalAssessment', 'MemoryComplaints', 'BehavioralProblems',
        'Confusion', 'Disorientation', 'PersonalityChanges', 'DifficultyComplettingTasks', 'Forgetfulness']]
        
        #preds = self.model.predict_proba(df)
       # return(preds[0][1])