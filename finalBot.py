#!/usr/bin/env python
import sys
import os
from twython import Twython

CONSUMER_KEY = str(os.environ['frogAPI'])
CONSUMER_SECRET = str(os.environ['frogSecretAPI'])
ACCESS_KEY = str(os.environ['frogAccess'])
ACCESS_SECRET = str(os.environ['frogSecretAccess'])


twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
#########
#get pics
mylines = []
with open("/home/pi/Documents/frogBot/listOfPicNames.txt", "r+") as myfile:
    for myline in myfile:
        mylines.append(myline)
myfile.close()
selected = mylines[0]
selectedFull = "/home/pi/Documents/frogBot/pics/" + mylines[0].strip('\n')
##########
#deletes line in file
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
pic = open(selectedFull, 'rb')
repsonse = twitter.upload_media(media=pic)

twitter.update_status(status='ribbit #frog',media_ids=[repsonse['media_id']])
