import time
import csv


def searchData():
    with open('unitedRent.csv', 'r', encoding='UTF8') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
 #    with open('unitedRent.csv', 'a', encoding='UTF8') as file:
        count = 0
        for row in csvreader:
            print(row)
            count+=1
            if count >=5:
                break


if __name__ == '__main__':
    searchData()
