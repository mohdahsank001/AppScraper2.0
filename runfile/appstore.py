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


# CSV 

# Updated list to store all of the game names. 
updatedlist = [] 


# A new list to store all of the game names from the CSV File. 
results = []

# CONVERT THE FIELDS IN THE CSV INTO A NEW LIST called as results. 
# Add the app names as new rows into the testnames.csv file. The app names are the app id's for the scrapper. 
# testnames.csv consist of all the app names as new rows . 

with open('testnames.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(row[0])


# USE  list incase if the reading from csv is unsuccessfull. 
# The list of app names that we would want the reviews of .
#appnames = ["monopoly"]
#appnames = ["monopoly","Fidget Toys Trading 3D","Flow Free","Two Dots","Blackout Bingo - Bingo Game","Pull the Pin","Parking Jam 3D","Adorable Home"," Match 3D"," Terraforming Mars","The Game of Life 2","Jigsaw Puzzle","Coin Pusher - Lucky Dozer Game"]


# List of app. names the reviews to. 
# Iterate through the results list to fetch the reviews of all of the apps - list with field names from CSV. 

for i in results :
               output = AppStore(country="us", app_name=i)
               output.review(how_many=5)
               updatedlist.append(output.reviews)


# print the output. 
print(updatedlist)


# write the reviews to a text file as output. 
with open('OUTPUTFILEAPPS.txt', 'w', encoding='utf-8') as f:
     f.write(str(updatedlist))


# Convert the Scraped data into JSON. 
with open("OUTPUTJSON.json", 'w') as file : 
     file.write((json.dumps(output.reviews,default=json_util.default, indent=0, sort_keys= False)))



# TESTING. 

"""
# Fetch the App using country name and app name
output = AppStore(country="us", app_name="Fidget Toys Trading 3D")

# Count of how many reviews 
output.review(how_many=10000)

# updated list to store the reviews.
updatedlist = []

# Add the reviews to the list 
updatedlist.append(output.reviews)


# Write the Output into a TEXT file. 
with open('APPREVIEWS.txt', 'w', encoding='utf-8') as f:
     f.write(str(updatedlist))


# Convert the list to JSON. 

print(updatedlist)
print(type(updatedlist))
#pprint(monopoly.reviews)
#pprint(monopoly.reviews_count)

"""


# CSV_2
"""
# iterate through the list to fetch the reviews of all of the apps. in the appnames list. 

or i in lists_from_csv :
               output = AppStore(country="us", app_name=i)
               output.review(how_many=20)f
               updatedlist.append(output.reviews)

"""

