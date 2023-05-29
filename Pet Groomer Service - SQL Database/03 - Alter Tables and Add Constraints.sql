Use PetGroomer;
--------RENAME TABLE AND COLUMNS TO CORRECT VACCINATION TYPO--------
EXEC sp_rename 'dbo.Vacation', 'Vaccination'; --MySQL code: ALTER TABLE Vacation RENAME TO Vaccination;
EXEC sp_rename 'dbo.Pet.VacinationID', 'VaccinationID', 'COLUMN'; --MySQL code: ALTER TABLE Pet RENAME COLUMN VacinationID to VaccinationID;*/

--------ALTER COLUMNS--------
/*Note - If the table contained data, a new column would need to be created.  Data from the old column would be inserted into the new one. Then, the old column would be deleted.*/

--Changing "many" entity in pet and vaccination many-to-one relationship.
ALTER TABLE Pet
DROP COLUMN VaccinationID;

ALTER TABLE Vaccination
ADD PetID int;

--Adding type of pet
ALTER TABLE Pet
ADD Type varchar(20);

--Converting from many-to-many relationship to many-to-one.
ALTER TABLE Employee
DROP COLUMN WorkScheduleID;

--------ADD CONSTRAINTS--------
ALTER TABLE Vaccination
ADD CONSTRAINT FK_Vaccination_Pet FOREIGN KEY (PetID) REFERENCES Pet(ID);

ALTER TABLE Employee
ADD CONSTRAINT FK_Employee_Store FOREIGN KEY (StoreID) REFERENCES Store(ID);

ALTER TABLE Pet
ADD CONSTRAINT FK_Pet_PetOwner FOREIGN KEY (PetOwnerID) REFERENCES PetOwner(ID);

ALTER TABLE WorkSchedule
ADD CONSTRAINT FK_WorkSchedule_Employee FOREIGN KEY (EmployeeID) REFERENCES Employee(ID)
,CONSTRAINT FK_WorkSchedule_Shift FOREIGN KEY (ShiftID) REFERENCES Shift(ID);

ALTER TABLE Appointment
ADD CONSTRAINT FK_Appointment_Service FOREIGN KEY (ServiceID) REFERENCES Service(ID)
,CONSTRAINT FK_Appointment_Store FOREIGN KEY (StoreID) REFERENCES Store(ID)
,CONSTRAINT FK_Appointment_Pet FOREIGN KEY (PetID) REFERENCES Pet(ID)
,CONSTRAINT FK_Appointment_PetOwner FOREIGN KEY (PetOwnerID) REFERENCES PetOwner(ID)
,CONSTRAINT FK_Appointment_Employee FOREIGN KEY (EmployeeID) REFERENCES Employee(ID)
,CONSTRAINT FK_Appointment_WorkSchedule FOREIGN KEY (WorkScheduleID) REFERENCES WorkSchedule(ID);