-- MySQL serverinde user_0d_1 isdifadecisini yaradir ve ona butun huquqlari verir
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
