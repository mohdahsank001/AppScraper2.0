
AppScraper 2.0 
--------------------------------------------------------------
<img src="https://github.com/mhdahsan2000/AppScraper2.0/blob/master/appimage.png" alt="My cool logo"/>

```
img src - blog.appfigures.com

Version info : 
(latest update : v 2.0 , buildname: RedSparrow) 
```

# Quickstart
------------------

Install:
```console
pip3 install app-store-scraper
```

Scrape reviews for an app:
```python
from app_store_scraper import AppStore
from pprint import pprint

minecraft = AppStore(country="au", app_name="minecraft")
minecraft.review(how_many=20)

pprint(minecraft.reviews)
pprint(minecraft.reviews_count)
```

Scrape reviews for a podcast:
```python
from app_store_scraper import Podcast
from pprint import pprint

sysk = Podcast(country="au", app_name="stuff you should know")
sysk.review(how_many=20)

pprint(sysk.reviews)
pprint(sysk.reviews_count)
```

# Variables and functions
-------------------------

Let's continue from the code example used in [Quickstart](#quickstart).


## Instantiation
------------------------

There are two required and one positional parameters:

- `country` (required)
  - two-letter country code of [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) standard
- `app_name` (required)
  - name of an iOS application to fetch reviews for
  - also used by `search_id()` method to search for `app_id` internally
- `app_id` (positional)
  - can be passed directly
  - or ignored to be obtained by `search_id` method internally

Once instantiated, the object can be examined:
```pycon
>>> minecraft
AppStore(country='au', app_name='minecraft', app_id=479516143)
```
```pycon
>>> print(app)
     Country | au
        Name | minecraft
          ID | 479516143
         URL | https://apps.apple.com/au/app/minecraft/id479516143
Review count | 2k
```

Other optional parameters are:

- `log_format`
  - passed directly to `logging.basicConfig(format=log_format)`
  - default is `"%(asctime)s [%(levelname)s] %(name)s - %(message)s"`
- `log_level`
  - passed directly to `logging.basicConfig(level=log_level)`
  - default is `"INFO"`
- `log_interval`
  - log is produced every 5 seconds (by default) as a "heartbeat" (useful for a long scraping session)
  - default is `5`


## Fetching Review
-------------------------------------

The maximum number of reviews fetched per request is 20. To minimise the number of calls, the limit of 20 is hardcoded. This means the `review()` method will always grab more than the `how_many` argument supplied with an increment of 20.

```pycon
>>> minecraft.review(how_many=33)
>>> minecraft.reviews_count
40
```

If `how_many` is not provided, `review()` will terminate after *all* reviews are fetched.

**NOTE** the review count seen on the landing page differs from the actual number of reviews fetched. This is simply because only *some* users who rated the app also leave reviews.

### Optional Parameters
--------------------------------------

- `after`
  - a `datetime` object to filter older reviews
- `sleep`
  - an `int` to specify seconds to sleep between each call

## Review Data

The fetched review data are loaded in memory and live inside `reviews` attribute as a list of dict.
```pycon
>>> minecraft.reviews
[{'userName': 'someone', 'rating': 5, 'date': datetime.datetime(...
```

Each review dictionary has the following schema:
```python
{
    "date": datetime.datetime,
    "isEdited": bool,
    "rating": int,
    "review": str,
    "title": str,
    "userName": str
 }
```

## Extended functionality (Changelog for AppScraper v 2.0)
----------------------------------------------------------------------------------------------
```
- Scraped multiple apps. at the same time with the same ip. (In case, if the request gets blocked use VPN to switch IP)
- Import the app id's (app. names from the CSV instead of inputing it as a parameter to the funtion)
- Fetched reviews are produced as output - see file "OUTPUTFILEAPPS.txt"
- Use list to upload all the app-names to the scraper function simultaneously.

- Open folder "runfile" in the root folder (Edit these files if required)  : 

appstore.py - code to run fetch multiple entries 
OUTPUTFILEAPPS.txt - scraped data as a list produced in the .txt file. 
OUTPUTJSON.json - scraped data as output in the JSON file.(Each review is a seperate dictionary.)
testnames.csv - Input the app names as new fields or rows in the CSV in the first column. 
```

OUTPUTJSON.json dict. format for one review :
--------------------------------------- 
```
{
"date": {
"$date": 1607646221000
},
"title": "Fun way to play bingo!",
"rating": 5,
"review": "This is a neat way to play Bingo!  The faster you daub, the more credit you get.  I like the practice feature of this app.  Of course you can play for money, if you don\u2019t mind making a deposit. You can win trophies for playing. The challenge is to not daub the wrong number.  You will be penalized.  The people at Skilz are all for player happiness. I have played enough for a Skillz sticker.  And because my address was entered incompletely, they sent me two stickers. How cool is that?! I am still having such a great time playing bingo this what way. I played so much I am developing a raw  area on my right wrist. It challenges me to move faster which is good. One issue I have with the game itself is waiting for my opponents score. There seems to be some lag here and I have to wait or just choose to move on to another game. But I keep coming back. So I guess I\u2019m having a good time.\n\nI keep coming back\n\nAlthough the app itself seems to put a big dent in my battery usage, I still enjoy the bingo.  The number display is quite large. So, due to a vison impairment, I have an easy time reading them, although the font style does cause confusion between 6\u2019s and 8\u2019s.    It\u2019s not enough to deter me.  BINGO on!",
"isEdited": false,
"userName": "Nota happy farmer"
}
```


--------------------------------------------------------------------------------------------------





