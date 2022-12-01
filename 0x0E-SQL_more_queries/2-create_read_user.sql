-- creates database hbtn_0d)2 and user_0d_2
-- user has SELECT privileges on hbtn_0d_2 with password
-- user_0d_2_pwd
CREATE DATABASE
	IF NOT EXISTS hbtn_0d_02;
CREATE USER
	IF NOT EXISTS 'user_0d_2'@'localhost'
	IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
	ON hbtn_0d_2.*
	TO 'user_0d_2'@'localhost'
	IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;
