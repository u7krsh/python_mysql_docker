# Python MySQL Docker

This project demonstrates how to perform CRUD (Create, Read, Update, Delete) operations on a MySQL database (`classicmodels`) using Python. The project is containerized using Docker and uses a YAML configuration file to manage database credentials.

## Features
- Perform CRUD operations on the `classicmodels` database.
- Read database configuration from a YAML file.
- Modular design with separate files for database operations and the main script.
- Easily configurable and extendable.

## Prerequisites
- Python 3.8 or higher
- Docker and Docker Compose
- MySQL server
- `pip` (Python package manager)

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/python_mysql_docker.git
cd python_mysql_docker
```

### 2. Project Structure
```markdown
python_mysql_docker/
├── config/
│   └── db_config.yaml        # YAML file for database configuration
├── src/
│   ├── db_operations.py      # Library for database operations
│   ├── main.py               # Main script for user interaction
├── docker-compose.yml        # Docker Compose configuration
├── Dockerfile                # Dockerfile for the Python application
├── requirements.txt          # Python dependencies
├── start.sql                 # SQL script to set up the database
└── README.md                 # Project documentation
```