import csv
import os


def openCsvFile(path = "pp-complete_short.csv", encoding='utf-8'):
      with open(path, encoding = encoding) as f:
        rows = csv.reader(f, delimiter=",")
        return list(rows)

def findSimilarStringsbyStreet(arr: list, path = 'all_duble.csv'):
    # rm = []
    match = 0
    with open(path, "a", newline='', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',') 
        for count, str in enumerate(arr):
            # search_str = str.split(',')
            s = ','.join(str[9:14])
            search_str = str
            match = 0
            
            for i in range((count + 1), len(arr)-1):
                if arr[i][0].find(s) != -1:
                    # rm.append(arr[i][0])
                    print(arr[i])
                    datawriter.writerow(arr[i])
                    if match == 0:
                        # rm.append(search_str)
                        datawriter.writerow([search_str]) 
                    match +=1
                    
            # rm = []

def findSimilarStringsbyNumber(arr: list):
    rm = []
    match = 0
    with open('Itog.csv', "w", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        for count, str in enumerate(arr):
            search_str = str[0].split(',')
            s = ','.join(search_str[7])
            print(s)
            search_str = str[0]
            match = 0
            for i in range((count + 1), len(arr)-1):
                if arr[i][0].find(s) != -1:
                    rm.append(arr[i][0])
                    datawriter.writerow(arr[i])
                    if match == 0:
                        rm.append(search_str)
                        datawriter.writerow([str])
                    match +=1

def findSimilarStringsbyEnd(arr: list):
    
    match = 0

    with open('Itog_4.csv', "w", newline='', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        for count, str in enumerate(arr):
            search_str = str[0].split(',')
            s = ','.join(search_str[7:14])
            search_str = str[0]
            match = 0
            for i in range((count + 1), len(arr)-1):
                if arr[i][0].find(s) != -1:
                    for_write = str[0].split(',')
                    address = for_write[7].replace('"', '', 4)
                    address2 = '' if len(for_write[8].replace('"', '', 4)) == 0 else for_write[8].replace('"', '', 4)
                    street = for_write[9].replace('"', '', 4)
                    city = for_write[10].replace('"', '', 4)
                    region = for_write[13].replace('"', '', 4)
                    district = for_write[11].replace('"', '', 4)
                    s = f"{address},{address2}, {street}, {city}, {district}, {region}"
                    datawriter.writerow([s])
        

if __name__ == '__main__':
    count = 0
    s = ''

    path = os.getcwd()
    
     
    for filename in os.listdir(path):
        if 'chunk' in filename:
            print(f'{path}\\{filename}')
            arr = openCsvFile(path = f'{path}\\{filename}')
            findSimilarStringsbyStreet(arr, path = f'{path}\\new{count}.csv')     
            count += 1
            if count == 2:
                break       



    # arr = openCsvFile()
    # findSimilarStringsbyStreet(arr)

    # arr = openCsvFile(path = "out5.csv")    
    # findSimilarStringsbyEnd(arr)    

    # print('END')
    