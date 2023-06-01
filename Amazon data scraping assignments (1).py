#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install bs4


# In[2]:


pip install beautifulsoup4


# In[3]:


pip install pandas


# In[4]:


pip install requests


# In[5]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# In[6]:


url = 'https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar'


# In[7]:


HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57','Accept-Language':'en-US, en;q=0.5'})


# In[8]:


webpage = requests.get(url, headers = HEADERS)


# In[9]:


webpage


# In[10]:


webpage.content


# In[11]:


soup = BeautifulSoup(webpage.content, "html.parser")


# In[12]:


soup


# In[13]:


links = soup.find_all("a",attrs = {'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})


# In[14]:


links


# In[15]:


link = links[0].get('href')


# In[16]:


product_list = "http://amazon.in" + link


# In[17]:


product_list


# In[18]:


new_webpage = requests.get(product_list, headers = HEADERS)


# In[19]:


new_webpage


# In[20]:


new_soup = BeautifulSoup(new_webpage.content, "html.parser")


# In[21]:


new_soup


# In[22]:


new_soup.find("span", attrs = {"id":'productTitle'}).text.strip()


# In[23]:


new_soup.find("span", attrs = {"class":'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'}).find("span", attrs = {"class":"a-offscreen"}).text


# In[24]:


new_soup.find("span", attrs = {"class":'a-icon-alt'}).text


# In[25]:


new_soup.find("div", attrs = {"id":'merchant-info'}).text.strip()


# In[26]:


# Function to extract Availability Status
def get_Product_Name(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price
def get_price(soup):

    try:
        price = soup.find("span", attrs = {"class":"a-offscreen"}).text

    except AttributeError:

            price = ""

    return price

def get_rating(soup):

    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""	

    return rating

def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = "Not Available"	

    return available

def get_seller_name(soup):

    try:
        # Outer Tag Object
        seller = soup.find("div", attrs={"id":'merchant-info'})
        
        # Inner NavigatableString Object
        seller_value = seller.text

        # Title as a string value
        seller_string = seller_value.strip()

    except AttributeError:
        seller_string = ""

    return seller_string


# In[ ]:


if __name__ == '__main__':
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57', 'Accept-Language': 'en-US, en;q=0.5'}

    URL = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"

    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")

    links = soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})
    links_list = [link.get('href') for link in links]

    d = {"Product Name": [], "price":[], "rating":[], "availability": [], "Seller Name": []}

    for link in links_list:
        new_webpage = requests.get("https://www.amazon.in" + link, headers=HEADERS)
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")
        
        availability = get_availability(new_soup)
        if availability == "In stock":
            seller_name = get_seller_name(new_soup)
            d['Seller Name'].append(seller_name)
        else:
            print("Product is out of stock")
            
        d['Product Name'].append(get_Product_Name(new_soup))
        d['price'].append(get_price(new_soup))
        d['rating'].append(get_rating(new_soup))
        d['availability'].append(availability)

    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df.dropna(subset=['Product Name'], inplace=True)
    amazon_df.to_csv("amazon_data.csv", header=True, index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




