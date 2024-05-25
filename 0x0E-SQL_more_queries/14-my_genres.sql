-- List all genres of my show
SELECT 
    tv_genres.name
FROM 
    tv_genres
JOIN 
    tv_show_genres  ON id = tv_show_genres.genre_id
JOIN 
    tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE 
    tv_shows.title = 'Dexter'
ORDER BY 
    tv_genres.name ASC;

