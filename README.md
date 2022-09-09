# 🎬Top 100 Movies Web Scraping using BeautifulSoup of Python

🌟A program which makes use of Web Scraping to get the real-time data of titles of the top 100 movies of all time from website using the BeautifulSoup package of Python.

👉In the 'main.py' file, the requests module is used to get the hard coded html data from the website(https://web.archive.org/web/20211226090047/https://www.empireonline.com/movies/features/best-movies-2/) 
and the response data is then stored in the python variable.

![Top 100 movies Website](https://github.com/bellaryyash23/100_Movies_Web_scrapping/blob/master/movie_web.png?raw=true)

👆Top 100 Movies Website👆

👉Next the BeautifulSoup Object is called to parse the stored html data for implementing web screaping.

👉In order to get the list of titles of the movies from this data we need to use the BeautifulSoup method '.find_all()' which takes the html tag name and other parameters
as arguments and returns the HTML tag in its entirety. 

👉For us to extract the text from the acquired HTML tag we use the '.get_text()' method which returns just the text i.e. the title of the movie tag.

👉This all data is then appended to a text file which is stored locally, allowing the user to view and edit and track their viewing list.

![Web Scraped list of top 100 movies in Text file](https://github.com/bellaryyash23/100_Movies_Web_scrapping/blob/master/movie_list.JPG?raw=true)

👆Web Scraped list of Top 100 movies stored in a Text file👆
