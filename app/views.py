from flask import Flask,render_template,request,redirect,url_for,send_from_directory,abort
from app import pythonparse
from pythonparse import pythonparse
from app import app
import os

@app.route('/')
def openpage():
    return 'hello'

app.config["IMAGE_UPLOADS"]='\\app\\app\\static\\uploads'
@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":

        image = request.files["fileToUpload"]

        
        image.save(os.path.join(app.config["IMAGE_UPLOADS"],image.filename))
        print("file saved",image)
        c = send_from_directory(app.config["IMAGE_UPLOADS"],filename=image.filename,as_attachment =True)
        print(os.path.join(app.config["IMAGE_UPLOADS"],image.filename))
        d = pythonparse(os.path.join(app.config["IMAGE_UPLOADS"],image.filename))
        print(d)
        return render_template("result.html",a=d)
    else:
        return render_template("base.html")

@app.route("/result")
def parse():
    print("hi")
    return "hello"   