-- List all db with genresof the show Dexter
SELECT 
    tvsg.genre_id AS genre,
    COUNT(tsg.show_id) AS number_of_shows
FROM 
    tv_show_genres tvsg
JOIN 
    tv_shows tsg ON tvsg.show_id = tsg.id
GROUP BY 
    tvsg.genre_id
ORDER BY 
    number_of_shows DESC;

