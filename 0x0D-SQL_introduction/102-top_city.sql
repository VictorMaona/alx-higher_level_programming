-- Show the top three cities with the hottest July and August temperatures.
SELECT city, AVG(temperature) as avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
