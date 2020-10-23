#!/usr/bin/env python
import sys
import os
from twython import Twython

#gets the keys from the os environment
CONSUMER_KEY = str(os.environ['frogAPI'])
CONSUMER_SECRET = str(os.environ['frogSecretAPI'])
ACCESS_KEY = str(os.environ['frogAccess'])
ACCESS_SECRET = str(os.environ['frogSecretAccess'])

#intializes twython object that will be used to make the tweet later on

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
#########
#get the name of the pic that will be posted

#opens the text file and fills an array with each element being the name of a pic
#saves the name of the first pic name in the file without the new line
#adds the rest of the file location to pic name

mylines = []
with open("/home/pi/Documents/frogBot/listOfPicNames.txt", "r+") as myfile:
    for myline in myfile:
        mylines.append(myline)
myfile.close()
selected = mylines[0]
selectedFull = "/home/pi/Documents/frogBot/pics/" + mylines[0].strip('\n')
##########
#deletes line in file

#refills the file with all the names that werent used
#this file is the same as what we started with minus the first line
#eventually, this file will become and we need to be manually reset
#the file was made using the terminal command "ls pics > listOfPicNames.txt"

with open("/home/pi/Documents/frogBot/listOfPicNames.txt", "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i != selected:
            f.write(i)
    f.truncate()
f.close()


########
#send tweet

#see twython documentation

pic = open(selectedFull, 'rb')
repsonse = twitter.upload_media(media=pic)

twitter.update_status(status='ribbit #frog',media_ids=[repsonse['media_id']])

#this code needs to be optimized when it comes to deleting the used pic name
#rebuilding the whole text file every time it tweets is very bad
#however I made this very late at night and havent had the time to sit down and produce a better solution
#for now, the code works and the twitter account is up.
