import sklearn
from sklearn.preprocessing import *
import numpy as np
from numpy import *


def normalization(data):
    data_mm = (data-data.min(axis=0)) / (data.max(axis=0)-data.min(axis=0))
    return data_mm

def numpy_standardization(data):
    std_data = (data-np.mean(data, axis=0)/(np.std(data, axis=0)))
    return std_data

def main():
    data = np.random.randint(30, size=(6,5))
    #print(data)
    std_data_temp = numpy_standardization(data)
    print(std_data_temp)

    no_data = normalization(data)
    print(no_data)


if __name__ == '__main__':
    main()
