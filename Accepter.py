import cv2
import numpy as np
import pyautogui
import time
import threading
import random
import discord
from discord.ext.commands import Bot

#DOTA SLAVE TOKEN
#NDYxNzY1Mzk3NjQxODIyMjA4.DhYEDw.fTTrsODDTBWfndMhsPnTCH5CsWo
PREFIX = '!'
client = Bot(command_prefix = PREFIX)
TOKEN = 'NDYxNzY1Mzk3NjQxODIyMjA4.DhYEDw.fTTrsODDTBWfndMhsPnTCH5CsWo'




#Looks for the dota 2 accept button every 5 seconds
#if it finds it, it will log, move the cursor and accept for the user
#has a random number generator for spite purposes


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


#Going to use discord api in python that will send a Private message
#to a user after they enter in their specified user, i will have to think
#more about how this would work since we can't have one bot per person
#:thinking:
#regardless just a thought, cheaper than twilio and we can run the bot
#on the raspberry pi
#THIS FUNCTION IS NOT FINISHED YET, STILL IN DEV

@client.command()
async def notify():
	print('in notify')
	test = 'bothehobo#3312'
	await client.send_message(test, 'jeff')

def main():
	acceptQueue()
	client.run(TOKEN)
	#notify()

main()
