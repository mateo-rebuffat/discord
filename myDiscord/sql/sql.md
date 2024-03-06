```sql
mysql> SHOW TABLES;
+-------------------+
| Tables_in_discord |
+-------------------+
| account           |
| channels          |
| role              |
| users             |
+-------------------+
4 rows in set (0.01 sec)

mysql> DESCRIBE account;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| username | varchar(255) | NO   |     | NULL    |                |
| name     | varchar(255) | NO   |     | NULL    |                |
| lastname | varchar(255) | NO   |     | NULL    |                |
| email    | varchar(255) | NO   | UNI | NULL    |                |
| password | varchar(255) | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
6 rows in set (0.00 sec)

mysql> DESCRIBE channels;
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| channel_id  | int          | NO   | PRI | NULL    |       |
| nom_channel | varchar(255) | YES  |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

mysql> DESCRIBE role;
+----------+--------------+------+-----+---------+-------+
| Field    | Type         | Null | Key | Default | Extra |
+----------+--------------+------+-----+---------+-------+
| role_id  | int          | NO   | PRI | NULL    |       |
| nom_role | varchar(255) | YES  |     | NULL    |       |
+----------+--------------+------+-----+---------+-------+
2 rows in set (0.01 sec)

mysql> DESCRIBE users;
+---------+-----------------+------+-----+---------+----------------+
| Field   | Type            | Null | Key | Default | Extra          |
+---------+-----------------+------+-----+---------+----------------+
| id      | int             | NO   | PRI | NULL    | auto_increment |
| user_id | bigint unsigned | YES  | UNI | NULL    |                |
| name    | varchar(255)    | YES  |     | NULL    |                |
| points  | int             | YES  |     | 0       |                |
+---------+-----------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
