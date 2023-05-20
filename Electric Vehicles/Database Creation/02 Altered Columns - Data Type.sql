USE ElectricVehicles;
-- Note: In order to alter columns, the columns must be empty. 
-- If the column has data,  a new column of desired data type will need to be created and then data will need to be transfered into new column. 

ALTER TABLE electricvehicles.vehicleregistration
MODIFY COLUMN PostalCode int, 
MODIFY COLUMN 2020CensusTract int, 
MODIFY COLUMN LegislativeDistrict int;