-- inner join
SELECT DISTINCT c.name
FROM tv_shows a
INNER JOIN tv_show_genres b
ON a.id = b.show_id
INNER JOIN tv_genres c
ON b.genre_id = c.id
WHERE a.title = 'Dexter'
ORDER BY 1;
