from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc
import csv
from selenium import webdriver

def setupDriver(url="https://www.unitedrentals.com/marketplace/equipment/compaction"):
    global count
    global flag
    try:
        driver.get(url)
        return driver
    except:
        print('setup driver function failed, Restarting mainUrls function...')
        if count > flag:
            flag = count
        count = 0
        mainUrls()


def mainUrls():
    global count
    try:
        mainUrlList = ['https://www.unitedrentals.com/marketplace/equipment/compaction','https://www.unitedrentals.com/marketplace/equipment/earthmoving-equipment']
        gettingElements(mainUrlList)
    except:
        print('mainUrls function failed, Restarting the function...')
        count = 0
        mainUrls()


def gettingElements(lists):

    global count
    global total
    global flag
    try:
        for i in lists:
            if count >= flag:
                try:
                    driver2 = setupDriver(i)
                except:
                    print("Calling main Url Function...")
                    if count > flag:
                        flag = count
                    count = 0
                    mainUrls()
                time.sleep(5)
                try:
                    driver.find_element(
                        by=By.XPATH, value='//*[@id="locationSearch"]').send_keys('Ontario, CA')
                    time.sleep(3)
                    driver.find_element(
                        by=By.XPATH, value='/html/body/div/div/div[3]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[1]/div/ul/li[1]').click()
                    time.sleep(3)
                    button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/button')))
                    button.click()
                except:
                    print("could not find filter form!")
                time.sleep(6)

                count+=1
                print(f'Restarting count point: {count}')

                time.sleep(1)
                filterData = ''
                title = ''
                try:
                    title = driver2.find_element(by=By.XPATH,value='/html/body/div/div/div[1]/section/div/nav/ol/li[2]').text
                except:
                    print('title not found!')
                try:
                    filterObject = driver2.find_elements(
                        by=By.XPATH, value='/html/body/div/div/main/section/div/div/aside/div[3]/div[2]/div[2]/div/fieldset')
                except:
                    print('filter object not found!!!')
                filterData = {}
                try:
                    for h in filterObject:
                        header = h.find_elements(by=By.XPATH,value='legend')
                        data = h.find_elements(by=By.CLASS_NAME,value='labelClass')
                        for head in header:
                            for val in data:
                                filterData.setdefault(head.text,[]).append(val.text)
                    print(filterData)
                except:
                    print('nothing found!')
                newDataList = [i,title]
                print(newDataList)
                try:
                    result = {}
                    result['URL'] = i
                    result['Category Title'] = title
                    result['Data'] = filterData
                    categoryWriter.writerow(result)
                    print('cooper csv wrote!')
                    total += 1
                    print(f'Total csv wrote: {total}')
                except Exception as e:
                    print("error in main in level argument", e.args[0])
                    print('cooper CSV not working!')
        print('Done!')
    except:
        print("function error! Calling main function")
        count = 0
        mainUrls()

if __name__ == '__main__':
    count = 0
    flag = 0
    total = 0
    with open('csv/threeCategory.csv', 'a', encoding='UTF8') as file:
        categoryHeader = ['URL', 'Category Title', 'Data']
        categoryWriter = csv.DictWriter(file, fieldnames=categoryHeader)
        categoryWriter.writeheader()
        time.sleep(2)
        driver = uc.Chrome()
        mainUrls()