import time
import csv
import numpy as np
def test():
    file = ['5','10',[*np.arange(1.0, 3.0, .1)]]
    for i in file:
        if type(i) == list:
            for j in i:
                print(f'this is inner list data {round(j,1)}')
        print(i)


def searchData():
    with open('unitedRent.csv', 'r', encoding='UTF8') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        fileAttribute = []
        FilterData0 = ['2WD','4WD','Push','Towable','Diesel','Electric','Gas','Gas or Diesel','2WD',[*range(8,24)],[*range(10,15)],[*range(15,21)],[*range(24,30)],[*range(26,36)],[*range(26,60)],[*range(30,36)],[*range(36,49)],[*range(36,71)],[*range(60,96)],[*range(96,186)],[*range(30,46)],[*range(46,69)],'IC','Internal Combustion']
        FilterData1 = [[*range(1000,1801)],[*range(3,16)],[*range(100,350)],[*range(350,1000)],'Towable','Tier 4','Diesel','Gas']
        FilterData2 = ['Double','Single','Pad','Smooth',[*range(18,50)],[*range(50,71)],[*range(71,90)],'Diesel','Gas',[*range(3000,6000)],[*range(6000,10001)]]
        FilterData3 = [[*range(500,2501)],[*range(2501,5001)],[*range(4,13)],[*range(13,19)],[*range(19,25)],[*range(25,49)],[*range(49,85)],[*np.arange(1.0, 3.0, .1)],[*np.arange(3.0, 5.1, .1)],[*range(400,750)],'4WD','Tire','Track',[*range(5,16)],[*range(16,18)],[*range(18,51)],[*range(51,91)],[*range(81,96)],[*range(91,131)],[*range(19000,40000)],[*range(40000,80000)],[*range(1000,5000)],[*range(10000,15000)],[*range(15000,20000)],[*range(5000,10000)],'Diesel',[*range(600,1700)],[*range(1700,2001)],[*range(2001,2800)],2800,'Reduced Tail Swing','Zero Swing','Low Ground Pressure','standard']
        FilterData4 = []
        FilterData5 = []
        FilterData6 = []
        FilterData7 = []
        FilterData8 = []
        FilterData9 = []
        FilterData10 = []
        FilterData11 = []
        FilterData12 = []
        FilterData13 = []
        
        for row in csvreader:
            for i in row:
                if '75' in i:
                    print(row)



if __name__ == '__main__':
    test()
