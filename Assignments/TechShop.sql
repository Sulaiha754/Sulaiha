----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------TASK 1 DATABASE DESIGN --------------------------------------------------------------------------------------------
--1. Create the database named "TechShop"

--2. Define the schema for the Customers, Products, Orders, OrderDetails and Inventory tables based on the provided schema.

--3. Create an ERD (Entity Relationship Diagram) for the database.

--4. Create appropriate Primary Key and Foreign Key constraints for referential integrity.

--5. Insert at least 10 sample records into each of the following tables.  a. Customers b. Products c. Orders d. OrderDetails e. Inventory

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
create database TechShop;
use TechShop;

create table Customers ( CustomerID int primary key, Firstname varchar(50), Lastname varchar(50), Email varchar(100) unique, Phone varchar(20), Address varchar(255));

create table Products (    ProductID int primary key,    ProductName varchar(100),   Description text,   Price decimal(10,2));

create table Orders ( OrderID int primary key, CustomerID int, OrderDate date, TotalAmount decimal(10,2),   foreign key (CustomerID) references Customers(CustomerID));

create table OrderDetails (  OrderDetailID int primary key, OrderID int, ProductID int, Quantity int,   foreign key (OrderID) references Orders(OrderID),
foreign key (ProductID) references Products(ProductID));

create table Inventory ( InventoryID int primary key, ProductID int, QuantityInStock int, LastStockUpdate date, foreign key (ProductID) references Products(ProductID));

insert into Customers(CustomerID, Firstname, Lastname, Email, Phone, Address) values (101,'Anu','Ashish','anu@gmail.com','9876543210','Chennai'),
(102,'Barathi','Bala','barathi@gmail.com','9987654321','Cuddalore'),(103,'Charu','Lekha','charu@gmail.com','9887654321','Madurai'),
(104,'Devi','Priya','devi@gmail.com','9877654321','Kerala'),(105,'Ezhil','Amudhan','ezhil@gmail.com','9876654321','Pondy'),
(106,'Fahad','Azim','fahad@gmail.com','9876554321','Villupuram'),(107,'Gayathri','Ravi','gayu@gmail.com','9876544321','Maharashtra'),
(108,'Hayfa','Parveen','hayfa@gmail.com','9876543321','Bangalore'),(109,'Ibrahim','Taj','immu@gmail.com','9876543221','Mumbai'),
(110,'Jacob','james','jacob@gmail.com','9876543211','Coimbatore');

select * from Customers;

insert into Products(productid, productname, description, price) values(201, 'Smartphone', 'Android smartphone with 6GB RAM', 15000.00),
(202, 'Laptop', '15-inch laptop with Intel i5', 55000.00),(203, 'Headphones', 'Wireless over-ear headphones', 2500.00),
(204, 'Smartwatch', 'Fitness tracking watch', 4000.00),(205, 'Tablet', '10-inch tablet with 64GB storage', 18000.00),
(206, 'Bluetooth Speaker', 'Portable Bluetooth speaker', 3000.00),(207, 'Keyboard', 'Wireless keyboard', 1500.00),
(208, 'Mouse', 'Ergonomic wireless mouse', 1200.00),(209, 'Monitor', '24-inch Full HD monitor', 10000.00),
(210, 'Power Bank', '10000mAh power bank', 1200.00);

select * from Products;

insert into Orders(orderid, customerid, orderdate, totalamount) values(301, 101, '2024-03-01', 15500.00),(302, 102, '2024-03-02', 56000.00),
(303, 103, '2024-03-03', 2500.00),(304, 104, '2024-03-04', 8000.00),(305, 105, '2024-03-05', 18000.00),(306, 106, '2024-03-06', 4200.00),(307, 107, '2024-03-07', 2700.00),
(308, 108, '2024-03-08', 13000.00),(309, 109, '2024-03-09', 11200.00),(310, 110, '2024-03-10', 2500.00);

