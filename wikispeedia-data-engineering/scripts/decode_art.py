import csv
import pandas as pd
import numpy as np

def indexed_articles():
    data = pd.read_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/decoded_csv/articles_decoded.csv", delimiter=",").to_numpy()
    pd.DataFrame(data).to_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/articles_iterated.csv", header = ["Article Name"], index_label= "Index")

def article_to_index(article, article_index):
    for i in range(article_index.shape[0]):
        if article_index[i][1] == article:
            return article_index[i][0]

def iterate_articles(article_index, article_links, links_to_index):
    for i in range(article_links.shape[0]):
        links_to_index.append((article_to_index(article_links[i][0], article_index), article_to_index(article_links[i][1], article_index)))

def linkto_articles():
    indexed_articles = pd.read_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/articles_iterated.csv", delimiter=",").to_numpy()
    links_data = pd.read_csv("C:\Development\wikispeedia-data-engineering\wikispeedia-data-engineering\decoded_csv\links_decoded.csv", delimiter = ",").to_numpy()
    linksto_index = []
    iterate_articles(indexed_articles, links_data, linksto_index)
    pd.DataFrame(np.array(linksto_index)).to_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/articles_links_to.csv", header = ["Source ID", "Target ID"], index_label = ["Index"])

    

indexed_articles()
linkto_articles()