# Neo4J Profiling Data

## Loading Data

First, all indexes must be created. These can be found in the `indexes` folder. Then we can begin to load the data. The order this is done is as follows:

1. `load_links.cypher`: 3186ms, 4592 labels, 4592 nodes, 4592 properties, 119,882 relationships
2. `load_category.cypher`: 469ms, 152 labels, 152 nodes, 152 properties, 5349 relationships
3. `load_games.cypher`: 491743ms, 398,107 labels, 398,107 nodes, 1,376,773 properties, 398,096 relationships
4. `load_unfinished_games.cypher`: 7749ms, 179,045 labels, created 179,045 nodes, set 636,635 properties, created 154,170 relationships
5. `link_paths_with_articles.cypher`: 8279ms, 500,847 relationships

Total time: 511,426ms or 8 min, 31sec
