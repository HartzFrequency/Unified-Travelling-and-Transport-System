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
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight` (
  `flightNo` varchar(10) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `FromLocation` varchar(8) DEFAULT NULL,
  `ToLocation` varchar(8) DEFAULT NULL,
  `Duration` time DEFAULT NULL,
  `Type` varchar(4) DEFAULT NULL,
  `Capacity` int DEFAULT NULL,
  `Fare` int DEFAULT NULL,
  PRIMARY KEY (`flightNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
INSERT INTO `flight` VALUES ('AF189','Flight 14','CDG','ORD','09:30:00','BU',180,6400),('AF198','Flight 5','CDG','HND','12:00:00','BU',150,7200),('AI101','Flight 1','DEL','LHR','08:45:00','EC',180,4500),('AI202','Flight 11','BOM','DXB','03:30:00','BU',120,3200),('AI820','Flight 20','DEL','DXB','03:45:00','BU',120,3300),('BA249','Flight 2','LHR','JFK','06:30:00','BU',220,6500),('BA735','Flight 12','LHR','SFO','11:05:00','FC',80,11800),('CA977','Flight 16','PEK','LAX','11:30:00','EC',200,8400),('CA983','Flight 7','PEK','JFK','13:10:00','EC',220,7800),('DL412','Flight 17','ATL','LHR','07:35:00','BU',150,4900),('DL68','Flight 8','ATL','CDG','08:20:00','BU',180,5200),('EK406','Flight 4','SYD','DXB','13:20:00','EC',200,9500),('LH107','Flight 18','FRA','JFK','08:35:00','FC',100,10100),('LH430','Flight 9','FRA','ORD','09:15:00','FC',120,9800),('QF1','Flight 10','SYD','LAX','13:30:00','EC',200,8900),('QF15','Flight 19','SYD','JFK','20:10:00','EC',220,10700),('SQ22','Flight 3','JFK','SIN','18:15:00','FC',80,13500),('SQ710','Flight 13','SIN','PEK','05:35:00','EC',150,5700),('UA223','Flight 6','LAX','LHR','10:55:00','FC',100,10500),('UA908','Flight 15','SFO','LHR','10:25:00','FC',120,11200);
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
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
