from flask import Flask, request, jsonify, Response, url_for, render_template
import requests

app = Flask(__name__)
api = 'http://localhost:5001'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['GET'])
def generate():
    response = requests.get(api + '/get/animal')
    noise = requests.post(api + '/get/noise', response)
    return response + noise

if __name__=='__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
