# ☁️ Cloud-Based Data Validation and Redundancy Removal System

This project is a cloud-native application that identifies and filters redundant data using AWS services like Lambda, API Gateway, and RDS.

## 🔧 Features

- Validate new data entries via API.
- Avoids insertion of duplicate records.
- Stores unique entries in the `validated_data` table.
- Logs duplicate data in `redundant_data_log`.
- CORS-enabled frontend form.

## 🛠 Tech Stack

- **Frontend**: HTML, JavaScript
- **Backend**: AWS Lambda (Python)
- **Database**: Amazon RDS (MySQL)
- **API Management**: Amazon API Gateway

## 🔗 API Endpoint

```bash
https://ab8dk51w70.execute-api.ap-south-1.amazonaws.com/default/validate
