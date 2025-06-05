from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Heatmap backend is running!"

@app.route('/generate_heatmap', methods=['POST'])
def generate_heatmap():
    file = request.files['video']
    # Save the video
    filename = "video.mp4"
    file.save(filename)
    
    # Placeholder for heatmap generation
    return jsonify({"message": "Heatmap received!"})

if __name__ == '__main__':
    app.run()
