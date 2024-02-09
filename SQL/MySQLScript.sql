-- Set safe update preference
--SET SQL_SAFE_UPDATES = 0;

-- Update non-numeric and empty values to null
UPDATE surveys
SET weight = NULLIF(TRIM(weight), '')
WHERE weight IS NOT NULL AND NOT TRIM(weight) REGEXP '^[0-9]+$';


-- Update NULL values to 0
UPDATE surveys 
SET 
    weight = 0
WHERE
    weight IS NULL;

-- Alter the table to change the data type of the weight column to INTEGER
ALTER TABLE surveys
MODIFY COLUMN weight INT;



-- hindfootlength column
-- Update non-numeric and empty values to null
UPDATE surveys 
SET 
    hindfoot_length = NULLIF(TRIM(hindfoot_length), '')
WHERE
    weight IS NOT NULL
        AND NOT TRIM(hindfoot_length) REGEXP '^[0-9]+$';

-- Update NULL values to 0
UPDATE surveys 
SET 
    hindfoot_length = 0
WHERE
    hindfoot_length IS NULL;

-- Alter the table to change the data type of the hindfoot_length column to INTEGER
ALTER TABLE surveys
MODIFY COLUMN hindfoot_length INT;

-- selecting all the records in the surveys table
SELECT 
    *
FROM
    surveys;

-- selecting year, onth and day column from the surveys table
SELECT 
    year, month, day
FROM
    surveys;

-- selecting only the year column from the surveys table
SELECT 
    year
FROM
    surveys;

/*
This is how to write a multiline comment
SQL engine will not execute this
*/

SELECT 
    *
FROM
    surveys
LIMIT 100;

-- Selecting the top 10
SELECT 
    *
FROM
    surveys
LIMIT 10;

-- Select unique records
SELECT DISTINCT
    species_id
FROM
    surveys;

/* Select year, month, day, sex, weight limit 
the result by 100 and use a multiline comment */
SELECT 
    year, month, day, sex, weight
FROM
    surveys
LIMIT 100;

-- Weight in miligrams
SELECT 
    species_id, weight * 1000 AS weight_in_mg
FROM
    surveys;

-- Rounding values
SELECT 
    species_id,
    year,
    month,
    day,
    ROUND(weight / 1000, 2) AS weight_in_kg_2dp
FROM
    surveys;

-- Filtering
SELECT 
    *
FROM
    surveys
WHERE
    species_id = 'DM';

-- Filtering expressions 9where year is 2000 or before
SELECT 
    *
FROM
    surveys
WHERE
    year <= '2000';

-- Filtering logic
SELECT 
    *
FROM
    surveys
WHERE
    year <= '2000' AND species_id = 'DM';

SELECT 
    *
FROM
    surveys
WHERE
    species_id = 'DM' OR species_id = 'DO'
        OR species_id = 'DS';

-- Challenge
SELECT 
    species_id,
    year,
    plot_id,
    weight,
    weight / 1000 AS weight_in_kg
FROM
    surveys
WHERE
    plot_id = 1 AND weight >= 75;

SELECT 
    *
FROM
    surveys
WHERE
    year >= 2000
        AND (species_id IN ('DM' , 'DO', 'DS'));

-- Sorting
SELECT 
    *
FROM
    species
ORDER BY genus ASC , species ASC;

-- Challenge
SELECT 
    year, species_id, weight / 1000 AS weight_in_kg
FROM
    surveys
ORDER BY weight_in_kg DESC;

-- Counting records i na table
SELECT 
    COUNT(*) AS surveys_count
FROM
    surveys;

-- Count aggragates
SELECT 
    COUNT(*) AS surveys_count, MIN(weight) AS min_weight
FROM
    surveys;

SELECT 
    COUNT(*) AS surveys_count, MAX(weight) AS max_weight
FROM
    surveys;

SELECT 
    SUM(weight) AS total_weight,
    AVG(weight) AS avg_weight,
    MAX(weight) AS max_weight,
    MIN(weight) AS min_weight
FROM
    surveys
WHERE
    weight >= 5 AND weight <= 10;

-- group by
SELECT 
    species_id, COUNT(*)
FROM
    surveys
GROUP BY species_id;

-- Challenge
SELECT 
    year,
    COUNT(*) AS total_individual_count,
    species_id,
    AVG(weight) AS avg_weight
