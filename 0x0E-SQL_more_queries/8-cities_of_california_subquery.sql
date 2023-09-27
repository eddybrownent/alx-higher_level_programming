-- Lists all the cities of California in DATABASE hbtn_0d_usa
-- The states table contains only one record where name = California
-- Results must be sorted in ascending order by cities.id
-- The database name will be passed as an argument of the mysql command
-- You are not allowed to use the JOIN keyword

SELECT	`id`,	`name`
FROM	`cities`
WHERE	`state_id` IN
	(SELECT	`id`
		FROM	`states`
		WHERE	`name` = "california")
	ORDER BY `id`;
