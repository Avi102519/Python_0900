#Create Database
CREATE DATABASE nit1;
use nit1;
#Create a table
create table student(
name varchar(30),
id int not null primary key,
address varchar(50),
marks int);

CREATE TABLE Friend(
Name varchar(30),
Phone int not null primary key,
City varchar(50));

SELECT * FROM STUDENT;
DESCRIBE STUDENT;
INSERT INTO STUDENT(NAME,ID,ADDRESS,MARKS) VALUES ('AVI','0717','SPRING HILL','23'); #SECURE WAY OF DATA INSERTION
INSERT INTO STUDENT VALUES('AIRA','1025','SPRING HILL','99'); #INSECURE WAY OF INSERTING DATA
INSERT INTO STUDENT VALUES('SWETHA,','1568','SPRING HILL','92'),('VINNIE,','1225','DUBLIN','95'),('KAVITA,','0621','DUBLIN','91'),('SOME','1116','PODILI','63');

SELECT 10+20;

USE NIT;
SELECT * FROM CUSTOMER;
SELECT * FROM CUSTOMER WHERE SALARY>5000; #To find list of customers with slary>5000
SELECT * FROM CUSTOMER WHERE SALARY = 2000; #To find a list of customers with salary = 2000
SELECT * FROM CUSTOMER WHERE SALARY != 2000; # To find a list of customers salary not equal to 2000
SELECT * FROM CUSTOMER WHERE SALARY<>2000; # To find a list of customers salary not equal to 2000
SELECT * FROM CUSTOMER WHERE SALARY>= 6500; #To find a list of customers whose salary is greater than or equal to 6500

# SQL logical Operations
SELECT * FROM CUSTOMER WHERE SALARY>6500 AND AGE>25; #Returns the rows with meet two conditions
SELECT * FROM CUSTOMER WHERE SALARY>=6500 OR AGE>25; #Returns the rows with one matching condition
SELECT * FROM CUSTOMER WHERE AGE IS NOT NULL; #Returns the rows where age is not null
SELECT * FROM CUSTOMER WHERE NAME LIKE 'K%'; #Returns the rows where customer name starts with 'K'
SELECT * FROM CUSTOMER WHERE AGE IN (25,27); # returns the customer rows with age 25 and 27
SELECT * FROM CUSTOMER WHERE AGE BETWEEN 25 and 30; # Returns the customer rows with age between 25 and 30
SELECT AGE FROM CUSTOMER WHERE EXISTS (SELECT AGE FROM CUSTOMER WHERE SALARY > 6500); #Returns only Age row with salary>6500
SELECT * FROM CUSTOMER WHERE AGE > ALL (SELECT AGE FROM CUSTOMER WHERE SALARY>6500);
SELECT * FROM CUSTOMER WHERE AGE > ANY (SELECT AGE FROM CUSTOMER WHERE SALARY>6500);

#SQL Expressions
SELECT COUNT(*) AS "RECORDS" FROM CUSTOMER; #Creating a new row with condition
SELECT current_timestamp(); #Selecting current timestamp
SELECT GETDATE; #Selecting current timestamp

#Drop or Delete database
DROP DATABASE NIT1;
#To select database
USE NIT1;
# TO Check available databases
SHOW DATABASES;

USE NIT;
#CREATE TABLE
CREATE TABLE MOVIE(
NAME VARCHAR(30),
YEAR INT NOT NULL PRIMARY KEY,
GENRE VARCHAR(50),
RATING INT);

DESC CUSTOMER; #customer table sorted by desc

#Populate one table using another table
INSERT INTO CUST (NAME,ID,AGE,ADDRESS,SALARY)
SELECT NAME,ID,AGE,ADDRESS,SALARY
FROM CUSTOMER
WHERE AGE >23;








