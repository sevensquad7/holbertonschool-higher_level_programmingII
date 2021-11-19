-- SUM
SELECT a.title, SUM(IFNULL(b.rate,0)) AS rating
FROM tv_shows a
LEFT JOIN tv_show_ratings b
ON a.id = b.show_id
GROUP BY a.title
ORDER BY 2 DESC;
