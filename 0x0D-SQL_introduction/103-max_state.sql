-- Show the highest temperature recorded in each state listed by name of state.
SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
