-- Exclude when name is empty
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;

