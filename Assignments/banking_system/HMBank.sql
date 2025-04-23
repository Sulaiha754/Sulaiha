
--------------------------------------------------------------------------ASSIGNMENT 3----------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------TASK 1 ------------------------------------------------------------------------------------------
use HMBank;

------I HAVE ALREADY CREATED DATABASE AND TABLES and INSERTED 5 RECORDS PREVIOUSLY FOR THE FOLLLOWING-----------

select name from sys.tables;

select * from Customers;
exec sp_help Transactions;
select * from Accounts;

select * from Transactions;

insert into Customers(customer_id,first_name,last_name,DOB,email,phone_number,address) values(6,'Fahad','Azim','2000-01-10','fahad@gmail.com','9876554321','Villupuram'),
(7,'Gayathri','Ravi','2000-02-11','gayu@gmail.com','9876544321','Maharashtra'),(8,'Hayfa','Parveen','2000-03-13','hayfa@gmail.com','9876543321','Salem'),
(9,'Ibrahim','Taj','2000-04-15','immu@gmail.com','9876543221','Pune'),(10,'Jacob','james','2000-05-25','jacob@gmail.com','9876543211','Nagercoil');

insert into Customers (customer_id,first_name,last_name,DOB,email,phone_number, address) values(11,'syed','musthafa','2010-12-24','syed@gmail.com','9998765432','madagadipet');
insert into Customers (customer_id,first_name,last_name,DOB,email,phone_number, address) values(12,'abdul','rahman','2001-11-21','rahman@gmail.com','9999765432','mailam');

insert into Accounts(account_id,customer_id,account_type,balance) values(106,6,'zero',600.00);
insert into Accounts(account_id,customer_id,account_type,balance) values(107,7,'current',2200.00);
insert into Accounts(account_id,customer_id,account_type,balance) values(108,8,'savings',1400.00);
insert into Accounts(account_id,customer_id,account_type,balance) values(109,9,'zero',1100.00);
insert into Accounts(account_id,customer_id,account_type,balance) values(110,10,'savings',1600.00);
insert into Accounts(account_id,customer_id,account_type,balance) values(111,11,'savings',16600.00);
insert into Accounts(account_id,customer_id,account_type,balance) values(112,11,'current',1600.00);
insert into Accounts(account_id,customer_id,account_type,balance) values(113,12,'zero',1300.00);

insert into Transactions(transaction_id,account_id,transaction_type,amount,transaction_date) values(1006,106,'withdrawal',200.00,'2024-04-10'),
(1007,107,'deposit',1200.00,'2024-04-11'),(1008,108,'withdrawal',100.00,'2024-04-01'),
(1009,109,'deposit',300.00,'2024-04-05'),(1010,110,'withdrawal',100.00,'2024-04-04');
insert into Transactions(transaction_id,account_id,transaction_type,amount,transaction_date) values(1011,111,'deposit',200.00,'2024-04-03');
insert into Transactions(transaction_id,account_id,transaction_type,amount,transaction_date) values(1012,111,'withdrawal',100.00,'2024-04-03');

------------------------------------------------------------------------------TASK 2 ---------------------------------------------------------------------------------------------

--QUESTION1. Write a SQL query to retrieve the name, account type and email of all customers. 

select c.first_name ,c.last_name ,c.email,a.account_type from Accounts a join Customers c on c.customer_id=  a.customer_id;

--QUESTION 2. Write a SQL query to list all transaction corresponding customers.

select  c.customer_id,  c.first_name ,c.last_name , t.transaction_id, t.transaction_type, t.amount, t.transaction_date from customers c join 
 accounts a on c.customer_id = a.customer_id join  transactions t on a.account_id = t.account_id;

 --QUESTION 3. Write a SQL query to increase the balance of a specific account by a certain amount.

update accounts set balance =balance+5000 where customer_id=3;
select * from Accounts;

 --QUESTION 4. Write a SQL query to Combine first and last names of customers as a full_name

select first_name + '' + last_name as full_name from Customers;

 --QUESTION 5. Write a SQL query to remove accounts with a balance of zero where the account type is savings.

delete from Accounts where balance = 0 and account_type = 'savings';

 --QUESTION 6. Write a SQL query to Find customers living in a specific city

select * from Customers where address like '%Pune%';

 --QUESTION 7.  Write a SQL query to Get the account balance for a specific account.

select balance from Accounts where account_id=105;

 --QUESTION 8. Write a SQL query to List all current accounts with a balance greater than $1,000.

select * from Accounts where account_type='current' and balance >1000;

 --QUESTION 9. Write a SQL query to Retrieve all transactions for a specific account

select * from transactions where account_id = 110;

 --QUESTION 10.  Write a SQL query to Calculate the interest accrued on savings accounts based on a given interest rate.

select  account_id,  balance,  balance * 0.020 as interest_accrued from  accounts where  account_type = 'savings'; --2.0 interesr calculated

 --QUESTION 11. Write a SQL query to Identify accounts where the balance is less than a specified overdraft limit.

select * from accounts where balance < -500;

 --QUESTION 12. Write a SQL query to Find customers not living in a specific city

