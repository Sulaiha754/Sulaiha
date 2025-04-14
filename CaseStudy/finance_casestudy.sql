create database financemanagerdb;
use financemanagerdb;

create table users ( user_id int primary key identity(1,1),  username varchar(50) not null,  password varchar(255) not null,email varchar(100) not null unique);

 insert into users(username,password,email)values('user1','User@12345','sulaihabari10@gmail.com');

 insert into users(username, password, email) values('user2','user123','user@gmail.com');


 create table expense_categories (category_id int primary key identity(1,1),category_name varchar(50) not null);

create table expenses ( expense_id int primary key identity(1,1), user_id int foreign key references users(user_id), 
category_id int foreign key references expense_categories(category_id),amount decimal(10, 2) not null,date date not null,description varchar(255));

create table income_categories (category_id int primary key identity(1,1),category_name varchar(50) not null);

create table income (income_id int primary key identity(1,1),  user_id int foreign key references users(user_id),
category_id int foreign key references income_categories(category_id),  amount decimal(10, 2) not null, date date not null,description varchar(255));


insert into expense_categories (category_name) values ('Tax'),('Food'), ('Transportation'), ('Utilities'), ('Rent'), ('Entertainment'),
('Stationery'),('Clothing'),('medicine'),('hospital'),('wifi-subscription'),('recharge'),('gas');

insert into expenses (user_id,category_id, amount, date, description)
values (1, 2, 100.00, '2025-04-14', 'Dinner');

insert into income_categories (category_name) values ('Investments');
('Salary'), ('Freelance'), ('Business'), ('Gift'), ('Other');

select * from expense_categories;
select * from income_categories;
select * from income;
select * from expenses;
select * from users;