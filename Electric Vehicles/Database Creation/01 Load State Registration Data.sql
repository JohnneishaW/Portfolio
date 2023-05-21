CREATE TABLE #TempStateRegistrations(
   State VARCHAR(100),
   RegistrationCount INT
);

BULK INSERT #TempStateRegistrations
FROM 'C:\Users\Johnneisha\OneDrive\Documents\GitHub\Portfolio\Electric Vehicles\Data Sources\ev-registration-counts-by-state_cleaned.csv'
WITH (
   FIELDTERMINATOR = ',',
   ROWTERMINATOR = '\n',
   FIRSTROW = 2
);

USE ElectricVehicles; --ElectricVehicles is the database.

CREATE TABLE StateRegistrations(
	StateID int PRIMARY KEY IDENTITY(1,1), --identity used for auto increment ID
	State varchar(255) NOT NULL,
	RegistrationCount int
);

INSERT INTO StateRegistrations (State, RegistrationCount)
SELECT State, RegistrationCount
FROM #TempTable;
