CREATE DATABASE `yugioh`;

CREATE TABLE `cards` (
  `id` varchar(100) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `attack_strength` int(11) DEFAULT NULL,
  `defense_strength` int(11) DEFAULT NULL,
  `image_filename` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `decks` (
  `id` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL
);

CREATE TABLE `decks_cards` (
  `id` varchar(100) NOT NULL,
  `card_id` varchar(100) DEFAULT NULL,
  `deck_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);