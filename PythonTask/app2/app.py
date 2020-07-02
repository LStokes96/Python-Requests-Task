from flask import Flask, request, jsonify, Response, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['GET'])
def get_animal():
    return Response(mimetype='text/plain')


