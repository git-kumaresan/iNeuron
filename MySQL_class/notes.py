show databases;
create database ineuron;
show databases;
use ineuron;

create table bank_details (age int, job varchar(30), marital varchar(30), education varchar(30), `default` varchar(30),	balance int, housing varchar(30), loan varchar(30),	contact varchar(30), `day` int,	`month` varchar(30),	duration int,	campaign int,	pdays int,	previous int, poutcome varchar(30),	y varchar(30)) ;

create table if not exists bank_details (age int, job varchar(30), marital varchar(30), education varchar(30), `default` varchar(30),	balance int, housing varchar(30), loan varchar(30),	contact varchar(30), `day` int,	`month` varchar(30),	duration int,	campaign int,	pdays int,	previous int, poutcome varchar(30),	y varchar(30)) ;

show tables;

Describe bank_details

insert into bank_details values(58,"management","married","tertiary","no",2143,"yes","no","unknown",5,"may",261,1,-1,0,"unknown","no")

select * from bank_details ;
select * from bank_details ;

insert into bank_details values (44,"technician","single","secondary","no",29,"yes","no","unknown",5,"may",151,1,-1,0,"unknown","no"),
(33,"entrepreneur","married","secondary","no",2,"yes","yes","unknown",5,"may",76,1,-1,0,"unknown","no"),
(47,"blue-collar","married","unknown","no",1506,"yes","no","unknown",5,"may",92,1,-1,0,"unknown","no"),
(33,"unknown","single","unknown","no",1,"no","no","unknown",5,"may",198,1,-1,0,"unknown","no"),
(35,"management","married","tertiary","no",231,"yes","no","unknown",5,"may",139,1,-1,0,"unknown","no"),
(28,"management","single","tertiary","no",447,"yes","yes","unknown",5,"may",217,1,-1,0,"unknown","no"),
(42,"entrepreneur","divorced","tertiary","yes",2,"yes","no","unknown",5,"may",380,1,-1,0,"unknown","no"),
(58,"retired","married","primary","no",121,"yes","no","unknown",5,"may",50,1,-1,0,"unknown","no"),
(43,"technician","single","secondary","no",593,"yes","no","unknown",5,"may",55,1,-1,0,"unknown","no"),
(41,"admin.","divorced","secondary","no",270,"yes","no","unknown",5,"may",222,1,-1,0,"unknown","no"),
(29,"admin.","single","secondary","no",390,"yes","no","unknown",5,"may",137,1,-1,0,"unknown","no"),
(53,"technician","married","secondary","no",6,"yes","no","unknown",5,"may",517,1,-1,0,"unknown","no"),
(58,"technician","married","unknown","no",71,"yes","no","unknown",5,"may",71,1,-1,0,"unknown","no"),
(57,"services","married","secondary","no",162,"yes","no","unknown",5,"may",174,1,-1,0,"unknown","no"),
(51,"retired","married","primary","no",229,"yes","no","unknown",5,"may",353,1,-1,0,"unknown","no"),
(45,"admin.","single","unknown","no",13,"yes","no","unknown",5,"may",98,1,-1,0,"unknown","no"),
(57,"blue-collar","married","primary","no",52,"yes","no","unknown",5,"may",38,1,-1,0,"unknown","no"),
(60,"retired","married","primary","no",60,"yes","no","unknown",5,"may",219,1,-1,0,"unknown","no"),
(33,"services","married","secondary","no",0,"yes","no","unknown",5,"may",54,1,-1,0,"unknown","no"),
(28,"blue-collar","married","secondary","no",723,"yes","yes","unknown",5,"may",262,1,-1,0,"unknown","no"),
(56,"management","married","tertiary","no",779,"yes","no","unknown",5,"may",164,1,-1,0,"unknown","no"),
(32,"blue-collar","single","primary","no",23,"yes","yes","unknown",5,"may",160,1,-1,0,"unknown","no"),
(25,"services","married","secondary","no",50,"yes","no","unknown",5,"may",342,1,-1,0,"unknown","no"),
(40,"retired","married","primary","no",0,"yes","yes","unknown",5,"may",181,1,-1,0,"unknown","no"),
(44,"admin.","married","secondary","no",-372,"yes","no","unknown",5,"may",172,1,-1,0,"unknown","no"),
(39,"management","single","tertiary","no",255,"yes","no","unknown",5,"may",296,1,-1,0,"unknown","no")


