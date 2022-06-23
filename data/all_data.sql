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

-- Dumpen data van tabel incubator.alembic_version: ~1 rows (ongeveer)
DELETE FROM `alembic_version`;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` (`version_num`) VALUES
	('c6efbcc24001');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;

-- Dumpen data van tabel incubator.grow_run: ~0 rows (ongeveer)
DELETE FROM `grow_run`;
/*!40000 ALTER TABLE `grow_run` DISABLE KEYS */;
INSERT INTO `grow_run` (`id`, `mushroom_id`, `mushroom_stage`, `grow_start`, `spawn_start`, `fruit_start`, `active`) VALUES
	(1, 1, 0, '2022-05-19 16:31:04', NULL, NULL, 1);
/*!40000 ALTER TABLE `grow_run` ENABLE KEYS */;

-- Dumpen data van tabel incubator.mushroom: ~7 rows (ongeveer)
DELETE FROM `mushroom`;
/*!40000 ALTER TABLE `mushroom` DISABLE KEYS */;
INSERT INTO `mushroom` (`id`, `name`, `spawn_temp`, `fruit_temp`, `spawn_fae`, `fruit_fae`, `mushroom_img`) VALUES
	(1, 'shiitake', 20, 20, 5, 5, 'https://www.dewassendemaan.be/sites/default/files/producten/Shiitake.jpg'),
	(2, 'elm', 20, 20, 5, 5, 'https://m.media-amazon.com/images/I/51VsNXHvYSL._AC_SY1000_.jpg'),
	(3, 'blue oyser', 20, 20, 5, 5, 'https://agro-market24.eu/uploads/photos/39210/sprzedam_mushrooms-fresh-forest%20mushrooms%20-oyster%20mushrooms-_agro-marke24_gie%C5%82da%20rolna-963097-39210.jpg'),
	(4, 'pink oyster', 20, 20, 5, 5, 'https://www.gourmetmushrooms.co.uk/wp-content/uploads/2019/09/Pink-Oyster-Sqaure.jpg'),
	(5, 'golden oyster', 20, 20, 5, 5, 'https://www.beaconhillmushrooms.co.uk/wp-content/uploads/elementor/thumbs/goysterimg-p8bporkivcw61pvx6m55seakrht8t3t62kwxa428io.jpg'),
	(6, 'lion\'s mane', 20, 20, 5, 5, 'https://www.beaconhillmushrooms.co.uk/wp-content/uploads/elementor/thumbs/LM-PR-e1639499941684-phiep7lowx7op6vledc5n44ek1ck9lgxeu0ublkalc.jpg'),
	(7, 'beefsteak', 20, 20, 5, 5, 'https://www.beaconhillmushrooms.co.uk/wp-content/uploads/elementor/thumbs/beefsteak-polypore-p8bpqjhjs3bnz7b2tdrshy5x5p27ciuwzd9xwxfgrk.jpg');
/*!40000 ALTER TABLE `mushroom` ENABLE KEYS */;

-- Dumpen data van tabel incubator.temperature: ~16 rows (ongeveer)
DELETE FROM `temperature`;
/*!40000 ALTER TABLE `temperature` DISABLE KEYS */;
INSERT INTO `temperature` (`id`, `celsius`, `grow_run_id`, `created_on`) VALUES
	(1, 18, 1, '2022-05-28 16:16:19'),
	(2, 22, 1, '2022-05-19 16:41:06'),
	(3, 23, 1, '2022-05-19 22:11:07'),
	(4, 24, 1, '2022-05-19 22:11:46'),
	(5, 25, 1, '2022-05-19 22:11:58'),
	(6, 24, 1, '2022-05-18 22:12:11'),
	(8, 25, 1, '2022-05-21 16:12:03'),
	(9, 26, 1, '2022-05-21 16:15:59'),
	(10, 24, 1, '2022-05-21 16:16:49'),
	(11, 22, 1, '2022-05-21 16:16:58'),
	(12, 20, 1, '2022-05-21 16:17:07'),
	(13, 19, 1, '2022-05-21 16:17:34'),
	(14, 20, 1, '2022-05-21 16:17:46'),
	(15, 21, 1, '2022-05-21 16:18:02'),
	(16, 20, 1, '2022-05-21 16:18:11'),
	(17, 21, 1, '2022-05-21 16:18:16');
/*!40000 ALTER TABLE `temperature` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
