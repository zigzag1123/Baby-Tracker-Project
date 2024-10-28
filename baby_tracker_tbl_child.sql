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
-- Table structure for table `tbl_child`
--

DROP TABLE IF EXISTS `tbl_child`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_child` (
  `fld_c_id_pk` int NOT NULL AUTO_INCREMENT,
  `fld_c_fname` varchar(48) DEFAULT NULL,
  `fld_c_lname` varchar(48) DEFAULT NULL,
  `fld_c_p_username_fk` varchar(48) DEFAULT NULL,
  `fld_c_doc` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`fld_c_id_pk`),
  KEY `c_fk` (`fld_c_p_username_fk`),
  CONSTRAINT `c_fk` FOREIGN KEY (`fld_c_p_username_fk`) REFERENCES `tbl_parents` (`fld_p_username_pk`),
  CONSTRAINT `c_not_null` CHECK (((`fld_c_fname` is not null) and (`fld_c_lname` is not null)))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_child`
--

LOCK TABLES `tbl_child` WRITE;
/*!40000 ALTER TABLE `tbl_child` DISABLE KEYS */;
INSERT INTO `tbl_child` VALUES (1,'Charles','Schwab','jhs0137','2024-10-02 18:35:00'),(2,'Henry','Schwab','jhs0137','2024-10-02 18:54:09');
/*!40000 ALTER TABLE `tbl_child` ENABLE KEYS */;
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
