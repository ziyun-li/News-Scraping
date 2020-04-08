from bs4 import BeautifulSoup
import requests
import csv


csv_file = open('News_Headlines.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Source','Region','Category','Headline','Description'])

url_ft = "https://www.ft.com/"
html_file_ft = requests.get(url_ft).text
# Parse html into BeautifulSoup to get BeautifulSoup object, parser can be lxml, html5
Soup1 = BeautifulSoup(html_file_ft, 'lxml')
articles1 = Soup1.find_all('div',class_= lambda value: value and value.startswith('o-teaser o-teaser--article'))
for article in articles1:
    source = 'Financial Times'
    region = 'World'
    try:
        category = article.find('a',class_='o-teaser__tag').text
    except:
        category = "None found"
    headline = article.find('div',class_='o-teaser__heading').text
    try:
        summary = article.p.a.text
    except:
        summary = "None found"
    csv_writer.writerow([source,region,category,headline,summary])
    print("Category:",category)
    print(headline)
    print(summary)

url_cna = "https://www.channelnewsasia.com/news/asia"
html_file_cna = requests.get(url_cna).text

Soup2 = BeautifulSoup(html_file_cna, 'lxml')
articles2 = Soup2.find_all('div',class_='teaser__content-wrapper')
for article in articles2:
    source = 'Channel News Asia'
    region = 'Asia'
    category = article.find('div',class_='teaser__category-container').text.strip()
    headline = article.h3.a.text
    summary = 'None Found'
    csv_writer.writerow([source,region,category,headline,summary])
    print("Category:",category)


csv_file.close()
