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
        date = str(random.randrange(1, 12)) + '/' + str(random.randrange(1, 28)) + '/' + str(
            random.randrange(2019, 2022))
        openDate.append(date)

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
    #print(df.head())
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
        'AccCreationDate': AccCreationDate,
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

    data = {
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

    store = create_store(storeName, parse_address(address, storeName))
    service = create_service(serviceNames)
    shift = create_shift(jobFile)
    petOwner = create_pet_owner(firstNames, lastNames, parse_address(address, firstNames), status)
    employee = create_employee(firstNames, lastNames, parse_address(address, firstNames))

