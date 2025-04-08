from flask import Flask, jsonify, request, render_template
from modelHelper import ModelHelper

# Create an Instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper()

#Route to render index.html template using data from Monga
@app.route("/")
def home():
    #Return template and data
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/predictions", methods=["POST"])
def predictions():
    content = request.json["data"]
    print(content)


    # parse
    age = int(content["age"])
    gender = int(content["gender"])
    ethnicity = int(content["ethnicity"])
    bmi = int(content["bmi"])
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
    confusion = int(content["confusion"])
    disorientation =  int(content["disorientation"])
    personality_changes =  int(content["personality_changes"])
    difficulty_completing_tasks =  int(content["difficulty_completing_tasks"])
    forgetfulness =  int(content["forgetfulness"])

    preds = modelHelper.predictions( age, gender, ethnicity, bmi, smoking, alcohol_consumtion, physical_activity, 
                diet_quality, sleep_quality, family_history_alzheimers, cardiovascular_disease, diabetes, depression,
                head_injury, hypertension, functional_assessment, memory_complaints, behavioral_problems, confusion, disorientation, personality_changes, difficulty_completing_tasks, forgetfulness)
    return(jsonify({"ok": True, "prediction": str(preds)}))


############################################################

# API ROUTES

@app.after_request
def add_header(r):
    """""
    Add headers to both force latest IE rendering engine or Chrome Frame,
    add also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

if __name__ == "__main__":

    app.run(debug=True, port = 8000)