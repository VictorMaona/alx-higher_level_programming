-- Utilize the database hbtn_0d_usa.
USE hbtn_0d_usa;

-- Using a subquery locate California state_id. 
SELECT id FROM states WHERE name = 'California';

-- List all Californian cities using the state_id from the subquery.
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
