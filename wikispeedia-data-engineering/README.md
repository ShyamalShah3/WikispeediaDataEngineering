# Wikispeedia Data Engineering

## Introduction

This folder contains data gathered from the Stanford Network Analysis Project, or SNAP. This is a publicly available data set. The specific data used is the [Wikispeedia data set](https://snap.stanford.edu/data/wikispeedia.html) which contains data gathered from a game where players would be tasked with navigating from one page of Wikipedia to another page.

## Diagram guide

`model_graph.drawio` has the graph database data model.

`model_relational.drawio` has the relational database data model.

## Scripts Guide

The `scripts` folder contains all scripts used to transform the data.

- `decode_csv.py` decoded the URL encoded files in `original_csv` to the files in `decoded_csv`.

The `indexes` folder contains scripts to create indexes that help csv loading and querying proceed faster.

The `load_csv` folder contains scripts to upload the data to Neo4j from the csv format. NOTE: These can be run in almost any order except the script in `link_paths_with_articles.cypher` must be run after the `load_*paths.cypher` files.

## Data Guide

The `original` folder contains the data in the form that it was immediately after downloading. The files here are the following:

- `articles.tsv` contains a listing of all the articles.
- `categories.tsv` maps articles to categories. Categories are heirarchical, with multiple subcategories. Articles can belong to multiple categories.
- `links.tsv` displays all links that each article has.
- `paths_finished.tsv` contains data on instances where a user completes the path between two pages.
- `paths_unfinished.tsv` contains data on instances where a user does not complete the path between two pages.
- `shortest-path-distance-matrix.txt` has the computed shortest distance between any two pages, if it exists.

The `original_csv` folder contains the data after it was converted to csv and comments were stripped.

The `decoded_csv` folder contains the data after the URL encoding was decoded. All these files are encoded in UTF-8.
