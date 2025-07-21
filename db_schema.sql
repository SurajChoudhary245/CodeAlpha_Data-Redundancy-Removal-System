CREATE TABLE validated_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(15),
    address TEXT
);

CREATE TABLE redundant_data_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reason VARCHAR(255),
    data_payload JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);