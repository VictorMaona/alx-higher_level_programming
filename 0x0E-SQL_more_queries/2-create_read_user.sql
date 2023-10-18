-- build or change the database hbtn_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- user user_0d_2 with the password user_0d_2_pwd may be created or modified.
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- give user_0d_2 the USAGE privilege across all databases.
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
