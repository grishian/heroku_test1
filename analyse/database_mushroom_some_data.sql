-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server versie:                10.6.5-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Versie:              11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumpen data van tabel test_mushroom.t_grow_run: ~5 rows (ongeveer)
DELETE FROM `t_grow_run`;
/*!40000 ALTER TABLE `t_grow_run` DISABLE KEYS */;
INSERT INTO `t_grow_run` (`PK_ID`, `F_CREATEON`, `F_UPDATEDON`, `F_NAME`, `F_MUSHROOM_ID`, `F_MUSHROOM_STAGE`, `F_GROW_START`, `F_SPAWN_START`, `F_FRUIT_START`, `F_IS_ACTIVE`) VALUES
	(1, '2022-03-11 12:01:04', '2022-03-11 12:01:04', 'button grow', 2, 'active', '2022-03-11 12:01:04', NULL, NULL, 'not_active'),
	(2, '2022-03-11 12:12:57', '2022-03-11 14:03:46', 'elm grow', 4, 'fruiting', '2022-03-11 12:12:57', NULL, NULL, 'not_active'),
	(3, '2022-03-11 14:06:16', '2022-03-11 14:08:11', 'oyster grow', 3, 'fruiting', '2022-03-11 14:06:16', NULL, NULL, 'not_active'),
	(4, '2022-03-11 14:08:11', '2022-03-11 14:11:16', 'shiitake', 1, 'fruiting', '2022-03-11 14:08:11', NULL, NULL, 'not_active'),
	(5, '2022-03-11 14:11:16', '2022-03-11 15:21:54', 'nieuwste grow', 5, 'fruiting', '2022-03-11 14:11:16', NULL, NULL, 'not_active'),
	(6, '2022-03-11 15:21:54', '2022-03-11 15:21:54', 'crash ofni', 1, 'fruiting', '2022-03-11 15:21:54', NULL, NULL, 'active');
/*!40000 ALTER TABLE `t_grow_run` ENABLE KEYS */;

-- Dumpen data van tabel test_mushroom.t_mushroom: ~5 rows (ongeveer)
DELETE FROM `t_mushroom`;
/*!40000 ALTER TABLE `t_mushroom` DISABLE KEYS */;
INSERT INTO `t_mushroom` (`PK_ID`, `F_CREATEON`, `F_UPDATEDON`, `F_NAME`, `F_SPAWN_TEMP`, `F_FRUIT_TEMP`, `F_SPAWN_FAE`, `F_FRUIT_FAE`) VALUES
	(1, '2022-03-10 10:44:19', '2022-03-10 10:44:19', 'shiitake', 22, 20, 5, 10),
	(2, '2022-04-10 10:46:12', '2022-04-10 10:46:12', 'button', 20, 20, 5, 5),
	(3, '2022-05-10 11:44:19', '2022-05-10 10:44:19', 'oyster', 22, 20, 5, 10),
	(4, '2022-06-10 11:44:19', '2022-06-10 11:44:19', 'elm', 22, 20, 5, 10),
	(5, '2022-07-10 12:46:12', '2022-07-10 12:46:12', 'turkey_tail', 20, 20, 5, 5);
/*!40000 ALTER TABLE `t_mushroom` ENABLE KEYS */;

-- Dumpen data van tabel test_mushroom.t_temperature: ~5 rows (ongeveer)
DELETE FROM `t_temperature`;
/*!40000 ALTER TABLE `t_temperature` DISABLE KEYS */;
INSERT INTO `t_temperature` (`PK_ID`, `F_CREATEON`, `F_UPDATEDON`, `F_CELSIUS`, `F_GROW_RUN_ID`) VALUES
	(1, '2022-03-10 10:55:29', '2022-03-10 10:55:29', 25, 5),
	(2, '2022-03-11 10:55:29', '2022-03-11 10:55:29', 24, 5),
	(3, '2022-03-12 10:55:29', '2022-03-12 10:55:29', 27, 5),
	(4, '2022-03-13 10:55:29', '2022-03-13 10:55:29', 23, 5),
	(5, '2022-03-14 10:55:29', '2022-03-14 10:55:29', 20, 5);
/*!40000 ALTER TABLE `t_temperature` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
