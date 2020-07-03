from flask import Flask, request, jsonify, Response
import random


app = Flask(__name__)

@app.route('/get/animal', methods=['GET'])
def animal():
    animals = ["Dog", "Cat", "Mouse", "Whale"]
    send = animals[random.randrange(4)]
    return Response(send, minetype='text/plain')

@app.route('/get/noise', methods=['POST'])
def noise():
    animal = request.data.decode("utf-8")
    noise = {"Dog": "Bark", "Cat": "Meow", "Mouse": "Squeak", "Whale": "WOOOOOOAAAAAAOOOOOLLLLLEEEEEE"}
    animal_noise = noise[animal]
    return Response(animal_noise, minetype='text/plain')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
