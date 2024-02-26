from flask import Flask, jsonify
from morseapi import MorseRobot
import logging


app = Flask(__name__)

robot = None
bot_address = "C2:37:67:68:BD:38"

def get_robot():
    global robot
    if robot is None:
        robot = MorseRobot(bot_address)
    return robot

@app.route('/connect')
def connect():
    print("connect!")
    global robot
    try:
        if robot is None:
            robot = MorseRobot(bot_address)
        robot.connect()
        robot.reset()
        return jsonify({"status": "connected"})
    except:
        return jsonify({"error": "Failed to connect"}), 500

'''
INFO:werkzeug:127.0.0.1 - - [25/Feb/2024 18:56:00] "GET /disconnect HTTP/1.1" 500 -
'''
# broken

@app.route('/disconnect')
def disconnect():
    print("disconnect!")
    global robot
    try:
        if robot is not None:
            robot.disconnect() # Method must be trash
            robot = None
            return jsonify({"status": "disconnected"})
    except:
        return jsonify({"error": "Failed to disconnect"}), 500

@app.route('/forward')
def drive():
    print("forward")
    try:
        if robot is None:
            return jsonify({"error": "Robot not connected"}), 400
        robot.move(500)
        return jsonify({"status": "moved forward"})
    except:
        return jsonify({"error": "Failed to move"}), 500

@app.route('/right')
def right():
    print("right")
    try:
        if robot is None:
            return jsonify({"error": "Robot not connected"}), 400
        robot.turn(-90)
        return jsonify({"status": "moved forward"})
    except:
        return jsonify({"error": "Failed to move"}), 500

@app.route('/left')
def left():
    print("left")
    try:
        if robot is None:
            return jsonify({"error": "Robot not connected"}), 400
        robot.turn(90)
        return jsonify({"status": "moved forward"})
    except:
        return jsonify({"error": "Failed to move"}), 500

@app.route('/back')
def back():
    print("back")
    try:
        if robot is None:
            return jsonify({"error": "Robot not connected"}), 400
        robot.move(-300)
        return jsonify({"status": "moved forward"})
    except:
        return jsonify({"error": "Failed to move"}), 500

if __name__ == '__main__':
    app.run(port=5555, debug=True)
