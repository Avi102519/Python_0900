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

use NIT;
SELECT * FROM STUDENT;
INSERT INTO STUDENT VALUES('SAM',12,'HYD',56);

#06/10--And and or operators
SELECT * FROM CUSTOMER WHERE ID >=5 AND SALARY <=6000;

SELECT * FROM CUSTOMER WHERE ID >=5 OR SALARY <=6000;
#TO UPDATE THE ENTOIRE ROW
UPDATE STUDENT SET salary = '10000';

UPDATE STUDENT SET ADDRESS = 'Delhi' WHERE ID = 37; 
ALTER TABLE STUDENT ADD PHONENO INT;
UPDATE STUDENT SET PHONENO = 123; 
UPDATE STUDENT SET PHONENO = '456' WHERE ID IN (55); 

DESCRIBE STUDENT;
ALTER TABLE STUDENT MODIFY COLUMN ADDRESS VARCHAR(100);
ALTER TABLE STUDENT DROP COLUMN PHONENO;

SELECT * FROM STUDENT;
DELETE FROM STUDENT WHERE name = 'Kodi';

SELECT SUM(MARKS) FROM STUDENT;
SELECT AVG(MARKS) FROM STUDENT;
SELECT MAX(MARKS) FROM STUDENT;
SELECT MIN(MARKS) FROM STUDENT;
SELECT COUNT(MARKS) FROM STUDENT;
SELECT * FROM STUDENT ORDER BY MARKS; #ASCENDING ORDER
SELECT * FROM STUDENT ORDER BY MARKS DESC;
SELECT * FROM STUDENT WHERE NAME LIKE 'P%';
SELECT * FROM STUDENT WHERE NAME LIKE '%Y';
SELECT * FROM STUDENT WHERE NAME LIKE 'PR_%';
use nit;
select * from emp;

#TOP Clause
Select Top3 * FROM customer;

SELECT * FROM CUSTOMER LIMIT 3;
#SPECIFIED NUMBER OF ROWS WITH NUMERIC CONFIG;

SELECT * FROM CUSTOMER WHERE ROWNUM<=3;

#The SQL group by clause used in collaboration with select statement to arrange identical data groups.
SELECT NAME FROM CUSTOMERS GROUP BY NAME ORDER BY NAME;

#DISTINCT KEYWORD USED TO CONJGATE WITH SELECT STATEMENT TO ELIMINATE ALL THE DUPLICATE RECORDS AND FETCHING ONLY UNIQUE RECORDS

SELECT DISTINCT SALARY FROM CUSTOMER ORDER BY SALARY;
#SQL SORTING
SELECT * FROM CUSTOMER ORDER BY NAME, SALARY;



#JOINS

describe emp;

create table employee(id int not null primary key,Salary int, empcode int,name varchar(30));
insert into employee values (12,20000,102,'aman'),(23,60000,104,'arup'),(78,30000,105,'max'),(80,25000,103,'ram'),(34,90000,106,'sam');
select * from employee;
select * from student;

select * from student inner join employee on student.id = employee.id; #Common items available in two tables
select * from student inner join employee on employee.id = student.id;
select * from student left join employee on student.id = employee.id;
select * from student left join employee on employee.id = student.id;

select * from student right join employee on employee.id = student.id;
select * from student cross join employee;

