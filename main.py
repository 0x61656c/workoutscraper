import urllib.request
from bs4 import BeautifulSoup, Comment

"""
url='https://www.bodybuilding.com/sitemap/sitemap-bbcomexercise.xml'
"""

def scrape_urls(sitemap_url = "", msearch = 'loc'): #default to xml url parse
  """
  Return a set of stringified content from a file in html/xml format
  """
  content = urllib.request.urlopen(sitemap_url)
  soup = BeautifulSoup(content, "html.parser")
  set_1 = soup.find_all(msearch)
  
  set_2 = []
  for _item in set_1:
    update = str(_item)[5:-6]
    set_2.append(update)
  
  return set_2

def scrape_div_class(key = "", sitemap_url = ""): #default to xml url parse
  """
  Scrape div elements by class
  """
  content = urllib.request.urlopen(sitemap_url)
  soup = BeautifulSoup(content, "html.parser")
  set_1 = soup.find_all("section", {'class' : key})
  
  set_2 = []
  for _item in set_1:
    update = str(_item)[5:-6]
    set_2.append(update)
  
  return set_2

def main():
  sitemap = "https://www.bodybuilding.com/sitemap/sitemap-bbcomexercise.xml"
  data = scrape_urls(sitemap)


  for item in data:
    content = scrape_div_class("ExDetail-section ExDetail-guide",item)
    print(content)


if __name__ == "__main__":
  main()
