from flask import Flask, jsonify, request
from morseapi import MorseRobot
from time import sleep
import logging
import ast
import re

app = Flask(__name__)

bot = None
bot_address = "C2:37:67:68:BD:38"

def get_robot():
    global bot
    if bot is None:
        bot = MorseRobot(bot_address)
    return bot

@app.route('/connect')
def connect():
    print("connect!")
    global bot
    try:
        if bot is None:
            bot = MorseRobot(bot_address)
        bot.connect()
        bot.reset()
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
    global bot
    try:
        if bot is not None:
            bot.disconnect() # Method must be trash
            bot = None
            return jsonify({"status": "disconnected"})
    except:
        return jsonify({"error": "Failed to disconnect"}), 500

@app.route('/forward')
def drive():
    print("forward")
    try:
        if bot is None:
            return jsonify({"error": "Robot not connected"}), 400
        bot.move(500)
        return jsonify({"status": "moved forward"})
    except:
        return jsonify({"error": "Failed to move"}), 500

@app.route('/right')
def right():
    print("right")
    try:
        if bot is None:
            return jsonify({"error": "Robot not connected"}), 400
        bot.turn(-90)
        return jsonify({"status": "moved forward"})
    except:
        return jsonify({"error": "Failed to move"}), 500

@app.route('/left')
def left():
    print("left")
    try:
        if bot is None:
            return jsonify({"error": "Robot not connected"}), 400
        bot.turn(90)
        return jsonify({"status": "moved forward"})
    except:
        return jsonify({"error": "Failed to move"}), 500

@app.route('/back')
def back():
    print("back")
    try:
        if bot is None:
            return jsonify({"error": "Robot not connected"}), 400
        bot.move(-300)
        return jsonify({"status": "moved forward"})
    except:
        return jsonify({"error": "Failed to move"}), 500


@app.route('/llama', methods=['POST'])
def llama():
    data = request.get_json()
    print("data:")
    print(data)

    command = data.get(u"command")
    print("COMMAND:")
    print(command)
    try:

        #command_list = ast.literal_eval(command)
        command_list = re.findall(r'\[([^]]+)\]', command)[0].split(', ')
        print("Parsed Command List:")
        print(command_list)

        for item in command_list:
            print(item)
            eval(item)
            sleep(1)
        # command_list = eval(command)
        # print("Parsed Command List:")
        # print(command_list)

        # for item in command_list:

    
        #     if bot is None:
        #         return jsonify({"error": "Robot not connected"}), 400
        #     print(item)
        #     print(" I PRINTED THE ITEM ^")
        #     sleep(1)

        #exec(command)
        return jsonify({"status": "Executed command " + command})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Failed to execute command: " + str(e)})
    #return jsonify({"backAtYa": data})
    
    #command = data.get("command")
    #print("Command: " + command)
    
    # try:
    #     if bot is None:
    #         return jsonify({"error": "Robot not connected"}), 400
        
    #     # Ensure the command is properly prefixed with 'await'
    #     full_command = "await " + command
    #     print("Full command: " + full_command)
        # # Use exec to execute the await command in an async function
        # local_vars  = { 'bot' : bot }
        # exec("async def __temp_func():\n    " + full_command, globals(), local_vars)
        # local_vars['__temp_func']()
        
        # return jsonify({"status": "Executed command " + command})
    # except Exception as e:
    #     print("Error:", str(e))
    #     return jsonify({"error": "Failed to execute command: " + str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)