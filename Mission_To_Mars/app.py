#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars1


# In[2]:


app = Flask(__name__)


# In[3]:


app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# In[4]:


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


# In[ ]:


@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_data = scrape_mars1.scrape()
    mars.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

