-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 192.168.1.54    Database: baby_tracker
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `tbl_event_data`
--

DROP TABLE IF EXISTS `tbl_event_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_event_data` (
  `fld_e_id_pk` int NOT NULL AUTO_INCREMENT,
  `fld_c_id_fk` int DEFAULT NULL,
  `fld_event_time` varchar(17) DEFAULT NULL,
  `fld_event_type` varchar(15) DEFAULT NULL,
  `fld_e_doc` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`fld_e_id_pk`),
  KEY `e_d_fk` (`fld_c_id_fk`),
  CONSTRAINT `e_d_fk` FOREIGN KEY (`fld_c_id_fk`) REFERENCES `tbl_child` (`fld_c_id_pk`),
  CONSTRAINT `e_d_not_null` CHECK ((`fld_c_id_fk` is not null))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_event_data`
--

LOCK TABLES `tbl_event_data` WRITE;
/*!40000 ALTER TABLE `tbl_event_data` DISABLE KEYS */;
INSERT INTO `tbl_event_data` VALUES (3,1,'09 30 2024  02:22','Sleep','2024-10-02 18:48:15'),(4,1,'09 30 2024  06:22','Awake','2024-10-02 18:48:15'),(6,1,'10 01 2024  06:22','Sleep','2024-10-02 19:47:24'),(7,1,'10 01 2024  12:22','Awake','2024-10-02 19:51:25'),(8,2,'10 01 2024  08:22','Sleep','2024-10-02 21:50:09'),(9,2,'10 01 2024  14:22','Awake','2024-10-02 21:50:17'),(10,1,'10 02 2024  13:12','Sleep','2024-10-02 22:24:35'),(11,1,'10 02 2024  21:25','Awake','2024-10-02 22:25:22');
/*!40000 ALTER TABLE `tbl_event_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-22 22:12:00
