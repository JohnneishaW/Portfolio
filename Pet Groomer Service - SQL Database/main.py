import random
import pandas as pd
import numpy as np


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
        date = str(random.randrange(1, 12)) + '-' + str(random.randrange(1, 28)) + '-' + str(
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
    print(df.head())
    return df


def create_service(serviceNames):
    allServices = {}
    storeServices = [] #tuple of service name, cost, and duration (minutes)
    StoreID = []
    Name = []
    Cost = []
    Duration = []
    for item in store.index:
        storeId = item
        for serviceItem in serviceNames:
            storeServices.append((serviceItem, random.randrange(1, 30), random.randrange(15, 45)))

        allServices[storeId] = storeServices
        storeServices = []

    print(list(allServices.values())[0][1][0])

    data = {
        'StoreID': allServices.keys(),
        'Name': allServices.values(),
        'Cost': allServices.keys(),
        'Duration': allServices.keys()
    }
    df = pd.DataFrame(data)
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
