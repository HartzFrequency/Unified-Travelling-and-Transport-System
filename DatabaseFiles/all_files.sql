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
-- Table structure for table `abbreviation`
--

DROP TABLE IF EXISTS `abbreviation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `abbreviation` (
  `abbreviation` varchar(8) DEFAULT NULL,
  `full_form` varchar(50) DEFAULT NULL,
  UNIQUE KEY `abbreviation` (`abbreviation`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `abbreviation`
--

LOCK TABLES `abbreviation` WRITE;
/*!40000 ALTER TABLE `abbreviation` DISABLE KEYS */;
INSERT INTO `abbreviation` VALUES ('NANS','Non Air Conditioning Non Sleeper'),('NASL','Non Air Conditioning Sleeper'),('ACNS','Air Conditioning Non Sleeper'),('ACSL','Air Conditioning Sleeper'),('DI','Diesel'),('PE','Petrol'),('EV','Electric Vechile'),('AC','Air conditioning'),('CC','Chair coach'),('GN','General Coach'),('SL','Sleeper'),('FC','First Class'),('BU','Buisness'),('EC','Econoimics');
/*!40000 ALTER TABLE `abbreviation` ENABLE KEYS */;
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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `Admin_ID` int NOT NULL,
  `Admin_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Admin_ID`),
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`Admin_ID`) REFERENCES `users` (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'harsh shrivastava'),(2,'gauri thakre'),(3,'akhil jain'),(4,'abhishek rajput');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
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
-- Table structure for table `bus`
--

DROP TABLE IF EXISTS `bus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bus` (
  `BusID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `FromLocation` varchar(8) DEFAULT NULL,
  `ToLocation` varchar(8) DEFAULT NULL,
  `Duration` time DEFAULT NULL,
  `Type` varchar(4) DEFAULT NULL,
  `Capacity` int DEFAULT NULL,
  `Fare` int DEFAULT NULL,
  PRIMARY KEY (`BusID`),
  UNIQUE KEY `BusID_UNIQUE` (`BusID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bus`
--

LOCK TABLES `bus` WRITE;
/*!40000 ALTER TABLE `bus` DISABLE KEYS */;
INSERT INTO `bus` VALUES (1,'Bus 1','GWL','DLH','08:00:00','NANS',40,500),(2,'Bus 2','BHP','MUM','12:30:00','NASL',50,750),(3,'Bus 3','DLH','BHP','10:45:00','ACNS',30,600),(4,'Bus 4','MUM','GWL','14:15:00','ACSL',60,900),(5,'Bus 5','GWL','BHP','06:45:00','NASL',20,300),(6,'Bus 6','DLH','MUM','16:30:00','ACSL',70,1200),(7,'Bus 7','BHP','GWL','09:00:00','NANS',35,450),(8,'Bus 8','MUM','DLH','18:15:00','ACNS',80,1500),(9,'Bus 9','GWL','MUM','10:30:00','NASL',45,700),(10,'Bus 10','BHP','DLH','07:15:00','ACSL',25,350),(11,'Bus 11','BHP','GWL','09:45:00','NANS',35,450),(12,'Bus 12','MUM','DLH','18:45:00','ACSL',80,1500),(13,'Bus 13','GWL','MUM','10:15:00','NASL',45,700),(14,'Bus 14','BHP','DLH','07:30:00','ACNS',25,350),(15,'Bus 15','DLH','MUM','16:00:00','NASL',70,1200),(16,'Bus 16','GWL','BHP','06:30:00','NASL',20,300),(17,'Bus 17','MUM','GWL','14:30:00','ACSL',60,900),(18,'Bus 18','DLH','BHP','10:15:00','ACNS',30,600),(19,'Bus 19','BHP','MUM','12:00:00','NASL',50,750),(20,'Bus 20','GWL','DLH','08:30:00','NANS',40,500);
/*!40000 ALTER TABLE `bus` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-25 13:15:15
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
-- Table structure for table `railways`
--

DROP TABLE IF EXISTS `railways`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `railways` (
  `PNR` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `fare` int DEFAULT NULL,
  `time` time DEFAULT NULL,
  PRIMARY KEY (`PNR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `railways`
--

LOCK TABLES `railways` WRITE;
/*!40000 ALTER TABLE `railways` DISABLE KEYS */;
INSERT INTO `railways` VALUES (1001,'Train 1',500,'10:30:00'),(1002,'Train 2',750,'11:00:00'),(1003,'Train 3',300,'12:45:00'),(1004,'Train 4',900,'14:20:00'),(1005,'Train 5',600,'15:10:00'),(1006,'Train 6',450,'16:30:00'),(1007,'Train 7',800,'17:15:00'),(1008,'Train 8',350,'18:00:00'),(1009,'Train 9',550,'19:30:00'),(1010,'Train 10',700,'20:45:00'),(1011,'Train 11',400,'21:20:00'),(1012,'Train 12',950,'22:00:00'),(1013,'Train 13',250,'23:30:00'),(1014,'Train 14',850,'00:15:00'),(1015,'Train 15',500,'01:00:00');
/*!40000 ALTER TABLE `railways` ENABLE KEYS */;
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
-- Table structure for table `train`
--

DROP TABLE IF EXISTS `train`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `train` (
  `PNR` int NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `FromLocation` varchar(8) DEFAULT NULL,
  `ToLocation` varchar(8) DEFAULT NULL,
  `Duration` time DEFAULT NULL,
  `Type` varchar(4) DEFAULT NULL,
  `Capacity` int DEFAULT NULL,
  `Fare` int DEFAULT NULL,
  PRIMARY KEY (`PNR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `train`
--

LOCK TABLES `train` WRITE;
/*!40000 ALTER TABLE `train` DISABLE KEYS */;
INSERT INTO `train` VALUES (1234,'Duronto Express','DLH','GWL','10:00:00','AC',60,1700),(12345,'Rajdhani Express','DLH','MUM','10:30:00','GN',50,1500),(23456,'Shatabdi Express','MUM','DLH','08:45:00','CC',40,1000),(34567,'Garib Rath Express','BHP','GWL','06:15:00','SL',70,500),(45678,'Duronto Express','GWL','DLH','11:00:00','AC',60,1800),(56789,'Jan Shatabdi Express','DLH','BHP','08:30:00','CC',50,1200),(67890,'Tejas Express','BHP','MUM','07:00:00','AC',45,2000),(78901,'Rajdhani Express','MUM','DLH','11:30:00','AC',50,1800),(89012,'Shatabdi Express','DLH','BHP','09:15:00','CC',40,1100),(90123,'Garib Rath Express','MUM','GWL','05:45:00','SL',70,450);
/*!40000 ALTER TABLE `train` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-25 13:15:15
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
-- Table structure for table `trucks`
--

DROP TABLE IF EXISTS `trucks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trucks` (
  `truckNo` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `fare` int DEFAULT NULL,
  `time` time DEFAULT NULL,
  PRIMARY KEY (`truckNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trucks`
--

LOCK TABLES `trucks` WRITE;
/*!40000 ALTER TABLE `trucks` DISABLE KEYS */;
INSERT INTO `trucks` VALUES (1001,'Truck 1',500,'10:30:00'),(1002,'Truck 2',750,'11:00:00'),(1003,'Truck 3',300,'12:45:00'),(1004,'Truck 4',900,'14:20:00'),(1005,'Truck 5',600,'15:10:00'),(1006,'Truck 6',450,'16:30:00'),(1007,'Truck 7',800,'17:15:00'),(1008,'Truck 8',350,'18:00:00'),(1009,'Truck 9',550,'19:30:00'),(1010,'Truck 10',700,'20:45:00'),(1011,'Truck 11',400,'21:20:00'),(1012,'Truck 12',950,'22:00:00'),(1013,'Truck 13',250,'23:30:00'),(1014,'Truck 14',850,'00:15:00'),(1015,'Truck 15',500,'01:00:00');
/*!40000 ALTER TABLE `trucks` ENABLE KEYS */;
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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(25) NOT NULL,
  `last_name` varchar(25) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `phone` varchar(15) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(25) NOT NULL,
  `points` int DEFAULT '0',
  `Password` varchar(8) NOT NULL,
  PRIMARY KEY (`UserID`,`Password`),
  UNIQUE KEY `Password_UNIQUE` (`Password`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'harsh','shrivastava','2003-06-05','8109288418','Hathi Khana Road Morar','Gwalior','MP',0,'20030605'),(2,'gauri','thakre','2003-11-30','9479675959','Hostel No. 4, MITS','Gwalior','MP',0,'20031130'),(3,'akhil','jain','2003-08-05','7456025891','Dal Bazar','Gwalior','MP',0,'20030805'),(4,'abhishek','rajput','2003-07-05','8109288418','Hazira','Gwalior','MP',0,'20030705'),(5,'shahrukh','khan','1992-01-09','8827344852','Gandhi Chowk Bazar','Chatarpur','MP',0,'19920109'),(6,'shraddha','kapoor','1985-08-30','6212418873','Juhu','Mumbai','MH',0,'19850830'),(7,'sunny','deol','1983-12-25','6748319921','Jalianvala Bagh','Amritsar','PJ',0,'19831225'),(8,'hema','malini','1948-10-16','9828157533','Kavi Bharti Nagar','Tiruchirapalli','TN',0,'19481016'),(9,'jethalal','gada','2004-12-02','7852773891','Phool Bagh','Gwalior','MP',0,'20041202'),(10,'kartik','aryan','1995-02-14','7143143143','Thatipur','Gwalior','MP',0,'19950214');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-25 13:15:13
