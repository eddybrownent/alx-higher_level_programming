-- List the number of records with the same score in table second_table
-- Records are ordered in descending
SELECT `score`, count(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
