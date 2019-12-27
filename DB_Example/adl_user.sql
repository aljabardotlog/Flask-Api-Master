/*
 Navicat Premium Data Transfer

 Source Server         : [mysql]127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 80012
 Source Host           : 127.0.0.1:3306
 Source Schema         : adl_user

 Target Server Type    : MySQL
 Target Server Version : 80012
 File Encoding         : 65001

 Date: 28/12/2019 05:29:39
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for adl_user
-- ----------------------------
DROP TABLE IF EXISTS `adl_user`;
CREATE TABLE `adl_user` (
  `kd_user` int(30) NOT NULL AUTO_INCREMENT,
  `kd_user_group` int(30) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `nama` text,
  `login` datetime NOT NULL,
  `logout` datetime NOT NULL,
  `status` char(1) NOT NULL,
  PRIMARY KEY (`kd_user`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for adl_user_group
-- ----------------------------
DROP TABLE IF EXISTS `adl_user_group`;
CREATE TABLE `adl_user_group` (
  `kd_user_group` int(30) NOT NULL AUTO_INCREMENT,
  `nm_group` varchar(50) NOT NULL,
  `kt_group` text NOT NULL,
  PRIMARY KEY (`kd_user_group`) USING BTREE,
  KEY `kd` (`kd_user_group`) USING BTREE,
  KEY `group` (`nm_group`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for menu
-- ----------------------------
DROP TABLE IF EXISTS `menu`;
CREATE TABLE `menu` (
  `kd_menu` int(30) NOT NULL AUTO_INCREMENT,
  `group_menu` varchar(30) NOT NULL,
  `name` text NOT NULL,
  `nickname` varchar(3) NOT NULL,
  `class` text NOT NULL,
  `icon` text NOT NULL,
  `posisi` int(30) NOT NULL,
  PRIMARY KEY (`kd_menu`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for menu_sub
-- ----------------------------
DROP TABLE IF EXISTS `menu_sub`;
CREATE TABLE `menu_sub` (
  `kd_menu_sub` int(30) NOT NULL AUTO_INCREMENT,
  `kd_menu` int(30) NOT NULL,
  `name` text NOT NULL,
  `class` text NOT NULL,
  `posisi` int(5) NOT NULL,
  PRIMARY KEY (`kd_menu_sub`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for menu_user
-- ----------------------------
DROP TABLE IF EXISTS `menu_user`;
CREATE TABLE `menu_user` (
  `kd_menu_user` int(30) NOT NULL AUTO_INCREMENT,
  `kd_user` int(30) NOT NULL,
  `kd_menu` int(30) NOT NULL,
  `kd_menu_sub` int(30) NOT NULL,
  PRIMARY KEY (`kd_menu_user`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

SET FOREIGN_KEY_CHECKS = 1;
