-- Using the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Using Sub-query to fetch the cities of California sorted by cities.id
SELECT cities.id, cities.name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id ASC;
