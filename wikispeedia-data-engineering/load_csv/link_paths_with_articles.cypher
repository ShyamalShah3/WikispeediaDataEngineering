MATCH (p:Path)
WITH collect(p) as all_path_nodes
UNWIND all_path_nodes AS pn
MATCH (a:Article {name:p.name})
MERGE (p)-[:ARTICLE]->(a)