select * from Orders;

insert into OrderDetails(OrderDetailID, OrderID, ProductID, Quantity) values(401, 301, 201, 1),(402, 302, 202, 1),(403, 303, 203, 1),(404, 304, 204, 2),
(405, 305, 205, 1),(406, 306, 206, 1),(407, 307, 207, 2),(408, 308, 208, 2),(409, 309, 209, 1),(410, 310, 210, 2);

select * from OrderDetails;

insert into Inventory(InventoryID, ProductID, QuantityInStock, LastStockUpdate) values(501, 201, 50, '2024-02-20'),(502, 202, 30, '2024-02-21'),
(503, 203, 100, '2024-02-22'),(504, 204, 40, '2024-02-23'),(505, 205, 25, '2024-02-24'),(506, 206, 60, '2024-02-25'),
(507, 207, 80, '2024-02-26'),(508, 208, 75, '2024-02-27'),(509, 209, 20, '2024-02-28'),(510, 210, 90, '2024-02-29');

select * from Inventory;

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------TASK 2 DDL,DML,DQL--------------------------------------------------------------------------------------------------------------

--QUESTION 1. Write an SQL query to retrieve the names and emails of all customers

select Firstname, Lastname,Email from Customers;

--QUESTION 2. Write an SQL query to list all orders with their order dates and corresponding customer names.

select o.OrderID, o.OrderDate, c.Firstname, c.Lastname from Orders o join Customers c on o.CustomerID = c.CustomerID;

--QUESTION 3. Write an SQL query to insert a new customer record into the "Customers" table.

insert into Customers (CustomerID, Firstname, Lastname, Email, Phone, Address) values (111, 'kavitha', 'raj', 'kavitha@gmail.com', '9876543212', 'Lucknow');
select * from Customers;

--QUESTION 4. Write an SQL query to update the prices of all electronic gadgets in the "Products" table by increasing them by 10%

update Products set Price = Price * 1.10;
select * from Products;

--QUESTION 5. Write an SQL query to delete a specific order and its associated order details from the "Orders" and "OrderDetails" tables

delete from OrderDetails where OrderID = 310;
select * from OrderDetails;
delete from Orders where OrderID = 301;
select * from Orders;

--QUESTION 6. Write an SQL query to insert a new order into the "Orders" table

insert into Orders (OrderID, CustomerID, OrderDate, TotalAmount)values (311, 102, '2024-04-08', 2000.00);
select * from Orders;

--QUESTION 7. Write an SQL query to update the contact information (e.g., email and address) of a specific customer in the "Customers" table

update Customers set Email = 'gayravi@yahoo.com', Address = 'Germany' where CustomerID = 107;
select * from Customers;

--QUESTION 8. Write an SQL query to recalculate and update the total cost of each order in the "Orders" table based on the prices and quantities in the "OrderDetails" table.

update Orders set TotalAmount = (  select sum(p.Price * od.Quantity)  from OrderDetails od  join Products p on od.ProductID = p.ProductID  where od.OrderID = Orders.OrderID);
select * from Orders;
select* from OrderDetails;

--QUESTION 9. Write an SQL query to delete all orders and their associated order details for a specific customer from the "Orders" and "OrderDetails" tables. 

delete from orderdetails where orderid in (select orderid from orders where customerid = 109);
delete from orders where customerid = 109;
select * from Orders;
select* from OrderDetails;

--question 10. Write an SQL query to insert a new electronic gadget product into the "Products" table, including product name, category, price, and any other relevant details.

insert into Products (ProductID, Productname, Description, Price)values (211, 'router', 'dual band wifi router', 3500.00);
select * from Products;

--QUESTION 11. Write an SQL query to update the status of a specific order in the "Orders" table (e.g., from "Pending" to "Shipped").

