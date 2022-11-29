-- lists number of records with the same score in second_table
-- hbtn_0c_0 database
-- result should display score and the number of records
-- for this score with the label number
-- top first
SELECT score, COUNT(*) AS `number` FROM second_table
GROUP BY SCORE
ORDER BY `number` DESC;
