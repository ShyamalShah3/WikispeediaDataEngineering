import csv
import pandas as pd
import numpy as np


def get_index(category, cat_list):
    for element in cat_list:
        if element[1] == category:
            return element[0]

def process_cat_list(cat_list, start_id, cat_np, subcat_np, cat_set):
    end_id = start_id
    for i in range(len(cat_list)):
        category = cat_list[i]
        if not category in cat_set:
            cat_np.append((end_id, category))
            cat_set.add(category)
            if i != 0:
                parent_index = get_index(cat_list[i - 1], cat_np)
                subcat_np.append((parent_index, end_id))
            end_id += 1
    return end_id

def iterate_categories():
    data = pd.read_csv("C:\Development\wikispeedia-data-engineering\wikispeedia-data-engineering\decoded_csv\categories_decoded.csv", delimiter=",").to_numpy()
    start_id = 0
    cat_np = []
    subcat_np = []
    cat_set = set()
    for i in range(data.shape[0]):
        cat_list = data[i,1].split(".")
        start_id = process_cat_list(cat_list, start_id, cat_np, subcat_np, cat_set)
    print(subcat_np)
    pd.DataFrame(np.array(cat_np), columns = ["ID", "Name"], index = None).to_csv("C:\Development\wikispeedia-data-engineering\wikispeedia-data-engineering\SQL\categories_iterated.csv", index = None)
    pd.DataFrame(np.array(subcat_np), columns = ["from_id", "to_id"]).to_csv("C:\Development\wikispeedia-data-engineering\wikispeedia-data-engineering\SQL\subcategories_iterated.csv")


iterate_categories()