create database user;
use  user;
create table student(
id int auto_increment  primary key,
fname varchar(100),
rollno varchar(10),
email varchar(40),
phno varchar(10),
dept varchar(30),
degree varchar(10),
gender varchar(10)
);
drop table student;
insert into student (fname,rollno,email,phno,dept,degree,gender) values('bharath','20l109','bharath@gmail.com','9360334722','BE','ECE','Male');
insert into student (fname,rollno,email,phno,dept,degree,gender) values('surya','20l154','surya@gmail.com','9360334722','BE','ECE','Male');
insert into student (fname,rollno,email,phno,dept,degree,gender) values('gokul' ,'20l115','gokul@gmail.com','9360334722','BE','ECE','Male');
insert into student (fname,rollno,email,phno,dept,degree,gender) values('sudhan','20l117','sudhan@gmail.com','9360334722','BE','ECE','Male');
select * from student;