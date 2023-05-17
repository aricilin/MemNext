match ()-[r]->() delete r
match (n) delete n


LOAD CSV WITH HEADERS FROM 'file:///sampledyr.csv' AS row
MERGE (seed:Seed {key: row.key, name: row.name, quality: row.quality})
ON MATCH SET seed.key = row.key, seed.name = row.name, seed.quality = row.quality;


LOAD CSV WITH HEADERS FROM 'file:///sampledyr_links.csv' AS row
MATCH (seed_1:Seed {key: row.seed1})
MATCH (seed_2:Seed {key: row.seed2})
MERGE (seed_1)-[l:LINK]-(seed_2);