match ()-[r]->() delete r
match (n) delete n


LOAD CSV WITH HEADERS FROM 'file:///dyr.csv' AS row
MERGE (seed:Seed {key: row.key, name: row.name, quality: row.quality})
ON MATCH SET seed.key = row.key, seed.name = row.name, seed.quality = row.quality;

MATCH (n:Seed {quality:'q1'})
SET n:q1;

MATCH (n:Seed {quality:'q2'})
SET n:q2;

MATCH (n:Seed {quality:'q3'})
SET n:q3;

MATCH (n:Seed {quality:'q4'})
SET n:q4;

MATCH (n:Seed {quality:'q5'})
SET n:q5;

MATCH (n:Seed {quality:'q6'})
SET n:q6;

MATCH (n:Seed {quality:'q7'})
SET n:q7;

MATCH (n:Seed {quality:'q8'})
SET n:q8;

MATCH (n:Seed {quality:'q9'})
SET n:q9;

MATCH (n:Seed {quality:'q0'})
SET n:q0;




LOAD CSV WITH HEADERS FROM 'file:///dyr_links.csv' AS row
MATCH (seed_1:Seed {key: row.seed1})
MATCH (seed_2:Seed {key: row.seed2})
MERGE (seed_1)-[l:LINK]-(seed_2);