----------------------------------------------------------------------------- CODING CHALLENGE - MSSQL -----------------------------------------------------------------------------

------------------------------------------------------------------------------ PETPALS ------------------------------------------------------------------------------------------------------

--QUESTION 1. Provide a SQL script that initializes the database for the Pet Adoption Platform ”PetPals”.

create database PetPals;
use PetPals;

--QUESTION 2. Create tables for pets, shelters, donations, adoption events, and participants.

--QUESTION 3. Define appropriate primary keys, foreign keys, and constraints.

--QUESTION 4. Ensure the script handles potential errors, such as if the database or tables already exist

create table Pets(petid int primary key, name varchar(50),age int, breed varchar(50),type varchar(20),available_for_adoption bit);

insert into Pets(petid,name,age,breed,type,available_for_adoption) values 
(101,'Mani',2,'Labrador','dog',1),
(102,'snow',3,'Persian','cat',1),
(103,'Mueza',4,'indian','cat',0),
(104,'subbu',5,'german shepherd','dog',1),
(105,'harry',2,'rabbit','rabbit',1),
(106,'coco',3,'pug','dog',0),
(107,'lara',1,'siamese','cat',0);

select * from Pets;

create table Shelters(shelterid int primary key, name varchar(50), location varchar(55));

insert into Shelters(shelterid, name,location) values (201,'happy tails','Nungambakkam'),
(202,'furry friends','kodambakkam'),
(203,'care4paws','madipakkam'),
(204,'cute creatures','velacherry'),
(205,'tiny friends','choolaimedu'),
(206,'whisk-world','aavadi'),
(207,'pets-mart','aalandur');

select * from Shelters;

create table Donations(donationid int primary key, donor_name varchar(35),donation_type varchar(20),donation_amount decimal(10,2), donation_item varchar(20),donation_date datetime);

insert into Donations(donationid,donor_name,donation_type,donation_amount,donation_item,donation_date) values 
(301,'sulaiha','cash',1000.00,null,'2025-04-01'),
(302,'safana','item',null,'food','2025-04-02'),
(303,'syed','item',null,'blankets','2025-04-05'),
(304,'Sumaiya','cash',2000.00,null,'2025-04-09'),
(305,'hayfa','cash',1500.00,null,'2025-04-07'),
(306,'yusuf','itme',null,'toys','2025-04-10'),
(307,'absar','cash',2500.00,null,'2025-04-15');

select * from Donations;

create table AdoptionEvents(eventid int primary key, event_name varchar(50),event_date datetime, location varchar(50));

insert into AdoptionEvents (eventid, event_name, event_date, location) values
(401, 'Adopchild', '2025-04-15', 'Chennai Trade Center'),
(402, 'Paws meet human', '2025-04-18', 'lignite Hall'),
(403, 'Furry Fiesta', '2025-04-20', 'Convention Center'),
(404, 'Tails Expo', '2025-04-23', 'Mailam Pet Arena'),
(405, 'Pet Fest', '2025-04-25', ' City Hall'),
(406, 'pet world', '2025-04-27', 'egmore hall'),
(407, 'New Beginnings', '2025-04-30', 'EA Mall');

select * from AdoptionEvents;

create table Participants(participantid int primary key,participant_name varchar(35),participant_type varchar(50), eventid  int foreign key references AdoptionEvents(eventid));

insert into Participants(participantid,participant_name,participant_type, eventid) values
(501,'reeshma','Shelter',404),
(502,'shahana','Adopter',403),
(503,'femina','Shelter',401),
(504,'mariyam','Adopter',405),
(505,'famitha','Shelter',405),
(506,'aanisha','Adopter',402),
(507,'sameera','Shelter',406);

select * from Participants;

--QUESTION 5. Write an SQL query that retrieves a list of available pets (those marked as available for adoption) from the "Pets" table. 

select * from Pets where available_for_adoption=1;

--QUESTION 6. Write an SQL query that retrieves the names of participants (shelters and adopters) registered for a specific adoption event. 

declare @eventid int = 404;
select p.participant_name, p.participant_type, a.event_name from participants p join AdoptionEvents a on p.eventid = a.eventid where p.eventid=@eventid;

--QUESTION 7. Create a stored procedure in SQL that allows a shelter to update its information (name and location) in the "Shelters" table.

create procedure updatehelter @new_shelterid int, @shelter_name varchar(50), @shelter_location varchar(50) as
begin
if exists(select * from Shelters where shelterid = @new_shelterid)
begin
update Shelters set name=@shelter_name, location=@shelter_location where shelterid= @new_shelterid;
	print 'Shelter information updated successfully.';
end
else
begin
	print 'Error: Shelter ID not found.';
	end
end;
exec  updatehelter @new_shelterid= 202, @shelter_name = 'Furry Home', @shelter_location = 'T. Nagar';
select * from Shelters;

