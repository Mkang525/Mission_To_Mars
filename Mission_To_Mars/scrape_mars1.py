#!/usr/bin/env python
# coding: utf-8

# In[2]:


from splinter import Browser
from bs4 import BeautifulSoup
import os
import requests
import pymongo
import pandas as pd


# In[3]:


def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


# In[4]:


def scrape():

# Mars News
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    browser.is_element_present_by_css("ul.item_list li.slide", wait_time = 1)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    summary=soup.find('div', class_='list_text')

    title=summary.find('div', class_='content_title')
    mars_title= title.text

    paragraph=summary.find('div', class_='article_teaser_body')
    mars_paragraph= paragraph.text

# JPL Mars Space Images - Featured Image

    url1='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response1 = requests.get(url1)
    soup1 = BeautifulSoup(response1.text, 'html.parser')
    
    image = soup1.find('article')
    image1= image.footer.a
    img_jpl=image1['data-fancybox-href']
    img_link = f'https://jpl.nasa.gov{img_jpl}'
    
# Mars Weather

    url2 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url2)

    browser.is_element_present_by_tag('body div.css-1dbjc4n', wait_time = 1)

    html = browser.html
    soup2 = BeautifulSoup(html, 'html.parser')  

    twitter_body = soup2.body
    twitter_div=twitter_body.find('div', class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0')
    weather_tweet=twitter_div.find('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0').text
  
# Mars Facts

    url3 = 'https://space-facts.com/mars/'
    
    tables = pd.read_html(url3)
    df = tables[0]
    df.columns = ['Attributes','']
    df.set_index('Attributes')
    facts_table = df.to_html()
    

    
# Mars Hemispheres

    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)
    soup3 = BeautifulSoup(browser.html, 'html.parser')
    
    title_list=[]
    titles = soup3.find_all('h3')
    for title in titles:
        title_list.append(title.text)

    images_list=[]
    count=0
    for link in title_list:
        browser.find_by_css('img.thumb')[count].click()
        images_list.append(browser.find_by_text('Sample')['href'])
        browser.back()
        count=count+1

    hemisphere_image_urls = []
    counter = 0
    for item in images_list:
        hemisphere_image_urls.append({"Title":title_list[counter],"img_url":images_list[counter]})
        counter = counter+1
  
    mars_data = {"Title":mars_title, "Paragraph": mars_paragraph, "Featured_Image":img_link,
                 "Weather":weather_tweet,"Facts":facts_table,"Hemispheres":hemisphere_image_urls}
    
    return mars_data


    


# In[ ]:




