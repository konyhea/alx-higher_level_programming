-- Using the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Single SELECT statement with LEFT JOIN and ORDER BY clause
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

