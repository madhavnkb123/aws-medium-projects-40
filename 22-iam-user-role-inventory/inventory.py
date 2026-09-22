import boto3
iam=boto3.client("iam")
print("USERS")
for x in iam.list_users()["Users"]: print(x["UserName"],x["CreateDate"])
print("ROLES")
for x in iam.list_roles()["Roles"]: print(x["RoleName"],x["CreateDate"])