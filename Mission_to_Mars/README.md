# Mission To Mars
<h1>Web-Scraping-Challenge:</h1>


## Description
The task of this assignment, was to build a web application that scrapes various websites for data related to the Mission to Mars and display the information in a single HTML page.
![image](https://github.com/hanniecodes/web-scraping-challenge/blob/main/Mission_to_Mars/images/Scraping%20webpage.jpg?raw=true)  
![image](https://github.com/hanniecodes/web-scraping-challenge/blob/main/Mission_to_Mars/images/scraping_hemispheres%20.jpg?raw=true)  

There were three parts to this assignment:
- [Scraping](#Scraping)
- [MongoDb](#MongoDb)
- [Flask Appliication/HTML](#FlaskAppliication/HTML)

## Scraping
I completed my initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. This had four parts: The Latest Mars News, Featured Mars Image, Mars Facts, And the Different Mars Hemispheres. 
<br>
<br>
<h3><b> The Latest Mars News  </b></h3>
Using the [Mars News Site](https://redplanetscience.com/), I scraped and collected the latest News Title and Paragraph Text and put them into two variables news_title and news_par.
![image](https://github.com/hanniecodes/web-scraping-challenge/blob/main/Mission_to_Mars/images/Mars%20news.jpg?raw=true)
<br>
<br>
<h3><b> Featured Mars Image </b></h3>
<br>
* Using the  [Mars Space Images website](https://spaceimages-mars.com) I used the  Splinter module to navigate the site and find the image URL for the current Featured Mars Image, and assigned the URL string to a variable called `featured_image_url` by combining what was scraped and the original URL. 


![image](https://github.com/hanniecodes/web-scraping-challenge/blob/main/Mission_to_Mars/images/featured%20image.jpg?raw=true)
<br>
<br>
<h3><b> Mars Facts </b></h3>
Using the [Mars Facts website](https://galaxyfacts-mars.com) and Pandas, I was able to scrape the table containing facts about the Earth and Mars and converted  the data to a HTML table string.
![image](https://github.com/hanniecodes/web-scraping-challenge/blob/main/Mission_to_Mars/images/mars%20facts.jpg?raw=true)
<br>
<br>
<h3><b> Mars Hemispheres </b></h3>
Using the [astrogeology site](https://marshemispheres.com/), I obtained high-resolution images for each hemisphere of Mars by creating a For loop that captured both the image and the title. I stored them in the img_url and title variables. 

![image](https://github.com/hanniecodes/web-scraping-challenge/blob/main/Mission_to_Mars/images/hemispheres.jpg?raw=true)
<br>
<br>
<br>

## MongoDb

## FlaskAppliication/HTML