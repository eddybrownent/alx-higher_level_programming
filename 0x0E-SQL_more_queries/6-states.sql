-- Create  a DATABASE hbtn_0d_usa with a table states
-- id INT unique, auto generated, can’t be null and is a primary key
--   name VARCHAR(256) can’t be null

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
	PRIMARY KEY(`id`),
	`id`	INT	NOT NULL AUTO_INCREMENT,
	`name`	VARCHAR(256) NOT NULL
);
