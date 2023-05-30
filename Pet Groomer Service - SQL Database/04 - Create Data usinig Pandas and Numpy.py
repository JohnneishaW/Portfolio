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


def create_store(storeNameList, addressList):
    store_street = []
    store_city = []
    store_state = []
    store_zip = []
    phone = []
    for item in storeNameList:
        currentAdd = addressList.iloc[random.randrange(0, (addressList.shape[0])-1), :]
        store_street.append(currentAdd['Street'])
        store_city.append(currentAdd['City'])
        store_state.append(currentAdd['State'])
        store_zip.append(currentAdd['Zipcode'])
    data = {
            'Name': storeNameList,
            'Street': store_street,
            'City': store_city,
            'State': store_state,
            'Zip': store_zip
        }
    df = pd.DataFrame(data)
    print(df)
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

    store = create_store(storeName, address)

