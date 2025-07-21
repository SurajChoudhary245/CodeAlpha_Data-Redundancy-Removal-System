import json
import pymysql

# RDS config
rds_host = "redundancy-data.c76w26iu0fnd.ap-south-1.rds.amazonaws.com"
db_user = "admin"
db_password = "your_password"
db_name = "redundancy-data"

def lambda_handler(event, context):
    body = json.loads(event['body'])

    name = body['name']
    email = body['email']

    connection = pymysql.connect(
        host=rds_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = connection.cursor()

    # Check if email already exists
    cursor.execute("SELECT * FROM data_entries WHERE email = %s", (email,))
    result = cursor.fetchone()

    if result:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Duplicate entry! Data not inserted.'})
        }

    # Insert unique entry
    cursor.execute("INSERT INTO data_entries (name, email) VALUES (%s, %s)", (name, email))
    connection.commit()

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Data inserted successfully!'})
    }
