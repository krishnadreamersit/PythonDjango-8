# Writting CSV - Write Row
import csv

# Writing on CSV File
with open('data_1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])

# Reading from CSV File
with open('data_1.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

"""
# Writting CSV - Write Rows
import csv
row_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]
with open('data_files/data_2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

# Reading CSV - Comma Delimiter
import csv
with open('data_files/data1.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Reading CSV - Initial Spaces
import csv
with open('data_files/data3.csv', 'r') as file:
    reader = csv.reader(file, skipinitialspace=True)
    for row in reader:
        print(row)

# Writting CSV - Delimiters (Custom Delimiters)
import csv
row_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]

with open('data_files/data_3.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter = '\t')
    writer.writerows(row_list)

# Reading CSV - Delimiters (Custom Delimiters)
import csv
with open('data_files/data_3.csv', 'r') as file:
    reader = csv.reader(file, skipinitialspace=True, delimiter = '\t')
    for row in reader:
        print(row)

# Writting CSV - Quotes
import csv
row_list = [
    ["SN", "Name", "Quotes"],
    [1, "Buddha", "What we think we become"],
    [2, "Mark Twain", "Never regret anything that made you smile"],
    [3, "Oscar Wilde", "Be yourself everyone else is already taken"]
]
with open('data_files/data_4.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
    writer.writerows(row_list)

# Reading CSV - Quotes
import csv
with open('data_files/data_4.csv', 'r') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in reader:
        print(row)

# Writting CSV - Custom Quotes
import csv
row_list = [
    ["SN", "Name", "Quotes"],
    [1, "Buddha", "What we think we become"],
    [2, "Mark Twain", "Never regret anything that made you smile"],
    [3, "Oscar Wilde", "Be yourself everyone else is already taken"]
]
with open('data_files/data_5.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';', quotechar='*')
    writer.writerows(row_list)

# Reading CSV - Custom Quotes
import csv
with open('data_files/data_5.csv', 'r') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';', quotechar='*', skipinitialspace=True)
    for row in reader:
        print(row)

# Reading CSV - Dialect
import csv
csv.register_dialect('dialect1', delimiter='|', skipinitialspace=True, quoting=csv.QUOTE_ALL)
with open('data_files/data5.csv', 'r') as file:
    reader = csv.reader(file, dialect='dialect1')
    for row in reader:
        print(row)

# Reading CSV - Sniffer()
import csv

with open('data_files/data8.csv', 'r') as file:
    sample = file.read(64)
    has_header = csv.Sniffer().has_header(sample)
    print(has_header)
    deduced_dialect = csv.Sniffer().sniff(sample)

with open('data_files/data8.csv', 'r') as file1:
    reader = csv.reader(file1, deduced_dialect)
    for row in reader:
        print(row)

# Writing CSV - DictWriter
import csv

with open('data_files/data_6.csv', 'w', newline='') as file:
    field_names = ('Name','Age','Profession')
    writer = csv.DictWriter(file, fieldnames=field_names, skipinitialspace=True)
    writer.writeheader()
    writer.writerow({'Name': 'Jack', 'Age': '23', 'Profession': 'Doctor'})
    writer.writerow({'Name': 'Miller', 'Age': '22', 'Profession': 'Engineer'})


# Reading CSV - DictReader
import csv
with open('data_files/data_6.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
"""