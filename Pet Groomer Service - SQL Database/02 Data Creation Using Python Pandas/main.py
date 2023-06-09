import random
import pandas as pd
import numpy as np
from datetime import time, date


def load_file_into_numpy_array(filepath, delimiter):
    array = np.array([])
    with open(filepath, 'r') as file:
        for line in file:
            split_line = line.split(delimiter)
            stripped_line = [element.strip() for element in split_line]
            array = np.append(array, stripped_line)
    return array


def load_file_into_pandas_dataframe(filename, delimiter):
    df = pd.read_csv(filename, sep=delimiter)
    return df


def parse_address(addressList, for_table):
    street = []
    city = []
    state = []
    zipcode = []
    for item in for_table:
        currentAdd = addressList.iloc[random.randrange(0, (addressList.shape[0]) - 1), :]
        street.append(currentAdd['Street'])
        city.append(currentAdd['City'])
        state.append(currentAdd['State'])
        zipcode.append(currentAdd['Zipcode'])
    return street, city, state, zipcode


def create_store(storeNameList, parsedAddress):
    phone = []
    openDate = []
    creatingPhone = []
    for item in storeNameList:
        openDate.append(date.fromisoformat(str(random.randrange(2000, 2022)) + '-' + str(random.randrange(10, 12))+ '-' + str(random.randrange(10, 28))))
        # create phone number
        for x in range(10):
            creatingPhone.append(random.randrange(0, 9))
        phone.append(''.join(map(str, creatingPhone)))
        creatingPhone = []

    data = {
        'Name': storeNameList,
        'Street': parsedAddress[0],
        'City': parsedAddress[1],
        'State': parsedAddress[2],
        'Zipcode': parsedAddress[3],
        'Phone': phone,
        'OpenDate': openDate
    }
    df = pd.DataFrame(data)
    #print(df.head())
    return df


def create_service(serviceNames):
    allServices = {}
    #storeServices = [] #tuple of service name, cost, and duration (minutes)
    StoreID = []
    Name = []
    Cost = []
    Duration = []
    for item in store.index:
        #storeId = item
        for serviceItem in serviceNames:
            #storeServices.append((serviceItem, random.randrange(1, 30), random.randrange(15, 45)))
            StoreID.append(item)
            Name.append(serviceItem)
            Cost.append(random.randrange(1, 30))
            Duration.append(random.randrange(15, 45))
        #allServices[storeId] = storeServices
        #storeServices = []

    #print(list(allServices.values())[0][1][0])

    data = {
        'StoreID': StoreID,
        'Name': Name,
        'Cost': Cost,
        'Duration': Duration
    }
    df = pd.DataFrame(data)
    #print(df.head())
    return df


def create_shift(jobs):
    Job = []
    ShiftDate = []
    ShiftStartTime = []
    ShiftEndTime = []

    counter = 0
#IMPROVEMENT - ADD CONDITIONAL TO ADDRESS SINGLE DIGIT PART OF DATES AND TIME (I.E. IF 8 --> RETURN 08)
    while counter<2:
        for j in jobs:
            Job.append(j)
            #print(j)
            shiftdate = date.fromisoformat(str(
            random.randrange(2019, 2024)) + '-' + str(random.randrange(10, 12))+ '-' + str(random.randrange(10, 28)))
            ShiftDate.append(shiftdate)
            
            start = time.fromisoformat(str(random.randrange(10, 24)) + ':' + str(random.randrange(10, 59)) + ':' + str(
            random.randrange(10, 59))+ '.' + str(random.randrange(100, 999)))
            end = time.fromisoformat('00:00:00.000')

            while(end<start):
                end = time.fromisoformat(str(random.randrange(10, 24)) + ':' + str(random.randrange(10, 59)) + ':' + str(
            random.randrange(10, 59))+ '.' + str(random.randrange(100, 999)))
            
            ShiftStartTime.append(start)
            ShiftEndTime.append(end)
        counter+=1

    data = {
        'Job': Job,
        'ShiftDate': ShiftDate,
        'ShiftStartTime': ShiftStartTime,
        'ShiftEndTime': ShiftEndTime
    }
    df = pd.DataFrame(data)
    # print(df.head())
    return df


