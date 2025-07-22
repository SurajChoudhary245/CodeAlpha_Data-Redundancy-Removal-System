# Data Redundancy Removal System

This project implements a cloud-based system to validate and duplicate data using AWS services.

## Features

- Accepts data (Name, Email, Phone, Address) via an API Gateway.
- Uses AWS Lambda (Python) to process the data.
- Stores validated data into AWS RDS (MySQL).
- Logs redundant data with reasons into a separate table.
- CORS support for frontend integration.

## Tech Stack

- **Frontend**: HTML + JavaScript
- **Backend**: AWS Lambda (Python)
- **Database**: AWS RDS (MySQL)
- **Other Services**: API Gateway

## Lambda Function Logic

1. Accepts POST request with JSON payload.
2. Parses and validates required fields.
3. Connects to RDS and checks for existing email in `validated_data`.
4. If duplicate, logs into `redundant_data_log` with reason.
5. If unique, inserts into `validated_data`.

## Database Schema

See `db_schema.sql` file.

## How to Deploy

1. Deploy the Lambda function with the given Python code.
2. Set up API Gateway to trigger the Lambda function.
3. Create the MySQL RDS instance and apply the schema from `db_schema.sql`.
4. Connect frontend with API Gateway endpoint.

## Author

Suraj Choudhary
