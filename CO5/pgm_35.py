import csv
with open('student.csv',newline='')as csvfile1:
    data=csv.DictReader(csvfile1)
    print("Name")
    print("----")
    for i in data:
        print(i['Name'])