select * from bank_details

select age, job from bank_details

select `default`, age from bank_details

select * from bank_details;

select * from bank_details where age = 41

select job from bank_details where age = 41

select *from bank_details where job = 'retired' and balance > 100

select *from bank_details

select * from bank_details where education = 'primary' or balance < 100
select * from bank_details where education = 'primary' and balance < 100

select distinct job from bank_details;

select * from bank_details order by age
select * from bank_details order by age desc;
select count(*) from bank_details

select sum(balance) from bank_details
select avg(balance) from bank_details
select min(balance) from bank_details
select max(balance) from bank_details

select * from bank_details where balance = (select min(balance) from bank_details)

select marital, count(*) from bank_details group by marital
select marital, count(*), sum(balance), avg(balance) from bank_details group by marital
select marital, count(*), sum(balance), avg(balance) from bank_details group by marital having sum(balance) > 300;

select marital, count(*), sum(balance), avg(balance) from bank_details group by marital having avg(balance) < 300;

select * from bank_details

select * from bank_details where education = 'unknown'

set sql_safe_updates = 0;
update bank_details set balance = 0 where job = 'unknown'

select * from bank_details where job = 'unknown'
select * from bank_details
update bank_details set contact = 'known', y = 'yes' where `month` = 'may'
select * from bank_details where month = 'may'

update bank_details set `default` = 'null' where `default` = 'no';
select * from bank_details where `default` = 'null'
select * from bank_details order by `default`

delete from bank_details where job = 'unknown'
select * from bank_details
ALTER TABLE bank_details DROP COLUMN previous;

DELIMITER &&
create procedure select_pro()
BEGIN
	select * from bank_details;
END &&


alter table bank_details drop column poutcome

call select_pro
call select_pro

delimiter &&
create procedure select_pre_filter()
begin
	select * from bank_details where job = 'retired' and balance >100;
end &&


delimiter &&
create procedure select_pre_filter_input(IN var int)
begin
	select * from bank_details where job = 'retired' and balance > var;
end &&

call select_pre_filter_input(50)

DELIMITER &&
create procedure select_pre_filter2(IN var int , IN var2 varchar(30) )
BEGIN
	select * from bank_details where job = var2 and balance > var;
END &&

call select_pre_filter2(100, 'retired')

call select_pre_filter2(100, 'services')



select * from (select job, age, education, y from bank_details) as a where a.age = 58;
select job, age, education, y from bank_details where age = 58

create view bank_view as select job, age, education, y from bank_details

select * from bank_view where age = 58
select * from bank_view

create table if not exists bank_details1 (age int, job varchar(30), marital varchar(30), education varchar(30), `default` varchar(30),	balance int, housing varchar(30), loan varchar(30),	contact varchar(30), `day` int,	`month` varchar(30),	duration int,	campaign int,	pdays int,	previous int, poutcome varchar(30),	y varchar(30)) ;


create table if not exists bank_details2 (age int, job varchar(30), marital varchar(30), education varchar(30), `default` varchar(30),	balance int, housing varchar(30), loan varchar(30),	contact varchar(30), `day` int,	`month` varchar(30),	duration int,	campaign int,	pdays int,	previous int, poutcome varchar(30),	y varchar(30)) ;

show tables