alter table Orders add status varchar(50);
update orders set status = 'pending' where orderid = 301;
update orders set status = 'shipped' where orderid = 302;
update orders set status = 'pending' where orderid = 303;
update orders set status = 'shipped' where orderid = 304;
update orders set status = 'assigned' where orderid = 305;
update orders set status = 'assigned' where orderid = 306;
update orders set status = 'shipped' where orderid = 307;
update orders set status = 'shipped' where orderid = 308;
update orders set status = 'shipped' where orderid = 311;
      update Orders set status ='shipped' where OrderID=301;
select * from Orders;

--QUESTION 12. Write an SQL query to calculate and update the number of orders placed by each customer in the "Customers" table based on the data in the "Orders" table.

update Customers set OrderCount = o.TotalOrders from Customers c join (select CustomerID, count(*) as TotalOrders 
from Orders group by CustomerID) as o on c.CustomerID = o.CustomerID;
select * from Customers;

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------TASK 3 AGGREGGATE FUNCTIONS , GROUP BY, ORDER BY, JOINS-----------------------------------------------------------------------------------

--QUESTION 1 Write an SQL query to retrieve a list of all orders along with customer information (e.g.,customer name) for each order.

select  o.OrderID,  o.OrderDate,c.FirstName + ' ' + c.LastName as CustomerName from Orders o join  Customers c on o.CustomerID = c.CustomerID;

--QUESTION 2 Write an SQL query to find the total revenue generated by each electronic gadget product.


select p.ProductName, sum (od.Quantity * p.Price) as TotalRevenue from OrderDetails od join Products p on od.ProductID = p.ProductID group by p.ProductName;

--QUESTION 3Write an SQL query to list all customers who have made at least one purchase. 
select distinct c.FirstName+' ' + c.LastName as CustomerName, c.Email, c.Phone from  Customers c join  Orders o on c.CustomerID = o.CustomerID;

--QUESTION 4 Write an SQL query to find the most popular electronic gadget, which is the one with the highest total quantity ordered. 


select top 1  p.ProductName,sum (od.Quantity) as TotalQuantityOrdered from OrderDetails od join Products p on od.ProductID = p.ProductID
group by  p.ProductName order by TotalQuantityOrdered desc;

--QUESTION 5 Write an SQL query to retrieve a list of electronic gadgets along with their corresponding categories.

alter table Products add Category varchar(50);
update Products set Category= 'mobile' where ProductID=201;
update Products set Category= 'laptop' where ProductID=202;
update Products set Category= 'headphone' where ProductID=203;
update Products set Category= 'watch' where ProductID=204;
update Products set Category= 'tablet' where ProductID=205;
update Products set Category= 'speaker' where ProductID=206;
update Products set Category= 'keyboards' where ProductID=207;
update Products set Category= 'mouse' where ProductID=208;
update Products set Category= 'mouse' where ProductID=209;

select ProductName, Category from Products;

--QUESTION 6. Write an SQL query to calculate the average order value for each customer. Include the customer's name and their average order value.

select c.FirstName + ' ' + c.LastName as CustomerName, avg(o.TotalAmount) as AverageOrderValue from  Customers c join  Orders o on c.CustomerID = o.CustomerID
group by c.FirstName, c.LastName;

--QUESTION 7. Write an SQL query to find the order with the highest total revenue. Include the order ID, customer information, and the total revenue.

select top 1  o.OrderID, c.FirstName + ' ' + c.LastName as CustomerName, o.TotalAmount from Orders o join Customers c on o.CustomerID = c.CustomerID order by o.TotalAmount desc;

--QUESTION 8.  Write an SQL query to list electronic gadgets and the number of times each product has been ordered.


select p.ProductName, count(od.OrderDetailID) as TimesOrdered from  OrderDetails od join  Products p ON od.ProductID = p.ProductID group by p.ProductName;

--QUESTION 9. Write an SQL query to find customers who have purchased a specific electronic gadget product.

