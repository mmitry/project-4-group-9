from flask import Flask, jsonify, render_template, request, redirect
import pandas as pd
import numpy as np
#from modelHelper import ModelHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#modelHelper = ModelHelper()

#################################################
# Flask Routes
#################################################

# HTML ROUTES - HOME
@app.route("/home")
def home():
    return render_template("home.html")

# HTML ROUTES - TABLEAU1
@app.route("/tableau1")
def tableau1():
    return render_template("tableau1.html")

# HTML ROUTES - TABLEAU2
@app.route("/tableau2")
def tableau2():
    return render_template("tableau2.html")

# HTML ROUTES - MODEL
@app.route("/model")
def model():
    return render_template("index.html")

# HTML ROUTES - REPORT
@app.route("/report")
def report():
    return render_template("report.html")

# HTML ROUTES - ABOUT US 
@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

# HTML ROUTES - SOURCES
@app.route("/sources")
def sources():
    return render_template("sources.html")

@app.route("/predictions", methods=["POST"])
def predictions():
    content = request.json["data"]
    print(content)

    # parse
    unnamed = content["unnamed"]
    patient_id = content["patient_id"]
    age = float(content["age"])
    gender = content["gender"]
    ethnicity = content["ethnicity"]
    bmi = content["bmi"]
    smoking = int(content["smoking"])
    alcohol_consumtion = int(content["alcohol_consumption"])
    physical_activity = int(content["physical_activity"])
    diet_quality = int(content["diet_quality"])
    sleep_quality = int(content["sleep_quality"])
    family_history_alzheimers = int(content["family_history_alzheimers"])
    cardiovascular_disease = int(content["cardiovascular_disease"])
    diabetes = int(content["diabetes"])
    depression = int(content["depression"])
    head_injury = int(content["head_injury"])
    hypertension = int(content["hypertension"])
    functional_assessment = int(content["functional_assessment"])
    memory_complaints = int(content["memory_complaints"])
    behavioral_problems = int(content["behavioral_problems"])
    confusion = content["confusion"]
    disorientation =  content["disorientation"]
    personality_changes =  content["personality_changes"]
    difficulty_completing_tasks =  content["difficulty_completing_tasks"]
    forgetfulness =  content["forgetfulness"]

    #preds = modelHelper.predictions(unnamed, patient_id, age, gender, ethnicity, bmi, smoking, alcohol_consumtion,
               #physical_activity, diet_quality, sleep_quality, family_history_alzheimers, cardiovascular_disease, diabetes, depression,
               #head_injury, hypertension, functional_assessment, memory_complaints, behavioral_problems, confusion, disorientation, personality_changes, difficulty_completing_tasks, forgetfulness)

    #return(jsonify({"ok": True, "prediction": str(preds)}))

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

# Run the App
if __name__ == '__main__':
    app.run(debug=True)