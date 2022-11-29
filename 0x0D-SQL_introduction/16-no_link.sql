-- lists all records of second_table of the database hbtn_0c_0
-- dont list rows
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC;
