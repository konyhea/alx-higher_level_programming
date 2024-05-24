-- List all db with genresof the show Dexter
SELECT 
    tv_genres.name AS genre,
    COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM 
    tv_genres
JOIN 
    tv_show_genres  ON id = tv_show_genres.genre_id
GROUP BY 
    tv_show_genres.genre_id
ORDER BY 
    number_of_shows DESC;
