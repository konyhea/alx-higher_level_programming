-- Lists all shows contained in the db
SELECT
    tvs.title,
    CASE
        WHEN tsg.genre_id IS NOT NULL THEN tsg.genre_id
        ELSE NULL
    END AS genre_id
FROM
    tv_shows tvs
LEFT JOIN
    tv_show_genres tsg ON tvs.id = tsg.show_id
ORDER BY
    tvs.title ASC,
    tsg.genre_id ASC;
