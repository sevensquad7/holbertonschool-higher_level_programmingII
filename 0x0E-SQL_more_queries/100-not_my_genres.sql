-- inner join
SELECT DISTINCT a.name
FROM tv_genres a
INNER JOIN tv_show_genres b
on a.id = b.genre_id
WHERE b.genre_id NOT IN (
      		     	SELECT b.genre_id
			 FROM tv_shows a
			 INNER JOIN tv_show_genres b
			 ON a.id = b.show_id
			 INNER JOIN tv_genres c
			 ON b.genre_id = c.id
			 WHERE a.title = 'Dexter')
ORDER BY 1;
