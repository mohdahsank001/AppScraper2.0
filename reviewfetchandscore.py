"""
Created on Thu Aug  2 19:42:10 2021
@author: Mohammed Ahsan
-------------------------------------------------------
APP REVIEW SCRAPER - ioS and google Store. 
version : 1.0 
Build name : RedSparrow -----
-------------------------------------------------------
"""

from app_store_scraper import AppStore
from pprint import pprint
import json
from bson import json_util
import datetime
import csv
import sys
from datetime import datetime
from datetime import timedelta 

# ******* ! Instruction : INCASE OF Connection error fetching 0 reviews : use VPN to Change the IP address and run the code again. !  *******


print("******************************************* - WELCOME TO REVIEW AND SCORE FETCHER - ******************************************")
print("version 1.2")
print("Build name : REd Sparrow ------------------- ")
print("\n")
print("Created by Mohammed Ahsan kollathodi for SellCrowd under the Creative Common License., All rights reserved 2021.")
#print("\n")
print("******************************************************************************************************************************")
# CSV
print("\n")
print("INSTRUCTIONS: PASTE YOUR APP NAME INSIDE THE PARAMETER appname WITHIN THE CODE TO GET THE APP. REVIEWS.")
print("\n")

# Updated list to store all of the game names. 

updatedlist = [] 


# A new list to store all of the game names from the CSV File. 
results = []

# For each dictionary In the output JSON, the list to append the corresponding app-name 
appnames = [] 

# Final list 

finallist = []

# CONVERT THE FIELDS IN THE CSV INTO A NEW LIST called as results. 
# Add the app names as new rows into the testnames.csv file. The app names are the app id's for the scrapper. 
# testnames.csv consist of all the app names as new rows . 

# Name of the app. here. 

appname = "Gunship Battle Total Warfare"

output = AppStore(country="us", app_name=appname)
output.review(how_many=1000)
updatedlist.append(output.reviews) 


# Final list 
finallist = appnames + updatedlist 


# print the output. 
print("OUTPUT REVIEWS :")
print("\n")
print(updatedlist)
print("\n")
print("Reviews fetch Complete !!")
  

filename = appname+".json"


# Convert the UPDATED list  into JSON with format : APPNAME + reviews , each set of reviews would have the app-name at the beginning.  
with open(filename, 'w') as file : 
     file.write((json.dumps(output.reviews,default=json_util.default, indent=0, sort_keys= False)))


"""
Created on Thu Sep 7 19:42:10 2021
@author: Mohammed Ahsan
-------------------------------------------------------
Review score Fetcher
version : 1.0 
Build name : RedSparrow -----

The following script fetches all of the review scores 
of multiple reviews of apps. in the output JSON file and 
also produces the max. review score. 
-------------------------------------------------------
"""


file = open(filename, 'r')
data = json.load(file)    
reviewscores = [] 


fivestar = 0 
fourstar = 0 
threestar = 0 
twostar = 0 
onestar = 0 


for review in data : 
    reviewscores.append(review['rating'])


    if (review['rating']) == 5 : 
        fivestar = fivestar + 1 
    elif (review['rating']) == 4 : 
        fourstar = fourstar + 1 
    elif (review['rating']) == 3 : 
        threestar = threestar + 1 
    elif (review['rating']) == 2 : 
        twostar = twostar + 1 
    elif (review['rating']) == 1 : 
        onestar = onestar + 1

print("\n")
print("App-name:"+appname)
#print(reviewscores)
        

print("\n")
print("FIVE STARTS COUNT:")
print(fivestar)

print("\n")
print("FOUR STARS COUNT:")
print(fourstar)

print("\n")
print("THREE STARS COUNT:")
print(threestar)

print("\n")
print("TWO STARS COUNT:")
print(twostar)

print("\n")
print("ONE STAR COUNT:")
print(onestar)

# Total number of reviews
totalreviewcount = fivestar + fourstar + threestar + twostar + onestar

# The max review score from the set of review scores. 
print("\n")
print(":TOTAL REVIEW COUNT:")
print(totalreviewcount)
maxvalue = max(reviewscores)
print("\n")
print("THE MAX. REVIEW SCORE FOR THE app."+" "+appname+" "+"is as following :")
print((maxvalue))




