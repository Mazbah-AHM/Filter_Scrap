import time
import csv

def Something():
    pass


if __name__ == '__main__':
    with open('rent_product.csv', 'r', encoding='UTF8') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
    with open('unitedRent.csv', 'a', encoding='UTF8') as file, open('price.csv', 'a', encoding='UTF8') as priceFile:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        time.sleep(2)
        priceHeader = ['URL', 'ID', 'Category', 'Sub Category', 'Daily', 'Weekly', 'Monthly', 'Item Cost', 'Deliver to Jobsite',
                       'Retrieval From Jobsite', 'Environmental Fee', 'Tax', 'Estimated Cost']
        priceWriter = csv.DictWriter(priceFile, fieldnames=priceHeader)
        priceWriter.writeheader()
