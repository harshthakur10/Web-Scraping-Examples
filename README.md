# IMDb and Wikipedia Scraping

This repository contains Python scripts for web scraping IMDb's top movies list and extracting data from Wikipedia's list of U.S. states and territories.

## Prerequisites

Before running the scripts, ensure you have Python installed on your machine. Additionally, you need to install the following Python libraries:

- requests
- BeautifulSoup4
- pandas


# Points to Remember(For code) :

* Web Scraping: The process of extracting data from websites.
* Python: The programming language used to write the scripts.
* IMDb: The Internet Movie Database, from which movie data is scraped.
* Wikipedia: The online encyclopedia, from which U.S. states and territories data is scraped.
* Data Extraction: The process of retrieving structured data from various sources.
* BeautifulSoup: A Python library used for web scraping.
* Requests: A Python library used for making HTTP requests.
* Pandas: A Python library used for data manipulation and analysis.
* Top Movies: Refers to the list of top-rated movies on IMDb.
* U.S. States: Refers to the states of the United States of America.
* Territories: Refers to the territories of the United States.
* Population Data: Refers to demographic information such as the population of states and territories.

# *IMDb Top Movies Scraping*

The script imdb_top_movies.py scrapes IMDb's top movies list and extracts movie titles.


**Functionality**

* Sends a GET request to IMDb's Top Movies page.

* Parses the HTML content using BeautifulSoup.

* Extracts movie titles from the parsed content.


**Performance**

The script is lightweight and should execute quickly, as it only extracts text data from a single web page(Static web page).



# *Wikipedia U.S. States and Territories Data Scraping*

The script us_states_population.py scrapes Wikipedia's page listing U.S. states and territories. It extracts state names and population data.


**Functionality**

* Sends a GET request to Wikipedia's page listing U.S. states and territories.

* Parses the HTML content using BeautifulSoup.

* Extracts state names and population data from the table.


**Performance**

Performance may vary depending on the size of the table and the complexity of the HTML structure.

The script should handle moderate-sized tables efficiently, but performance may degrade with extremely large tables.
