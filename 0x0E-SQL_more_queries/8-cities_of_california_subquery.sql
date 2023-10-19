-- List all Californian cities using the state_id from the subquery,a subquery locate California state_id
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
