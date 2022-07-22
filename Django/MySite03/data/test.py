import csv

# from app3_1.models  import PersonalInfo
#
# file = open('personal_data.csv')
# csv_reader = csv.reader(file)
# header = []
# header_row = next(csv_reader)
# print(header_row)
# for row in csv_reader:
#         # print(row[0], row[1], row[2], row[3], row[4])
#         pinfo =  PersonalInfo(id=row[0], first_name=row[1],
#                              last_name=row[2], email=row[3], gender=row[4])
#         pinfo.save()
# print("Data Migrate Successfully!")