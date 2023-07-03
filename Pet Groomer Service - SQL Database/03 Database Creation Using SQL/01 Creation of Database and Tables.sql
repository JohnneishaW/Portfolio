CREATE DATABASE PetGroomer;

USE PetGroomer;

CREATE TABLE Pet(
ID int IDENTITY(1,1) PRIMARY KEY
,PetOwnerID int
,Name varchar(100)
,Breed varchar(100)
,Age int
,Birthday date
,Weight int
,VacinationID int
,Status varchar(20)
);

CREATE TABLE PetOwner(
ID int IDENTITY(1,1) PRIMARY KEY
,FirstName varchar(30)
,LastName varchar(30)
,Street varchar(50)
,City varchar(30)
,State varchar(30)
,Zipcode int
,Phone int
,Email varchar(100)
,AcctCreationDate date
,LastLoggedIn date
,Status varchar(20)
);

CREATE TABLE Vacation(
ID int IDENTITY(1,1) PRIMARY KEY
,Name varchar(255)
,Expiration date
);

CREATE TABLE Employee(
ID int IDENTITY(1,1) PRIMARY KEY
,StoreID int
,FirstName varchar(30)
,LastName varchar(30)
,Street varchar(50)
,City varchar(30)
,State varchar(30)
,Zipcode int
,Phone int
,Email varchar(100)
,HireDate date
,WorkScheduleID int
);

CREATE TABLE WorkSchedule(
ID int IDENTITY(1,1) PRIMARY KEY
,ShiftID int
,EmployeeID int
);

CREATE TABLE Shift(
ID int IDENTITY(1,1) PRIMARY KEY
,Job varchar(50)
,ShiftDate date
,ShiftStartTime time
,ShiftEndTime time
);

CREATE TABLE Service(
ID int IDENTITY(1,1) PRIMARY KEY
,StoreID int
,Name varchar(30)
,Cost decimal
,Duration decimal
);

CREATE TABLE Store(
ID int IDENTITY(1,1) PRIMARY KEY
,Name varchar(30)
,Street varchar(50)
,City varchar(30)
,State varchar(30)
,Zipcode int
,Phone int
,OpenDate date
);

CREATE TABLE Appointment(
ID int IDENTITY(1,1) PRIMARY KEY
,ServiceID int
,StoreID int
,PetID int
,PetOwnerID int
,EmployeeID int
,WorkScheduleID int
,StartTime time
,Date date
);