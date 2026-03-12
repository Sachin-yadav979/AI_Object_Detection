from flask import Flask, render_template
import cv2
from ultralytics import YOLO

app = Flask(__name__)

model = YOLO("yolov8n.pt")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()