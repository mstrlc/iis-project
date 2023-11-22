CREATE SCHEMA IF NOT EXISTS `transport`;
USE `transport`;

DROP TABLE IF EXISTS `user`;

CREATE TABLE IF NOT EXISTS `transport`.`user` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `surname` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;