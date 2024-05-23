SELECT 
    tvg.name
FROM 
    tv_show_genres tsg
JOIN 
    tv_shows ts ON tsg.show_id = ts.id
JOIN 
    tv_genres tvg ON tsg.genre_id = tvg.id
WHERE 
    ts.title = 'Dexter'
ORDER BY 
    tvg.name ASC;

