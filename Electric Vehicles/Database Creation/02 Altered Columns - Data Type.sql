-- Note: In order to alter columns, the columns must be empty. 
-- If the column has data,  a new column of desired data type will need to be created and then data will need to be transfered into new column. 

ALTER TABLE ElectricVehicles.dbo.StateRegistrations
ALTER COLUMN [RegistrationCount] INT NOT NULL;