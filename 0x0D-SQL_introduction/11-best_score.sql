-- lists all records in the second_table with score >= 10
-- records are ordered top first using score
SELECT score, name FROM second_table 
WHERE score >= 10 ORDER BY score DESC;
