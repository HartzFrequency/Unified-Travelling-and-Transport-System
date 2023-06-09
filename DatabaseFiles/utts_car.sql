-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: utts
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car` (
  `CarID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `FromLocation` varchar(8) DEFAULT NULL,
  `ToLocation` varchar(8) DEFAULT NULL,
  `Duration` time DEFAULT NULL,
  `Type` varchar(4) DEFAULT NULL,
  `Capacity` int DEFAULT NULL,
  `Fare` int DEFAULT NULL,
  PRIMARY KEY (`CarID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (1,'Car 1','GWL','DLH','08:00:00','DI',4,500),(2,'Car 2','BHP','MUM','12:00:00','PE',5,750),(3,'Car 3','DLH','BHP','10:00:00','DI',3,600),(4,'Car 4','MUM','GWL','14:00:00','EV',6,900),(5,'Car 5','GWL','BHP','06:00:00','DI',2,300),(6,'Car 6','DLH','MUM','16:00:00','EV',7,1200),(7,'Car 7','BHP','GWL','09:00:00','PE',3,450),(8,'Car 8','MUM','DLH','18:00:00','DI',8,1500),(9,'Car 9','GWL','MUM','10:00:00','EV',4,700),(10,'Car 10','BHP','DLH','07:00:00','PE',2,350),(11,'Car 11','BHP','GWL','09:00:00','DI',3,450),(12,'Car 12','MUM','DLH','18:00:00','EV',8,1500),(13,'Car 13','GWL','MUM','10:00:00','DI',4,700),(14,'Car 14','BHP','DLH','07:00:00','EV',2,350),(15,'Car 15','DLH','MUM','16:00:00','PE',7,1200),(16,'Car 16','GWL','BHP','06:00:00','DI',2,300),(17,'Car 17','MUM','GWL','14:00:00','EV',6,900),(18,'Car 18','DLH','BHP','10:00:00','PE',3,600),(19,'Car 19','BHP','MUM','12:00:00','DI',5,750),(20,'Car 20','GWL','DLH','08:00:00','EV',4,500);
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-25 13:15:14
