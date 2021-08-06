:auto USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM 'file:///wikispeedia/fixed_paths_finished_decoded.csv' AS row
CREATE (g:Game { hashedIpAddress: row.hashedIpAddress, timestamp: toInteger(row.timestamp), durationInSec: toInteger(row.durationInSec)})
SET g.rating = toInteger(row.rating)
WITH g, split(row.path, ';') AS path_list
SET g.length = size(path_list)
SET g.path_start = path_list[0]
SET g.path_end = path_list[size(path_list)-1]
CREATE (g)-[:PATH_START]->(first:Path {name: path_list[0], visit: 0, game_id:ID(g)})
CREATE (g)-[:PATH_END]->(last:Path {name: path_list[size(path_list)-1], visit: size(path_list)-1, game_id: ID(g)})
WITH ID(g) AS game_id, path_list, range(0, size(path_list) - 2) AS range_list
UNWIND range_list as index
MERGE (p1:Path {name: path_list[index], visit: index, game_id: game_id})
MERGE (p2:Path {name: path_list[index+1], visit: index+1, game_id: game_id})
MERGE (p1)-[:CONTINUES_PATH]->(p2)
