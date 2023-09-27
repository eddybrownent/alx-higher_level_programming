-- List the records in the table second_table of >= 10 score
-- The order is in descending score
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
