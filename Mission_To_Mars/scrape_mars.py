{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape():\n",
    "    executable_path = {\"executable_path\": \"chromedriver.exe\"}\n",
    "    browser = Browser('chrome', **executable_path, headless=False)\n",
    "    url_news = 'https://mars.nasa.gov/news/'\n",
    "    browser.visit(url_news)\n",
    "    \n",
    "    summary=soup.find('div', class_='list_text')\n",
    "    title=summary.find('div', class_='content_title')\n",
    "    title= title.text\n",
    "\n",
    "    paragraph=summary.find('div', class_='article_teaser_body')\n",
    "    paragraph= paragraph.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
