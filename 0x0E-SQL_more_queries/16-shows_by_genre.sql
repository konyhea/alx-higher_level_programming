-- list shows and genres
SELECT tv_shows.title,
       CASE
           WHEN tv_genres.name IS NOT NULL THEN tv_genres.name
           ELSE NULL
       END AS genre_name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, genre_name ASC;
