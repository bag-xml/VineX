-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 12, 2025 at 12:53 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vinexdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `commentID` int(11) NOT NULL,
  `authorID` int(11) NOT NULL,
  `postID` int(11) NOT NULL,
  `comment` varchar(500) NOT NULL,
  `creationDate` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `likes`
--

CREATE TABLE `likes` (
  `likeId` int(11) NOT NULL,
  `userId` int(11) NOT NULL,
  `postID` int(11) NOT NULL,
  `username` varchar(32) NOT NULL,
  `avatarURL` varchar(500) NOT NULL,
  `creationDate` varchar(25) NOT NULL,
  `location` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--

CREATE TABLE `notifications` (
  `notificationID` int(11) NOT NULL,
  `notificationType` int(1) NOT NULL,
  `userID` int(11) NOT NULL,
  `authorID` int(11) NOT NULL,
  `postID` int(11) NOT NULL,
  `commentID` int(11) NOT NULL,
  `sender_username` varchar(50) NOT NULL,
  `message` varchar(100) NOT NULL,
  `creationDate` varchar(25) NOT NULL,
  `avatarURL` varchar(500) NOT NULL DEFAULT 'http://vine-x.bag-xml.com/static/pfps/7bc6c93de0ad70ec51a42f5c6277be2496d4c90b0a4ad00b726f096d0e661797.png',
  `thumbnailURL` varchar(500) NOT NULL,
  `adminMessage` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `postID` int(11) NOT NULL,
  `authorID` int(11) NOT NULL,
  `authorName` varchar(50) NOT NULL,
  `thumbnailURL` varchar(500) NOT NULL,
  `videoURL` varchar(500) NOT NULL,
  `location` varchar(120) NOT NULL,
  `description` varchar(80) NOT NULL,
  `creationDate` varchar(25) NOT NULL,
  `comments` longtext NOT NULL,
  `likes` longtext NOT NULL,
  `tags` longtext NOT NULL,
  `usersWhoLiked` longtext NOT NULL DEFAULT '{"liked": []}',
  `verified` tinyint(1) NOT NULL DEFAULT 0,
  `promoted` tinyint(1) NOT NULL DEFAULT 0,
  `postToFacebook` int(11) NOT NULL DEFAULT 0,
  `foursquareVenueID` int(11) NOT NULL DEFAULT 0,
  `authorPFP` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `uniqueIdentifier` varchar(50) NOT NULL,
  `password` varchar(64) NOT NULL,
  `email` varchar(60) NOT NULL,
  `phoneNumber` int(11) NOT NULL,
  `username` varchar(32) NOT NULL,
  `description` varchar(60) NOT NULL,
  `pfp` longtext NOT NULL,
  `location` varchar(32) NOT NULL,
  `followingCount` int(11) NOT NULL,
  `followerCount` int(11) NOT NULL,
  `likeCount` int(11) NOT NULL,
  `postCount` int(11) NOT NULL,
  `blocked` longtext NOT NULL DEFAULT '{"blocked":[]}',
  `following` longtext NOT NULL DEFAULT '{"following":[]}',
  `followers` longtext NOT NULL DEFAULT '{"followers":[]}',
  `likedPosts` longtext NOT NULL DEFAULT '{"liked_posts":[]}',
  `pending_notifications_count` int(11) NOT NULL DEFAULT 0,
  `promo` tinyint(1) NOT NULL DEFAULT 0,
  `isPrivate` tinyint(1) NOT NULL DEFAULT 0,
  `isVerified` tinyint(1) NOT NULL DEFAULT 0,
  `isAdmin` tinyint(1) NOT NULL DEFAULT 0,
  `AdminKey` varchar(12) NOT NULL,
  `isBanned` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`commentID`);

--
-- Indexes for table `likes`
--
ALTER TABLE `likes`
  ADD PRIMARY KEY (`likeId`);

--
-- Indexes for table `notifications`
--
ALTER TABLE `notifications`
  ADD PRIMARY KEY (`notificationID`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`postID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `commentID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `likes`
--
ALTER TABLE `likes`
  MODIFY `likeId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `notifications`
--
ALTER TABLE `notifications`
  MODIFY `notificationID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `postID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
