:auto USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM 'file:///wikispeedia/categories_decoded.csv' AS row
MERGE (a:Article {name: row.article})
WITH a, split(row.category, '.') AS category_list
WITH a, category_list, range(0,size(category_list)-2) AS range_list
UNWIND range_list AS i
MERGE (c1:Category {name:category_list[i]})
MERGE (c2:Category {name:category_list[i+1]})
MERGE (c1) -[:SUBCATEGORY]-> (c2)
MERGE (c:Category {name:category_list[-1]})
MERGE (c) -[:HAS_ARTICLE]-> (a)
