-- inner join
SELECT DISTINCT a.title
FROM tv_shows a
INNER JOIN tv_show_genres b
ON a.id = b.show_id
INNER JOIN tv_genres c
ON b.genre_id = c.id
WHERE c.name = 'Comedy'
ORDER BY 1;
