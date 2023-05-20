CREATE DATABASE ElectricVehicles; 

USE ElectricVehicles;
CREATE TABLE StateRegistrations(
	StateID int PRIMARY KEY IDENTITY(1,1), --identity used for auto increment ID
	State varchar(255) NOT NULL,
	RegistrationCount int
);

CREATE TABLE VehicleRegistration(
VehicleRegID int PRIMARY KEY IDENTITY(1,1),
CAFVehicleType varchar(255),
VIN varchar(50),
DOLVehicleID varchar(50),
ModelYear char(4),
Make varchar(255),
Model varchar(255),
PrimaryUse varchar(100),
ElectricRange int,
OdometerReading int,
OdometerCode text,
VehCondition varchar(100),
SalePrice int,
SaleDate date,
BaseMSRP int,
TransactionType varchar(255),
DOLTransactionDate datetime,
TransactionYear int,
County varchar(100),
City varchar(100),
State varchar(100),
PostalCode int,
HB2778ExemptionEligibility2015 BIT, --bit is a bool (true/false)
HB2042CAFVEligibility2019 BIT,
HB2042ElectricRangeRequirementMet2019 BIT,
HB2042SaleDateRequirementMet2019 BIT,
HB2042SalePriceValueRequirementMet2019 BIT,
HB2042BatteryRangeRequirement2019 text,
HB2042PurchaseDateRequirement2019 text,
HB2042SalePriceValueRequirement2019 text,
ElectricVehicleFeePaid BIT,
TransportationElectrificationFeePaid BIT,
HybridVehicleElectrificationFeePaid BIT,
CensusTract2020 int,
LegislativeDistrict int,
ElectricUtility text
);