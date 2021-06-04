-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 11, 2021 at 03:30 AM
-- Server version: 5.7.31
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `delivero`
--

-- --------------------------------------------------------

--
-- Table structure for table `food`
--

DROP TABLE IF EXISTS `food`;
CREATE TABLE IF NOT EXISTS `food` (
  `Food_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Res_ID` int(11) NOT NULL,
  `Dish` varchar(30) NOT NULL,
  `Price` int(11) NOT NULL,
  PRIMARY KEY (`Food_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=152 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `food`
--

INSERT INTO `food` (`Food_ID`, `Res_ID`, `Dish`, `Price`) VALUES
(1, 1, 'Sweet Corn Soup ', 80),
(2, 1, 'Manchow Soup', 80),
(3, 1, 'Asparagus Soup', 90),
(4, 1, 'Mutton Paya Soup', 120),
(5, 1, 'Hara Bhara Kabab', 150),
(6, 1, 'Mix Veg Pakoda', 100),
(7, 1, 'Paneer Pakoda', 150),
(8, 1, 'Aloo Jeera Dry ', 120),
(9, 1, 'Schezwan Sauce', 25),
(10, 1, 'Egg Omelete ', 60),
(11, 1, 'Egg Bhurji', 60),
(12, 1, 'Fish Tawa Fry', 220),
(13, 1, 'Fish Tandoori', 240),
(14, 1, 'Barbeque Chicken', 190),
(15, 1, 'Chicken Lollipop', 180),
(16, 1, 'Chicken Chilly', 180),
(17, 1, 'Soya fried Chicken', 170),
(18, 1, 'Paneer Sate', 160),
(19, 1, 'Paneer Chilli', 170),
(20, 1, 'Veg 65', 180),
(21, 1, 'Chicken Tikka Roll', 140),
(22, 1, 'Paneer Tikka Roll', 120),
(23, 1, 'Chicken Roll ', 95),
(24, 1, 'Checken Egg Roll', 110),
(25, 1, 'Mix Veg Roll', 110),
(26, 1, 'Mix Veg Grill Platter', 440),
(27, 1, 'Chicken Grill Platter', 600),
(28, 1, 'Chicken Tandoori', 270),
(29, 1, 'Mutton Seekh Kabab', 190),
(30, 1, 'Stuffed Mushroom ', 210),
(31, 1, 'Chicken Malai Kabab', 210),
(32, 1, 'Jaipuri Kofta', 190),
(33, 1, 'Mushroom Masala', 160),
(34, 1, 'Paneer Palak', 170),
(35, 1, 'Shahi Paneer', 190),
(36, 1, 'Dal fry', 120),
(37, 1, 'Dal Makhani ', 140),
(38, 1, 'Chickwn Handi Full', 480),
(39, 1, 'Chicken Handi  Half', 280),
(40, 1, 'Chicken Koyla', 220),
(41, 1, 'Chicken Mughlai', 200),
(42, 1, 'Chicken Do Pyaza', 200),
(43, 1, 'Butter Chicken', 210),
(44, 1, 'Mutton Masala ', 210),
(45, 1, 'Mutton Kolhapuri', 220),
(46, 1, 'Mutton Do Pyaza', 210),
(47, 1, 'Mutton Keema', 240),
(48, 1, 'Mutton Biryani ', 270),
(49, 1, 'Chicken Biryani', 170),
(50, 1, 'Chicken Dum Biryani', 180),
(51, 1, 'Mutton Dum Biryani', 280),
(52, 1, 'Veg Biryani', 150),
(53, 1, 'Veg Dum Biryani', 160),
(54, 1, 'Jeera Rice ', 100),
(55, 1, 'Steam Rice', 80),
(56, 1, 'Kakdi Salad', 30),
(57, 1, 'Lassi', 60),
(58, 1, 'Buttermilk', 35),
(59, 1, 'Roti', 15),
(60, 1, 'Butter Roti', 20),
(61, 1, 'Paratha', 25),
(62, 1, 'Aloo Paratha', 40),
(63, 1, 'Naan', 30),
(64, 1, 'Butter Naan', 35),
(65, 1, 'Roti Ki Tokri', 150),
(66, 1, 'Triple Schezwan Rice', 150),
(67, 1, 'Stewed Rice', 170),
(68, 1, 'Pan Fried Rice', 160),
(69, 2, 'Matar PAneer', 110),
(70, 2, 'Shahi Paneer', 135),
(71, 2, 'Palak Paneer', 110),
(72, 2, 'Paneer Lababdar', 140),
(73, 2, 'Paneer Chilly', 125),
(74, 2, 'Dal Tadka', 80),
(75, 2, 'Rice', 60),
(76, 2, 'Tawa Roti', 10),
(77, 3, 'Chicekn Tandoori', 170),
(78, 3, 'Chicken Tikka', 180),
(79, 3, 'Paneer Tikka', 150),
(80, 3, 'Chicken Thali', 170),
(81, 3, 'Mutton Thali ', 210),
(82, 3, 'Veg Thali', 150),
(83, 3, 'Chicken Biryani', 130),
(84, 3, 'Mutton Biryani ', 150),
(85, 3, 'Plain Rice', 60),
(86, 3, 'Jeera Rice ', 70),
(87, 3, 'Chicken Curry', 120),
(88, 3, 'Kadai Chicken', 130),
(89, 3, 'Chicken Butter Masala', 130),
(90, 3, 'Chicken kali Mirch', 130),
(91, 3, 'Chicken Tawa Masala', 170),
(92, 3, 'Mutton Masala ', 160),
(93, 3, 'Mutton Curry', 170),
(94, 3, 'Chicken manchurian', 200),
(95, 3, 'Chicken Chilli', 190),
(96, 3, 'Paneer Manchurian', 180),
(97, 3, 'Paneer Chilli', 150),
(98, 3, 'Egg Fried Rice', 75),
(99, 3, 'Chicken Fried Rice', 85),
(100, 3, 'Egg Curry', 70),
(101, 2, 'Egg Roll', 50),
(102, 3, 'Double Chicken Roll', 90),
(103, 3, 'Matar Paneer', 180),
(104, 3, 'Paneer Butter Masala', 200),
(105, 3, 'Kadai Paneer', 220),
(106, 3, 'Dal Fry', 50),
(107, 3, 'Dal Tadka', 70),
(108, 3, 'Mix Veg', 80),
(109, 3, 'Chicken Hot Soup', 110),
(110, 3, 'Tomato Soup', 90),
(111, 3, 'Manchow Soup', 110),
(112, 3, 'Tandoori roti', 15),
(113, 3, 'Naan', 30),
(114, 3, 'Butter Naan', 35),
(115, 3, 'Tawa Roti', 8),
(116, 3, 'Butter Tawa Roti', 12),
(117, 4, 'Paneer Butter Masala', 110),
(118, 4, 'Mattar Paneer', 110),
(119, 4, 'Kadai Paneer', 200),
(120, 4, 'Handi Paneer', 200),
(121, 4, 'Paneer Do Pyaza', 190),
(122, 4, 'Paneer Lababdar', 190),
(123, 4, 'Shahi Paneer', 210),
(124, 4, 'Palak Paneer', 190),
(125, 4, 'Paneer Korma', 190),
(126, 4, 'Aloo Dum banarasi', 130),
(127, 4, 'Aloo Jeera Dry ', 90),
(128, 4, 'Paneer Mushroom Butter Masala', 220),
(129, 4, 'Mushroom Masala', 210),
(130, 4, 'Mushroom Pees kari', 200),
(131, 4, 'Mix veg', 140),
(132, 4, 'Veg Jhal Fry', 150),
(133, 4, 'Malai Kofta', 210),
(134, 4, 'Kaju Kari', 240),
(135, 4, 'Paneer Jaipuri', 200),
(136, 4, 'Chola Bhatura', 70),
(137, 4, 'Veg Burger', 50),
(138, 4, 'Paneer Burger', 60),
(139, 4, 'Cheese Burger', 80),
(140, 4, 'Pav Bhaji', 80),
(141, 4, 'Veg Pizza', 120),
(142, 4, 'Chilli Paneer', 190),
(143, 4, 'Veg Spring Roll', 130),
(144, 4, 'Paneer Spring Roll', 150),
(145, 4, 'Idli ', 40),
(146, 4, 'Idli Fry', 60),
(147, 4, 'Masala Dosa', 60),
(148, 4, 'Paper Dosa', 40),
(149, 4, 'Utpam Onion', 60),
(150, 4, 'Sambhar Bada', 50),
(151, 4, 'Shahi Paneer Dosa', 140);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
CREATE TABLE IF NOT EXISTS `orders` (
  `Order_ID` int(11) NOT NULL AUTO_INCREMENT,
  `CUST_NUM` varchar(15) NOT NULL,
  `DATE` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `COST` int(11) NOT NULL,
  PRIMARY KEY (`Order_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`Order_ID`, `CUST_NUM`, `DATE`, `COST`) VALUES
(1, '9876543210', '2021-01-07 00:00:00', 150),
(2, '9876543210', '2021-01-07 10:04:03', 300),
(3, '9876543210', '2021-01-07 10:23:43', 980),
(4, '9876543210', '2021-01-11 20:35:11', 200),
(5, '9876543210', '2021-01-11 20:36:12', 1070),
(6, '9876543210', '2021-01-24 22:02:27', 840),
(7, '9876543210', '2021-03-08 22:56:21', 295);

-- --------------------------------------------------------

--
-- Table structure for table `order_detail`
--

DROP TABLE IF EXISTS `order_detail`;
CREATE TABLE IF NOT EXISTS `order_detail` (
  `Order_ID` int(11) NOT NULL,
  `Food_ID` int(11) NOT NULL,
  `QTY` int(11) NOT NULL,
  PRIMARY KEY (`Order_ID`,`Food_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `order_detail`
--

INSERT INTO `order_detail` (`Order_ID`, `Food_ID`, `QTY`) VALUES
(1, 52, 1),
(2, 65, 2),
(3, 39, 2),
(3, 62, 4),
(3, 126, 2),
(4, 94, 1),
(5, 7, 1),
(5, 19, 2),
(5, 35, 2),
(5, 94, 1),
(6, 39, 3),
(7, 2, 2),
(7, 7, 1),
(7, 38, 2),
(7, 39, 1),
(7, 120, 1);

-- --------------------------------------------------------

--
-- Table structure for table `restaurants`
--

DROP TABLE IF EXISTS `restaurants`;
CREATE TABLE IF NOT EXISTS `restaurants` (
  `Res_ID` int(11) NOT NULL,
  `Res_Name` varchar(40) NOT NULL,
  PRIMARY KEY (`Res_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `restaurants`
--

INSERT INTO `restaurants` (`Res_ID`, `Res_Name`) VALUES
(1, 'Seven Star Hotel'),
(2, 'Swaad House'),
(3, 'Family Dhaba'),
(4, 'Chominoz Restuarant');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `Email` varchar(30) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `password` varchar(30) NOT NULL,
  PRIMARY KEY (`Phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`Email`, `Phone`, `Name`, `password`) VALUES
('', '', '', ''),
('test2@test2.com', '0123456789', 'Test2', 'Test@2'),
('test3@test3.com', '1234567890', 'Test', 'Test@3'),
('test1@test1.com', '9876543210', 'Test1', 'Test@1');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