def create_pet_owner(firstNamesList, lastNamesList, parsedAddress, statusList):
    FirstName = []
    LastName = []
    Phone = []
    CreatingPhone = []
    Email = []
    AccCreationDate = []
    LastLoggedIn = []
    Status = []

    for firstName in firstNamesList:
        FirstName.append(firstName)
        LastName.append(lastNamesList[random.randrange(0, len(lastNamesList)-1)])

        # create phone number
        for x in range(10):
            CreatingPhone.append(random.randrange(0, 9))
        Phone.append(''.join(map(str, CreatingPhone)))
        CreatingPhone = []

        Status.append(statusList[random.randrange(0, len(statusList)-1)])

        accCreationDate = date.fromisoformat(str(
            random.randrange(2019, 2023)) + '-' + str(random.randrange(10, 12)) + '-' + str(random.randrange(10, 28)))
        AccCreationDate.append(accCreationDate)

        lastLoggedIn = date.fromisoformat(str(
            random.randrange(2019, 2023)) + '-' + str(random.randrange(10, 12)) + '-' + str(random.randrange(10, 28)))

        if lastLoggedIn > accCreationDate:
            LastLoggedIn.append(lastLoggedIn)
        else:
            lastLoggedIn = date.fromisoformat(str(
                random.randrange(2019, 2023)) + '-' + str(random.randrange(10, 12)) + '-' + str(random.randrange(10, 28)))
            LastLoggedIn.append(lastLoggedIn)

        Email.append(firstName + str(random.randrange(0, 100)) + "@gmail.com")

    data = {
        'FirstName': FirstName,
        'LastName': LastName,
        'Street': parsedAddress[0],
        'City': parsedAddress[1],
        'State': parsedAddress[2],
        'Zipcode': parsedAddress[3],
        'Phone': Phone,
        'Email': Email,
        'AcctCreationDate': AccCreationDate,
        'LastLoggedIn': LastLoggedIn,
        'Status': Status
    }
    df = pd.DataFrame(data)
    #print(df.head())
    return df


def create_employee(firstNamesList, lastNamesList, parsedAddress):
    FirstName = []
    LastName = []
    Phone = []
    CreatingPhone = []
    Email = []
    HireDate = []
    StoreID = []

    for lastName in lastNamesList:
        LastName.append(lastName)
        FirstName.append(firstNamesList[random.randrange(0, len(lastNamesList)-1)])

        # create phone number
        for x in range(10):
            CreatingPhone.append(random.randrange(0, 9))
        Phone.append(''.join(map(str, CreatingPhone)))
        CreatingPhone = []

        hireDate = date.fromisoformat(str(
            random.randrange(2019, 2023)) + '-' + str(random.randrange(10, 12)) + '-' + str(random.randrange(10, 28)))
        HireDate.append(hireDate)

        Email.append(lastName + str(random.randrange(0, 100)) + "@gmail.com")

        StoreID.append(store.iloc[random.randrange(0, (store.shape[0]) - 1), :])

    data = {
        'StoreID': StoreID,
        'FirstName': FirstName,
        'LastName': LastName,
        'Street': parsedAddress[0],
        'City': parsedAddress[1],
        'State': parsedAddress[2],
        'Zipcode': parsedAddress[3],
        'Phone': Phone,
        'Email': Email,
        'HireDate': HireDate,
    }
    df = pd.DataFrame(data)
    # print(df.head())
    return df


def create_pet(petNames, petBreeds,petStatus):
    owner = []
    name = []
    breeds = []
    petType = []
    age = []
    birthday = []
    weight = []
    status = []


    for n in petNames:
        name.append(n)
        selectedBreedandType = petBreeds.iloc[random.randrange(0, (petBreeds.shape[0]) - 1), :]
        breeds.append(selectedBreedandType['Breed'])
        petType.append(selectedBreedandType['Type'])
        age.append(random.randrange(2,9))
        birthday.append(date.fromisoformat(str(random.randrange(2019, 2024)) + '-' + str(random.randrange(10, 12))+ '-' + str(random.randrange(10, 28))))
        weight.append(random.randrange(5,30))
        status.append(petStatus[random.randrange(0, len(petStatus)-1)])
        owner.append(petOwner.iloc[random.randrange(0, (petOwner.shape[0]) - 1), :])
                        

    data = {
        'PetOwnerID': owner,
        'Name': name,
        'Breed': breeds,
        'Age': age,
        'Birthday': birthday,
        'Weight': weight,
        'Status': status,
        'Type': petType
    }
    df = pd.DataFrame(data)
    #print(df.head())
    return df


