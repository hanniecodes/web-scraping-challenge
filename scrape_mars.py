# Dependencies
from splinter import Browser, browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests


    
def scrape(): 
    mars_data={}
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    # Mars news
    mars_url = 'https://redplanetscience.com/'
    browser.visit(mars_url)
    # Scrape page into Soup
    html = browser.html
    mars_soup = BeautifulSoup(html, "html.parser")
    news_title= mars_soup.find_all('div', class_='content_title')[0].text 
    news_date= mars_soup.find_all('div', class_='list_date')[0].text 
    news_par= mars_soup.find_all('div', class_='article_teaser_body')[0].text

    # Mars Image
    jpl_url = 'https://spaceimages-mars.com/'
    browser.visit(jpl_url)
    html = browser.html
    img_soup = BeautifulSoup(html, "html.parser")
    relative_image_path=img_soup.find_all('img', class_='headerimage fade-in')[0]["src"]
    featured_image_url= (f'{jpl_url}{relative_image_path}')

    # tables
    facts_url = 'https://galaxyfacts-mars.com'
    browser.visit(facts_url)
    html = browser.html
    facts_soup = BeautifulSoup(html, "html.parser")
    tables = pd.read_html(facts_url)
    mars_facts=tables[0]
    mars_facts.columns= ["Mars - Earth CompYes arison","Mars","Earth"]
    mars_facts.drop(index=mars_facts.index[0], axis=0,inplace=True)
    mars_facts.set_index('Mars - Earth Comparison')
    facts_html=mars_facts.to_html()
    facts_html.replace('\n','')

    # hemispheres
    hemi_url = 'https://marshemispheres.com/'
    browser.visit(hemi_url)
    html = browser.html
    hemi_soup = BeautifulSoup(html, "html.parser")
    mars_hemi=hemi_soup.find_all('div', class_='item')
    hemi_href=[]
    for row in mars_hemi:
        hemi_href.append(hemi_url+ (row.find('a', class_='itemLink product-item')['href']))
    # Create empty list
    hemi_img_urls = []
    # for loop to get title and image link
    for url in hemi_href:
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h2', class_ = 'title').text
        par_url=soup.find('img', class_ = 'wide-image')['src']
        img_url = hemi_url + par_url
        hemi_img_urls.append({'title': title, 'img_url': img_url})

    mars_data = {
        "News Title": news_title,
        "News Paragraph":news_par,
        "News Date":news_date,
        "Featured Image URL": featured_image_url, 
        "Mars Facts":facts_html, 
        "Mars Hemispheres": hemi_img_urls

    }
    return mars_data