select * from Customers where address  not like '%Pune%';

  ----------------------------------------------------------------------TASK 3-----------------------------------------------------------------------------------------------------------

  --QUESTION 1. Write a SQL query to Find the average account balance for all customers. 

select avg(balance) as average_balance from Accounts;

  --QUESTION 2. Write a SQL query to Retrieve the top 10 highest account balances.

select top 10   account_id, balance from  accounts order by balance desc;

  --QUESTION 3. Write a SQL query to Calculate Total Deposits for All Customers in specific date.

select sum(amount) as total_deposit from  transactions where  transaction_type = 'deposit' and transaction_date = '2024-12-01';

  --QUESTION 4. Write a SQL query to Find the Oldest and Newest Customers.

select *  from customers order by dob asc; -- oldest at top, newest at bottom

  --QUESTION 5. Write a SQL query to Retrieve transaction details along with the account type.

select t.transaction_id,t.transaction_type,t.amount,t.transaction_date,a.account_type from  transactions t join accounts a on t.account_id = a.account_id;

  --QUESTION 6. Write a SQL query to Get a list of customers along with their account details.

select c.customer_id, c.first_name, c.last_name, a.account_id, a.account_type, a.balance from customers c join  accounts a on c.customer_id = a.customer_id;

  --QUESTION 7. Write a SQL query to Retrieve transaction details along with customer information for a specific account.

select   c.first_name,   c.last_name,   t.transaction_id,   t.transaction_type,  t.amount,  t.transaction_date from customers c join 
 accounts a on c.customer_id = a.customer_id join  transactions t on a.account_id = t.account_id where  a.account_id = 101;

 --QUESTION 8. Write a SQL query to Identify customers who have more than one account.

select customer_id, count(account_id) as account_count from accounts group by customer_id having  count(account_id) > 1;

 --QUESTION 9. Write a SQL query to Calculate the difference in transaction amounts between deposits and withdrawals.

select account_id, sum(case when transaction_type = 'deposit' then amount else 0 end) - sum(case when transaction_type = 'withdrawal' then amount else 0 end) as difrnc
from  transactions group by account_id;

--QUESTION 10. Write a SQL query to Calculate the average daily balance for each account over a specified period.

SELECT account_id,AVG(balance) AS avgdailybalance FROM Accounts WHERE account_id IN 
(SELECT account_id FROM Transactions  WHERE transaction_date BETWEEN '2024-04-01' AND '2024-04-10')GROUP BY account_id;

--QUESTION 11.Calculate the total balance for each account type
  
select  account_type,sum(balance) as total_balance from accounts group by account_type;

--QUESTION 12. Identify accounts with the highest number of transactions order by descending order

select account_id, count(transaction_id) as transaction_count from transactions group by account_id order by transaction_count desc;

--QUESTION 13. List customers with high aggregate account balances, along with their account types

select   c.customer_id,   c.first_name,   c.last_name,  a.account_type, sum(a.balance) as total_balance from customers c join 
accounts a on c.customer_id = a.customer_id group by  c.customer_id, c.first_name, c.last_name, a.account_type having sum(a.balance) > 10000;

--QUESTION 14.. Identify and list duplicate transactions based on transaction amount, date, and account.

select account_id,amount,transaction_date, count(*) as duplicate_count from transactions group by account_id, amount, transaction_date having count(*) > 1;

--------------------------------------------------------------------TASK 4 -------------------------------------------------------------------------------------------------

--QUESTION 1. Retrieve the customer(s) with the highest account balance

select * from Customers where customer_id in (select customer_id from Accounts where balance = (select max(balance) from Accounts));

--QUESTION 2. Calculate the average account balance for customers who have more than one account

select customer_id,avg(balance) as avg_balance from accounts where customer_id in (select customer_id from accounts group by customer_id having count(account_id) > 1 )
group by customer_id;

--QUESTION 3. Retrieve accounts with transactions whose amounts exceed the average transaction amount.

select * from transactions where amount > (select avg(amount) from transactions);

--QUESTION 4. Identify customers who have no recorded transactions.

select * from customers where customer_id not in (select distinct a.customer_id  from accounts a join transactions t on a.account_id = t.account_id);

--QUESTION 5. Calculate the total balance of accounts with no recorded transactions.

select  sum(balance) as total_balance_without_txn from accounts where account_id not in (select distinct account_id from transactions);

--QUESTION 6. Retrieve transactions for accounts with the lowest balance.

select * from transactions where account_id in ( select account_id from accounts  where balance = (select min(balance) from accounts));

--QUESTION 7. Identify customers who have accounts of multiple types.

select customer_id from accounts group by customer_id having count(distinct account_type) > 1;

--QUESTION 8. . Calculate the percentage of each account type out of the total number of accounts.

select account_type, count(*) * 100.0 / (select count(*) from accounts) as percentage from accounts group by account_type;

--QUESTION 9. Retrieve all transactions for a customer with a given customer_id.

select * from transactions where account_id in (select account_id from accounts where customer_id = 101);

--QUESTION 10. Calculate the total balance for each account type, including a subquery within the SELECT clause.

select  account_type, (select sum(balance) from Accounts a2 where a2.account_type = a1.account_type) as total_balance from accounts a1 group by  account_type;

  
