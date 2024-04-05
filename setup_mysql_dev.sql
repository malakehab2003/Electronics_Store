-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS `electronic-store`;
CREATE USER IF NOT EXISTS 'alx'@'localhost' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON `electronic-store`.* TO 'alx'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'alx'@'localhost';
FLUSH PRIVILEGES;