--QUESTION 8. Write an SQL query that calculates and retrieves the total donation amount for each shelter (by shelter name) from the "Donations" table. 

alter table Donations add shelterid INT FOREIGN KEY REFERENCES Shelters(shelterid);

update Donations set shelterid = 201 WHERE donationid = 301;
update Donations set shelterid = 202 WHERE donationid = 302;
update Donations set shelterid = 202 WHERE donationid = 303;
update Donations set shelterid = 203 WHERE donationid = 304;
update Donations set shelterid = 204 WHERE donationid = 305;
update Donations set shelterid = 205 WHERE donationid = 306;
update Donations set shelterid = 206 WHERE donationid = 307;

select s.name as shelter_name, isnull(sum(d.donation_amount), 0) as total_donations from Shelters s left join Donations d on s.shelterid = d.shelterid group by s.name;
  
--QUESTION 9. Write an SQL query that retrieves the names of pets from the "Pets" table that do not have an owner (i.e., where "OwnerID" is null).
alter table Pets add owner_id int null;

select name,age,breed,type from Pets where owner_id  is null;

--QUESTION 10. Write an SQL query that retrieves the total donation amount for each month and year (e.g.,January 2023) from the "Donations" table. 

select format(donation_date, 'MMMM YYYY') as [Month- Year], sum(donation_amount) as Totaldonation from Donations where donation_type= 'cash'
group by format(donation_date, 'MMMM YYYY') order by min(donation_date);

--QUESTION 11. . Retrieve a list of distinct breeds for all pets that are either aged between 1 and 3 years or older than 5 years.

select distinct breed from Pets where (age between 1 and 3) or (age > 5);

--QUESTION 12. Retrieve a list of pets and their respective shelters where the pets are currently available for adoption

alter table Pets add shelterid int foreign key  references Shelters(shelterid);

update Pets set shelterid = 201 WHERE petid = 101;
update Pets set shelterid = 202 WHERE petid = 102;
update Pets set shelterid = 203 WHERE petid = 103;
update Pets set shelterid = 204 WHERE petid = 104;
update Pets set shelterid = 205 WHERE petid = 105;
update Pets set shelterid = 206 WHERE petid = 106;
update Pets set shelterid = 207 WHERE petid = 107;
select * from Pets;

select p.name as pet_name, s.name as shelter_name from Pets p join Shelters s on p.shelterid = s.shelterid where p.available_for_adoption = 1;

--QUESTION 13. 3. Find the total number of participants in events organized by shelters located in specific city

select count(p.participantid) as total_participants from Participants p join AdoptionEvents ae on p.eventid = ae.eventid
join Shelters s on p.participant_type = 'shelter' and p.participant_name = s.name where s.location = 'Nungambakkam';

--QUESTION 14. Retrieve a list of unique breeds for pets with ages between 1 and 5 years.

select distinct breed from Pets where age between 1 and 5;

--QUESTION 15. Find the pets that have not been adopted by selecting their information from the 'Pet' table.
create table users ( userid int primary key,name varchar(50),contact varchar(50));

insert into users (userid, name, contact) values(1, 'suhail', 'suhail@gmail.com'),(2, 'shakeel', 'shakeel@gmail.com'),(3, 'ibrahim', 'ibrahim@gmail.com');

create table adoption (adoptionid int primary key,petid int foreign key references pets(petid),userid int foreign key references users(userid),adoption_date date);

insert into adoption (adoptionid, petid, userid, adoption_date) values(1, 103, 1, '2025-04-10'),(2, 106, 2, '2025-04-13');

select * from pets where petid not in (select petid from adoption);

--QUESTION 16. Retrieve the names of all adopted pets along with the adopter's name from the 'Adoption' and 'User' tables

select p.name as pet_name, u.name as adopter_name from adoption a join pets p on a.petid = p.petid join users u on a.userid = u.userid;

--QUESTION 17. Retrieve a list of all shelters along with the count of pets currently available for adoption in each shelter.

select shelters.name as shelter_name,  count(pets.petid) as available_pets from  shelters left join  pets on shelters.shelterid = pets.shelterid and pets.available_for_adoption = 1
group by  shelters.name;

--QUESTION 18. Find pairs of pets from the same shelter that have the same breed

select  p1.name as pet1_name, p2.name as pet2_name, p1.breed, p1.shelterid
from  pets p1 join  pets p2 on p1.shelterid = p2.shelterid   and p1.breed = p2.breed  and p1.petid < p2.petid;

--QUESTION 19.  List all possible combinations of shelters and adoption events

select   shelters.name as shelter_name, adoptionevents.event_name from shelters cross join adoptionevents;

--QUESTION 20. Determine the shelter that has the highest number of adopted pets.

select top 1 s.name as shelter_name,count(a.petid) as adopted_pet_count from  Shelters s join pets p on s.shelterid = p.shelterid
join adoption a on p.petid = a.petid group by  s.name order by adopted_pet_count desc;

