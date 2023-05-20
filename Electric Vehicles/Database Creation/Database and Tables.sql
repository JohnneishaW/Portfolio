CREATE DATABASE ElectricVehicles;

CREATE TABLE StateRegistrations(
StateID int auto_increment PRIMARY KEY,
State varchar(255) NOT NULL,
RegistrationCount int
);

CREATE TABLE VehicleRegistration(
VehicleRegID int auto_increment PRIMARY KEY,
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
SaleDate datetime,
BaseMSRP int,
TransactionType varchar(255),
DOLTransactionDate datetime,
TransactionYear year,
County varchar(100),
City varchar(100),
State varchar(100),
PostalCode int(5),
2015HB2778ExemptionEligibility bool,
2019HB2042CAFVEligibility bool,
2019HB2042ElectricRangeRequirement bool,
2019HB2042SaleDateRequirement bool,
2019HB2042SalePriceValueRequirement bool,
2019HB2042BatteryRangeRequirement text,
2019HB2042PurchaseDateRequirement text,
2019HB2042SalePriceValueRequirement text,
ElectricVehicleFeePaid bool,
TransportationElectrificationFeePaid bool,
HybridVehicleElectrificationFeePaid bool,
2020CensusTract int(100),
LegislativeDistrict int(50),
ElectricUtility text
);