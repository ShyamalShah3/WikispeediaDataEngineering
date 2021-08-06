import csv
import pandas as pd
import numpy as np

def find_id(name, id_list):
    for i in range(id_list.shape[0]):
        if id_list[i][1] == name:
            return id_list[i][0]

def iterate_art_cat():
    art_cat = pd.read_csv("C:\Development\wikispeedia-data-engineering\wikispeedia-data-engineering\decoded_csv\categories_decoded.csv", delimiter=",").to_numpy()
    art_id = pd.read_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/articles_iterated.csv", delimiter=",").to_numpy()
    cat_id = pd.read_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/categories_iterated.csv", delimiter=",").to_numpy()
    has_art = []
    for i in range(art_cat.shape[0]):
        article = art_cat[i][0]
        category = art_cat[i][1].split(".")[-1]
        has_art.append((find_id(category, cat_id), find_id(article, art_id)))
    pd.DataFrame(np.array(has_art)).to_csv("C:/Development/wikispeedia-data-engineering/wikispeedia-data-engineering/SQL/has_article.csv", header = ["Category ID", "Article ID"], index_label = ["Index"])
    
iterate_art_cat()
