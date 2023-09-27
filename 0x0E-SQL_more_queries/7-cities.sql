-- Create a DATABASE hbtn_0d_usa with the table cities
-- cities description:
--	id INT unique, auto generated, can’t be null and is a primary key
-- 	state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
--	name VARCHAR(256) can’t be null

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	PRIMARY KEY(`id`),
	`id`		INT		NOT NULL AUTO_INCREMENT,
	`state_id`	INT		NOT NULL,
	`name`		VARCHAR(256)	NOT NULL,
	FOREIGN KEY(`state_id`)
	REFERENCES `hbtn_0d_usa`.`states`(`id`)
);