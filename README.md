# Stock Data Scraper
_A Python program which can scrap stock technical data from Yahoo Finance. This is part 1 of a **three-part python program series** where I teach how to create a stock screener from scratch. This is part 1 and it focuses on acquiring the technicals you're interested in screening._


# Part 1- Scraping Data
## Getting Started

These instructions will get you a copy of this project up and running on your local machine for development and testing purposes. You can play around with the stocks and indicators to capture the information you want to screen. This is part 1 of the **three-part python program series** and focuses on scraping stock data off of Yahoo Finance.


### Prerequisites

This program utilizes a few packages to successfully scrape data. To run this program, install the following packages with the instructions below. 
_Note: Open the command terminal, navigate to the project directory and then run the commands mentioned below-_

#### Time
A python module which provides various time related functionalities. More information can be found [here](https://docs.python.org/3/library/time.html "Time Official Documentation")
```
On Windows-

  pip install time
  
On Mac-
  
  sudo pip install time

```

#### BeautifulSoup4
A python module used to pull data out of HTML and XML files. More information can be found [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/ "BeautifulSoup4 Official Documentation")
```
On Windows-

  pip install BeautifulSoup4
  
On Mac-
  
  sudo pip install BeautifulSoup4

```

## Running the program
Once you have the dependencies mentioned above installed, you should be good to run the program. In order to do so, open the command terminal, navigate to the project folder and use the following command-

```
  python stock_scraper.py
```


<hr></hr>


# Part 2- Storing Data
## Getting Started

This is part 2 of the **three-part python program series** and focuses on storing the scraped data locally for screening.


### Prerequisites

You must install **Pandas** and **Numpy** on your system before proceeding with this part. 

## Running the program
Once you have the dependencies mentioned above installed, you should be good to run the program. In order to do so, open the command terminal, navigate to the project folder and use the following command-

```
  python get_data.py
```

## Modifications
If you explore the program you'll find a few key ways to manipulate the data storage pipeline. In specific, you can change the list of companies to store information about and also the actual indicators that are being stored. In order to do so, modify the ```stock_list``` and ```interested``` variables in the main function inside get_data.py.


<hr></hr>


# Part 3- Screening Data
Coming Soon!


<hr></hr>

## Further Resources
If you want to continue on with this series, feel free to [check out the Medium post](https://www.google.com "Building a stock screener from scratch"). You can also check out my other projects [here](https://www.harshrana.com "Harsh Rana")
