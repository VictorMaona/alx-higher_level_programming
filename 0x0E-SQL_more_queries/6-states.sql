-- Create or change the hbtn_0d_usa database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Utilize the database hbtn_0d_usa.
USE hbtn_0d_usa;
-- Making or changing the table's states
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
