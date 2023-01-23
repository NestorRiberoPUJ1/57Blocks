-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: 57blocks
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pokemons`
--

DROP TABLE IF EXISTS `pokemons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pokemons` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `type` varchar(45) NOT NULL,
  `health` int NOT NULL,
  `attack` int NOT NULL,
  `defense` int NOT NULL,
  `public` tinyint NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_pokemons_users_idx` (`user_id`),
  CONSTRAINT `fk_pokemons_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokemons`
--

LOCK TABLES `pokemons` WRITE;
/*!40000 ALTER TABLE `pokemons` DISABLE KEYS */;
INSERT INTO `pokemons` VALUES (1,'Magno','Fire',200,5,150,1,'2023-01-22 21:24:05','2023-01-22 21:24:05',1),(2,'Looky','Wind',20,15,120,1,'2023-01-22 21:24:23','2023-01-22 21:24:23',1),(3,'Pribbu','Water',60,10,70,1,'2023-01-22 21:24:52','2023-01-22 21:24:52',1),(4,'Kokky','Water',60,10,70,1,'2023-01-22 21:25:03','2023-01-22 21:25:03',1),(5,'Sludge','Water',60,10,70,1,'2023-01-22 21:25:10','2023-01-22 21:25:10',1),(6,'Martins','Wind',60,10,70,1,'2023-01-22 21:25:17','2023-01-22 21:25:17',1),(7,'Lenit','Wind',60,10,70,1,'2023-01-22 21:25:24','2023-01-22 21:25:24',1),(8,'Rocka','Earth',60,10,70,1,'2023-01-22 21:25:34','2023-01-22 21:25:34',1),(9,'Pretorian','Earth',60,10,70,1,'2023-01-22 21:25:41','2023-01-22 21:25:41',1),(10,'Magma','Fire',60,10,70,1,'2023-01-22 21:25:49','2023-01-22 21:25:49',1),(11,'Farhe','Fire',60,10,70,1,'2023-01-22 21:25:56','2023-01-22 21:25:56',1),(12,'Volta','Fire',60,10,70,1,'2023-01-22 21:26:03','2023-01-22 21:26:03',1);
/*!40000 ALTER TABLE `pokemons` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-22 23:39:14