def create_vaccination(vacList):
    name = []
    expirDate = []
    PetID = []

    for p in pet.index:
        PetID.append(p)
        name.append(vacList[random.randrange(0, len(vacList)-1)])
        expirDate.append(date.fromisoformat(str(random.randrange(2000, 2022)) + '-' + str(random.randrange(10, 12))+ '-' + str(random.randrange(10, 28))))
    
    data = {
        'Name': name,
        'Expiration': expirDate,
        'PetID': PetID
    }

    df = pd.DataFrame(data)
    # print(df.head())
    return df


def create_work_schedule():
    ShiftID = []
    EmployeeID = []

    for x in range(100):
        ShiftID.append(shift.iloc[random.randrange(0, (shift.shape[0]) - 1), :])
        EmployeeID.append(employee.iloc[random.randrange(0, (employee.shape[0]) - 1), :])

    data = {
        'ShiftID': ShiftID,
        'EmployeeID': EmployeeID
    }
    df = pd.DataFrame(data)
    #print(df.head())
    return df


def create_appointment():
    serviceid = []
    storeid = []
    petid = []
    petownerid = []
    employeeid = []
    workscheduleid = []
    starttime = []
    dates = []
    for x in range(100):
        serviceid.append(service.iloc[random.randrange(0, (service.shape[0]) - 1), :])
        storeid.append(store.iloc[random.randrange(0, (store.shape[0]) - 1), :])
        petid.append(pet.iloc[random.randrange(0, (pet.shape[0]) - 1), :])
        petownerid.append(petOwner.iloc[random.randrange(0, (petOwner.shape[0]) - 1), :])
        employeeid.append(employee.iloc[random.randrange(0, (employee.shape[0]) - 1), :])
        workscheduleid.append(workSchedule.iloc[random.randrange(0, (workSchedule.shape[0]) - 1), :])
        starttime.append(time.fromisoformat(str(random.randrange(10, 24)) + ':' + str(random.randrange(10, 59)) + ':' + str(random.randrange(10, 59))+ '.' + str(random.randrange(100, 999))))
        dates.append(date.fromisoformat(str(random.randrange(2019, 2024)) + '-' + str(random.randrange(10, 12))+ '-' + str(random.randrange(10, 28))))
    
    data = {
        'ServiceID': serviceid,
        'StoreID': storeid,
        'PetID': petid,
        'PetOwnerID': petownerid,
        'EmployeeID': employeeid,
        'WorkScheduleID': workscheduleid,
        'StartTime':starttime,
        'Date': dates,
    }

    df = pd.DataFrame(data)
    #print(df.head())
    return df


if __name__ == '__main__':
    # Load File Data Into Data Structure
    firstNames = load_file_into_numpy_array('First Names.txt', " \n")
    lastNames = load_file_into_numpy_array('Last Names.txt', " \n")
    address = load_file_into_pandas_dataframe("Addresses.txt", ",")
    storeName = load_file_into_numpy_array('Store Names.txt', " \n")
    petName = load_file_into_numpy_array('Pet Names.txt', " \n")
    jobFile = load_file_into_numpy_array('Jobs.txt', " \n")
    serviceNames = load_file_into_numpy_array('Service Names.txt', " \n")
    status = load_file_into_numpy_array('Status.txt', " \n")
    breeds = load_file_into_pandas_dataframe("Breeds.txt", ",")
    vaccinations = load_file_into_numpy_array('Vaccinations.txt', ",")

    store = create_store(storeName, parse_address(address, storeName))
    service = create_service(serviceNames)
    shift = create_shift(jobFile)
    petOwner = create_pet_owner(firstNames, lastNames, parse_address(address, firstNames), status)
    employee = create_employee(firstNames, lastNames, parse_address(address, firstNames))
    pet = create_pet(petName, breeds, status)
    vaccination = create_vaccination(vaccinations)
    workSchedule = create_work_schedule()
    appointment = create_appointment()

    