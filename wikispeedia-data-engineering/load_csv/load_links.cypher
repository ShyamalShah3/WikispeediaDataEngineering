:auto USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM 'file:///wikispeedia/links_decoded.csv' AS row
MERGE (ls:Article {name:row.linkSource})
MERGE (lt:Article {name:row.linkTarget})
MERGE (ls)-[:LINKS_TO]->(lt)