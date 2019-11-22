import cv2
import numpy as np
import pyautogui
import time
import threading
import random
import discord
from discord.ext.commands import Bot


PREFIX = '!'
client = Bot(command_prefix = PREFIX)
TOKEN = 'CHANGE FOR YOUR OWN BOT'




#Looks for the dota 2 accept button every 5 seconds
#if it finds it, it will log, move the cursor and accept for the user


def acceptQueue():
	print('checking')
	randomDouble = random.uniform(0.1,1)
	print(randomDouble)
	threading.Timer(5.0,acceptQueue).start()
	acceptLocation = pyautogui.locateCenterOnScreen('accept.png', grayscale = False)
	if acceptLocation is not None:
		pyautogui.moveTo(acceptLocation[0], acceptLocation[1], randomDouble)
		print('game found')
		pyautogui.click(button='left')



def main():
	acceptQueue()
	client.run(TOKEN)
	#notify()

main()
