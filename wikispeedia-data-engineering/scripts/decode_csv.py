from urllib.parse import unquote
import csv

filename = input('Enter file name: ')
newRows = []

with open(filename, 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        newRows.append([unquote(item, encoding='utf-8') for item in row])

# print(newRows)

with open(f"{filename.split('.csv')[0]}_decoded.csv", 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(newRows)
