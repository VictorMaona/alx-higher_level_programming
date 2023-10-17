-- Determine average temperature for each city and list in descending order of temperature.
SELECT city, AVG(temperature) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
