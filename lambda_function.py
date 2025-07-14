import pymysql
import json

# RDS credentials
rds_host = "redundancy-db.c76w26iu0fnd.ap-south-1.rds.amazonaws.com"
db_user = "admin"
db_password = "yourpassword123"
db_name = "redundancy"

def lambda_handler(event, context):
    data = event['data']
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    address = data.get('address')

    connection = pymysql.connect(
        host=rds_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM validated_data WHERE email=%s", (email,))
        result = cursor.fetchone()

        if result:
            cursor.execute(
                "INSERT INTO redundant_data_log (reason, data_payload) VALUES (%s, %s)",
                ("Duplicate email", json.dumps(data))
            )
            connection.commit()
            return {
                "status": "duplicate",
                "message": "Data already exists"
            }
        else:
            cursor.execute(
                "INSERT INTO validated_data (name, email, phone, address) VALUES (%s, %s, %s, %s)",
                (name, email, phone, address)
            )
            connection.commit()
            return {
                "status": "success",
                "message": "Data stored successfully"
            }
