-- In the 'second_table' indicate how many records have the same score.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;
