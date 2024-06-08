from morseapi import MorseRobot
import logging
import binascii

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize MorseRobot
bot = MorseRobot("C2:37:67:68:BD:38")

bot.reset()
bot.connect()
bot.say("hi")

def prompt_input():
    # Temporarily disable logging
    logging.disable(logging.CRITICAL)
    try:
        data = input("Enter command: ")
    finally:
        # Re-enable logging
        logging.disable(logging.NOTSET)
    return data

while True:
    try:
        data = prompt_input()
        if data == "exit":
            break
        exec(str(data))
    except Exception as e:
        print(e)
        break
