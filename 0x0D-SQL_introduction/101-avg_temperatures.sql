-- import hbtn_0c_0 database this table dump
-- script that displays the average temp(Fahrengeit) by city
-- by temperature(top first)
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
