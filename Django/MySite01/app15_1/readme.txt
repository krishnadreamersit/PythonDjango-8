192.168.102.221/app15_1/customers/
Customer - Model
id, fullname, address - Fields

Select all - R
GET 192.168.102.221/app15_1/customers/

Search and display - R
GET 192.168.102.221/app15_1/customers/12

Insert Record - C
POST 192.168.102.221/app15_1/customers/
body -> form data ->
fullname : Name
address  : Address

Update Record - U
PUT 192.168.102.221/app15_1/customers/12
body -> form data ->
fullname : New Name
address  : New Address

Delete Rcord - D
DELETE 192.168.102.221/app15_1/customers/12






