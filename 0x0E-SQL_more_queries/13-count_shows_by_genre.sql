-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT
	genre.`name` AS `genre`,
	COUNT(*) AS `number_of_shows`
FROM
	`tv_genres` AS genre
INNER JOIN
	`tv_show_genres` AS show_genre
	ON genre.`id` = show_genre.`genre_id`
GROUP BY
	genre.`name`
ORDER BY
	`number_of_shows` DESC;
