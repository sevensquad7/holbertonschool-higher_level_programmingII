-- Join
SELECT a.id, a.name, b.name
FROM cities a
INNER JOIN states b
ON a.state_id = b.id
ORDER BY 1;
