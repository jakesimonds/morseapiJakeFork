from morseapi import MorseRobot
import logging
import binascii

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
bot = MorseRobot("C2:37:67:68:BD:38")

bot.reset()
bot.connect()
bot.say("hi")

while True:
    try:
        data = input("Enter command: ")
        if data == "exit":
            break
        exec(data)
    except Exception as e:
        print(e)
        break