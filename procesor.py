import csv

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f"- name: {row[1]}")
        print(f"  degree: {row[4]}")
        print(f"  email: {row[2]}")
