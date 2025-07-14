CREATE TABLE validated_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT
);

CREATE TABLE redundant_data_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reason VARCHAR(255),
    data_payload TEXT,
    logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
