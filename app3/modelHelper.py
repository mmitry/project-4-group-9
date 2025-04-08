import pandas as pd
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def predictions(self, age, gender, ethnicity, bmi, smoking, alcohol_consumption, physical_activity, 
                diet_quality, sleep_quality, family_history_alzheimers, cardiovascular_disease, diabetes, depression,
                head_injury, hypertension, functional_assessment, memory_complaints, behavioral_problems, confusion, disorientation, personality_changes, difficulty_completing_tasks, forgetfulness):
        
        df = pd.DataFrame()
        df["Age"] = [age]
        df["Gender"] = [gender]
        df["Ethnicity"] = [ethnicity]
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
        df["DifficultyCompletingTasks"] = [difficulty_completing_tasks]
        df["Forgetfulness"] = [forgetfulness]
        
        #Load model
        model = pickle.load(open("Alzheimers_model_pipeline.pkl", 'rb'))
        
        # columns in order
        df = df.loc[:,['Age', 'Gender', 'Ethnicity',
        'BMI', 'Smoking', 'AlcoholConsumption',
        'PhysicalActivity', 'DietQuality',
        'SleepQuality', 'FamilyHistoryAlzheimers', 'CardiovascularDisease', 'Diabetes',
        'Depression', 'HeadInjury', 'Hypertension',
        'FunctionalAssessment', 'MemoryComplaints', 'BehavioralProblems',
        'Confusion', 'Disorientation', 'PersonalityChanges', 'DifficultyCompletingTasks', 'Forgetfulness'
        
        ]]
        
        preds = model.predict_proba(df)
        Positive = preds[0][1]
        return(Positive)