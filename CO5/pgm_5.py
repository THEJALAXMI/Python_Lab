import csv
csv_col=['Roll No','Name','Place']
dict_data=[{'Roll No':1,'Name':'Thejalakshmi','Place':'Thrissur'},
           {'Roll No':2,'Name':'Thasni','Place':'Thrissur'},
           {'Roll No':3,'Name': 'Anjela','Place':'Idukki'},
           {'Roll No':4,'Name':'Nandana','Place':'Palakkad'},
           {'Roll No':5,'Name':'Arya','Place':'Nemmara'}]
csv_file="student.csv"
try:
  with open(csv_file,'w')as file1:
     writer=csv.DictWriter(file1,fieldnames=csv_col)
     writer.writeheader()
     for data1 in dict_data:
        writer.writerow(data1)
except IOError:
     print("I/O error")
data1 = csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data1:
    print(row)
