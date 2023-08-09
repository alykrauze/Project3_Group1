SELECT * FROM tshirts;


DROP TABLE jeans;

CREATE TABLE jeans (
	MM6_jeans VARCHAR(50),
	diesel_jeans VARCHAR(50),
	blumarine_jeans VARCHAR(50)
);

SELECT * FROM jeans;

SELECT * FROM tshirts;

CREATE TABLE shirts_and_pants AS
SELECT *
FROM jeans
CROSS JOIN tshirts;

SELECT * FROM shirts_and_pants;

COPY shirts_and_pants TO 'Users/alicekrauze/ru_bootcamp/homework/3Project/Project3_Group1' WITH CSV HEADER;