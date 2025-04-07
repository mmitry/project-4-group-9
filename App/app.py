from flask import Flask, jsonify, request, render_template

# Create an Instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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
    return(jsonify({"ok": True}))

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



