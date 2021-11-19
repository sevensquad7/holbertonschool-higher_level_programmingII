-- inner join
SELECT DISTINCT a.title
FROM tv_shows a
LEFT JOIN tv_show_genres b
on a.id = b.show_id
WHERE IFNULL(b.show_id,'') NOT IN (
      		     	SELECT b.show_id
			 FROM tv_shows a
			 LEFT JOIN tv_show_genres b
			 ON a.id = b.show_id
			 LEFT JOIN tv_genres c
			 ON b.genre_id = c.id
			 WHERE c.name = 'Comedy')
ORDER BY 1;