insert into bank_details1 values (44,"technician","single","secondary","no",29,"yes","no","unknown",5,"may",151,1,-1,0,"unknown","no"),
(33,"entrepreneur","married","secondary","no",2,"yes","yes","unknown",5,"may",76,1,-1,0,"unknown","no"),
(47,"blue-collar","married","unknown","no",1506,"yes","no","unknown",5,"may",92,1,-1,0,"unknown","no"),
(33,"unknown","single","unknown","no",1,"no","no","unknown",5,"may",198,1,-1,0,"unknown","no"),
(35,"management","married","tertiary","no",231,"yes","no","unknown",5,"may",139,1,-1,0,"unknown","no"),
(28,"management","single","tertiary","no",447,"yes","yes","unknown",5,"may",217,1,-1,0,"unknown","no"),
(42,"entrepreneur","divorced","tertiary","yes",2,"yes","no","unknown",5,"may",380,1,-1,0,"unknown","no"),
(58,"retired","married","primary","no",121,"yes","no","unknown",5,"may",50,1,-1,0,"unknown","no"),
(43,"technician","single","secondary","no",593,"yes","no","unknown",5,"may",55,1,-1,0,"unknown","no"),
(41,"admin.","divorced","secondary","no",270,"yes","no","unknown",5,"may",222,1,-1,0,"unknown","no"),
(29,"admin.","single","secondary","no",390,"yes","no","unknown",5,"may",137,1,-1,0,"unknown","no"),
(53,"technician","married","secondary","no",6,"yes","no","unknown",5,"may",517,1,-1,0,"unknown","no"),
(58,"technician","married","unknown","no",71,"yes","no","unknown",5,"may",71,1,-1,0,"unknown","no"),
(57,"services","married","secondary","no",162,"yes","no","unknown",5,"may",174,1,-1,0,"unknown","no"),
(51,"retired","married","primary","no",229,"yes","no","unknown",5,"may",353,1,-1,0,"unknown","no"),
(45,"admin.","single","unknown","no",13,"yes","no","unknown",5,"may",98,1,-1,0,"unknown","no"),
(57,"blue-collar","married","primary","no",52,"yes","no","unknown",5,"may",38,1,-1,0,"unknown","no"),
(60,"retired","married","primary","no",60,"yes","no","unknown",5,"may",219,1,-1,0,"unknown","no"),
(33,"services","married","secondary","no",0,"yes","no","unknown",5,"may",54,1,-1,0,"unknown","no"),
(28,"blue-collar","married","secondary","no",723,"yes","yes","unknown",5,"may",262,1,-1,0,"unknown","no"),
(56,"management","married","tertiary","no",779,"yes","no","unknown",5,"may",164,1,-1,0,"unknown","no"),
(32,"blue-collar","single","primary","no",23,"yes","yes","unknown",5,"may",160,1,-1,0,"unknown","no"),
(25,"services","married","secondary","no",50,"yes","no","unknown",5,"may",342,1,-1,0,"unknown","no"),
(40,"retired","married","primary","no",0,"yes","yes","unknown",5,"may",181,1,-1,0,"unknown","no"),
(44,"admin.","married","secondary","no",-372,"yes","no","unknown",5,"may",172,1,-1,0,"unknown","no"),
(39,"management","single","tertiary","no",255,"yes","no","unknown",5,"may",296,1,-1,0,"unknown","no")

insert into bank_details2 select * from bank_details1

select * from bank_details2

-- to join two tables --
/* inner join operations, left join and right join operations */

select bank_details1.age, bank_details1.job, bank_details1.marital from bank_details1 inner join bank_details2 on bank_details1.age = bank_details2.age

/* workout more on data join process */

-- creating bank_details3 and working out on join operation --
create table if not exists bank_details3 (age int, job varchar(30), marital varchar(30), education varchar(30), `default` varchar(30),	balance int, housing varchar(30), loan varchar(30),	contact varchar(30), `day` int,	`month` varchar(30),	duration int,	campaign int,	pdays int,	previous int, poutcome varchar(30),	y varchar(30)) ;

insert into bank_details3 select *from bank_details2 where age = 58;

select * from bank_details3

-- inner join operations on bank_details2 and bank_details3
select bank_details2.age, bank_details2.job, bank_details2.marital from bank_details2 inner join bank_details3 on bank_details2.age = bank_details3.age

-- RIGHT JOIN OPERATION
select bank_details2.age, bank_details2.job, bank_details2.marital from bank_details2 right join bank_details3 on bank_details2.age = bank_details3.age

insert into bank_details3 select * from bank_details1 where age = 58;


show databases

show databases; show tables
drop database if exists kumaresan

show databases;