select distinct c.FirstName+' ' + c.LastName as CustomerName, c.Email, c.Phone from Customers c join Orders o on c.CustomerID = o.CustomerID 
join OrderDetails od on o.OrderID = od.OrderID join Products p on od.ProductID = p.ProductID where p.ProductName = 'Mouse';

--QUESTION 10. Write an SQL query to calculate the total revenue generated by all orders placed within a specific time period.

select sum(TotalAmount) as TotalRevenue from  Orders where OrderDate between '2024-03-01' and '2024-03-05';

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------TASK 4 SUBQUERY----------------------------------------------------------------------------------------------------

--1. Write an SQL query to find out which customers have not placed any orders

SELECT FirstName, LastName FROM Customers WHERE CustomerID NOT IN (  SELECT DISTINCT CustomerID FROM Orders);

--2. Write an SQL query to find the total number of products available for sale. 

SELECT COUNT(*) AS TotalProducts FROM Products;

--3. Write an SQL query to calculate the total revenue generated by TechShop.

SELECT SUM(TotalAmount) AS TotalRevenue FROM Orders;

--4. Write an SQL query to calculate the average quantity ordered for products in a specific category. 

SELECT AVG(Quantity) AS AverageQuantity FROM OrderDetails WHERE ProductID IN (   SELECT ProductID FROM Products WHERE Category = 'Mouse');

--5. Write an SQL query to calculate the total revenue generated by a specific customer.
SELECT SUM(TotalAmount) AS CustomerRevenue FROM Orders WHERE CustomerID = 105;  

--6. Write an SQL query to find the customers who have placed the most orders. List their names
--and the number of orders they've placed.

SELECT FirstName, LastName, OrderCount FROM (  SELECT c.FirstName, c.LastName, COUNT(o.OrderID) AS OrderCount FROM Customers c
 JOIN Orders o ON c.CustomerID = o.CustomerID GROUP BY c.FirstName, c.LastName) AS OrderCounts WHERE OrderCount = (
SELECT MAX(OrderCount) FROM (  SELECT COUNT(OrderID) AS OrderCount FROM Orders GROUP BY CustomerID ) AS SubCounts);

--7. Write an SQL query to find the most popular product category, which is the one with the highest total quantity ordered across all orders

SELECT Category, SUM(od.Quantity) AS TotalOrdered FROM Products p JOIN OrderDetails od ON p.ProductID = od.ProductID GROUP BY Category
HAVING SUM(od.Quantity) = (SELECT MAX(CategoryTotal) FROM (SELECT SUM(od.Quantity) AS CategoryTotal FROM Products p JOIN OrderDetails od ON p.ProductID = od.ProductID
 GROUP BY p.Category) AS Totals);

 --8. Write an SQL query to find the customer who has spent the most money (highest total revenue)on electronic gadgets. List their name and total spending.

SELECT FirstName, LastName, TotalSpent FROM (SELECT c.FirstName, c.LastName, SUM(o.TotalAmount) AS TotalSpent FROM Customers c
 JOIN Orders o ON c.CustomerID = o.CustomerID GROUP BY c.FirstName, c.LastName)
AS Spending WHERE TotalSpent = (SELECT MAX(TotalSpent) FROM (SELECT SUM(TotalAmount) AS TotalSpent FROM Orders GROUP BY CustomerID ) AS SubTotals);

--9. Write an SQL query to calculate the average order value (total revenue divided by the number of orders) for all customers.

SELECT AVG(TotalAmount) AS AverageOrderValue FROM Orders;

--10. Write an SQL query to find the total number of orders placed by each customer and list their names along with the order count.

SELECT c.FirstName, c.LastName, COUNT(o.OrderID) AS OrderCount FROM Customers c LEFT JOIN Orders o ON c.CustomerID = o.CustomerID GROUP BY c.FirstName, c.LastName;

--------------------------------------------------------------------*************************************----------------------------------------------------------------------------------
