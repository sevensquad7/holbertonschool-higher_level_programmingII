-- SUM
SELECT d.name, SUM(IFNULL(b.rate,0)) AS rating
FROM tv_shows a
LEFT JOIN tv_show_ratings b
ON a.id = b.show_id
LEFT JOIN tv_show_genres c
ON a.id = c.show_id
LEFT JOIN tv_genres d
ON c.genre_id = d.id
WHERE d.name IS NOT NULL
GROUP BY d.name
ORDER BY 2 DESC;