FROM
    surveys
GROUP BY year , species_id;

-- Order by aggregated values
SELECT 
    species_id, COUNT(*) AS species_count
FROM
    surveys
GROUP BY species_id
ORDER BY species_count;

-- aliases
SELECT 
    MAX(year) AS last_surveyed_year
FROM
    surveys;

SELECT 
    AVG(weight) AS avg_weight
FROM
    surveys;

-- Having
SELECT 
    species_id, COUNT(species_id) AS species_count
FROM
    surveys
GROUP BY species_id
HAVING species_count < 10;

SELECT 
    taxa, COUNT(*) AS taxa_count
FROM
    species
GROUP BY taxa
HAVING taxa_count > 10;

-- view 
CREATE VIEW summer_2000 AS
    SELECT 
        *
    FROM
        surveys
    WHERE
        year = 2000
            AND (month > 4 AND month < 10);

SELECT 
    *
FROM
    summer_2000
WHERE
    species_id = 'PE';

-- task
CREATE VIEW individual_captured AS
    SELECT 
        *
    FROM
        surveys
    WHERE
        year < 2000;

SELECT 
    *
FROM
    individual_captured;

SELECT 
    COUNT(*) AS sex_count
FROM
    individual_captured
WHERE
    sex = 'M';

-- Creating a database
CREATE DATABASE happyday;

-- create a table in the database
CREATE TABLE people (
    person_id INT,
    last_name VARCHAR(255),
    first_name VARCHAR(255),
    job_title VARCHAR(255),
    report_to VARCHAR(255)
);
-- add records into table
INSERT INTO people (person_id, last_name, first_name, job_title)
VALUES(1,'gru','felonius','supervillian');

-- add records to all rows
INSERT INTO people
VALUES (2, 'nefario', 'gru','doctor','supervillian');

-- have a quick look at the table
SELECT 
    *
FROM
    people;

INSERT INTO people
VALUES
(3,null, 'mel','minion','gru'),
(4,null, 'bob','minion','gru'),
(5,null, 'stewart','minion','gru'),
(6,null, 'john','minion','gru');

-- updating database
UPDATE people 
SET 
    job_title = 'Senior data scientist'
WHERE
    person_id = 2;

-- delete from table
DELETE FROM people 
WHERE
    person_id = 2;

-- deleting a column from the table
ALTER TABLE people
DROP COLUMN last_name;

-- Inner Join
SELECT 
    *
FROM
    surveys
        JOIN
    species ON surveys.species_id = species.species_id;

-- challenge
SELECT 
    species.genus, species.species, surveys.weight
FROM
    surveys
        JOIN
    species ON surveys.species_id = species.species_id;

-- LEFT JOIN
SELECT 
    *
FROM
    surveys
        LEFT JOIN
    species ON surveys.species_id = species.species_id;

-- RIGHT JOIN
SELECT 
    *
FROM
    surveys
        RIGHT JOIN
    species ON surveys.species_id = species.species_id;

-- FULL OUTER JOIN
SELECT 
    *
FROM
    surveys
        LEFT JOIN
    species ON surveys.species_id = species.species_id 
UNION SELECT 
    *
FROM
    surveys
        RIGHT JOIN
    species ON surveys.species_id = species.species_id;

-- challenge
SELECT 
    plots.plot_type, AVG(surveys.weight) AS Average_weight
FROM
    surveys
        JOIN
    plots ON surveys.plot_id = plots.plot_id
GROUP BY plots.plot_type;

-- chellenge
SELECT 
    surveys.species_id,
    species.taxa,
    AVG(weight) AS average_weight
FROM
    species
        JOIN
    surveys ON surveys.species_id = species.species_id
WHERE
    species.taxa = 'rodent'
GROUP BY surveys.species_id , species.taxa;


-- replace missing values
SELECT 
    species_id, sex, COALESCE(sex, 'U') AS sex_replaced
FROM
    surveys;

SELECT 
    hindfoot_length,
    COALESCE(hindfoot_length, '30') AS hindfoot_length_replaced
FROM
    surveys;

SELECT 
    species_id, AVG(hindfoot_length) as average_hindfoot_length
FROM
    surveys
WHERE hindfoot_length <> 30
GROUP BY species_id;
