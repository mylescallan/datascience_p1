



# AirBnB - A Sentiment Analysis

## Data
The source of the data is [kaggle.com](kaggle.com). The data used in this analysis is for two cities: [Boston](https://www.kaggle.com/airbnb/boston) and  [Seattle](https://www.kaggle.com/airbnb/seattle/data)

The data files are for _calendar_, _reviews_ and _listings_. The listings datafile contains one observation per listings, with information related to: Basic information (location, space, host, images (of listing and host), availability), Reviews, and Price. The calendar and reviews datafiles contain multiple entries per listing relating to individual availability data and reviews.



<span style='font-size:16.0pt;color:black;font-family:"Times New Roman";'>Where the data relates to  7403 unique listings.
The listings data contains information on those unique lists for 98 variables. The calendar data contains 8 
variables, with 2702460 observations (multiple observations per listing). And the reviews data contains 10 variables with
153124 observations</span>



<span style='font-size:16.0pt;color:black;font-family:"Times New Roman";'>The earliest date included in the reviews data is 03-21-09 
and the lastest is 09-06-16 (and the relevant dates for listsings are 
01-04-16 
to 09-07-16)</span>



<span style='font-size:16.0pt;color:black;font-family:"Times New Roman";'>There are 1383 listings that are not included in the reviews data. That is 18.68%.
This matches the missing reviews from the listings dataframe (i.e. where Number of Listings is zero): 1383</span>


# Files

- readme file
  - README.md
    - This file
- map files
  - boston_map.png
  - boston_zip_map.png
  - seattle_map.png
  - seattle_zip_map.png
    - Image files of maps of the regions analyzed
    - Created from screenshots of OpenStreetMaps
    - Bounding boxes for maps are either the min-max lat/lon for each listing or by zip code
 - css
   - Directory of CSS files
- data
  - Directory containing data
- helper_files
  - Directory of helper python files
- p1_blog_airBnB.html
  - HTML page of blog - made from Jupyter Notebook
- p1_blog_airBnB.ipynb
  - Jupyter Notebook (contains all analysis)
- p1_blog_airBnB_files
  - Directory of image files generated by Jupyter Notebook
- pickles files
  - sentiments_False_False.pickle
  - sentiments_False_True.pickle
  - sentiments_city_False.pickle
  - sentiments_city_True.pickle
  - sentiments_city_merge_False.pickle
  - sentiments_city_merge_True.pickle
  - sentiments_is_English_rows.pickle
  - sentiments_listing_id_False.pickle
  - sentiments_listing_id_True.pickle
    - To regenerate the sentiment analysis takes about 1 hour
    - To avoid redoing that analysis, the results are saved in pickle files
    - These pickle files are loaded automatically, unless otherwise specified when instantiating the `SentimentsWordCloud()` class _(which is done by using _update=True_)
    
- Modules

- file management
  - os
  - glob
- plotting
  - matplotlib.pyplot
  - seaborn
- language processing
  - fasttext
    - To extract english text
  - nltk.sentiment.vader method SentimentIntensityAnalyzer
    - To extract sentiments (postive, neutral, negative)
  - wordcloud methods WordCloud, STOPWORDS, ImageColorGenerator
    - To plot sentiments in word clouds

# Analysis

## Questions

For anyone new to AirBnB _(like me)_, the most obvious questions relate to:
- Locaton: If I want to avail of this service, what choices do I have in terms of location?
- Price: Compared to getting a hotel, is this service affordable?
- Reviews: What am I getting for the price that I pay? Is is a quality service?

