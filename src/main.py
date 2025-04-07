import yaml
from db_operations import ClassicModelsDB

def load_db_config(config_path):
    """
    Load database configuration from a YAML file.
    :param config_path: Path to the YAML configuration file.
    :return: Dictionary containing database configuration.
    """
    try:
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
            return config.get("database", {})
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {config_path}")
        return {}
    except yaml.YAMLError as err:
        print(f"Error parsing YAML file: {err}")
        return {}

def main():
    # Load database configuration from YAML file
    config_path = "db_config.yaml"
    db_config = load_db_config(config_path)

    if not db_config:
        print("Failed to load database configuration. Exiting...")
        return

    # Initialize the database connection
    db = ClassicModelsDB(
        host=db_config.get("host"),
        user=db_config.get("user"),
        password=db_config.get("password"),
        database=db_config.get("database")
    )

    while True:
        print("\nClassic Models Database - CRUD Operations")
        print("1. Create a new record")
        print("2. Read records")
        print("3. Update a record")
        print("4. Delete a record")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            table = input("Enter table name: ")
            columns = input("Enter column names (comma-separated): ").split(",")
            values = input("Enter values (comma-separated): ").split(",")
            data = dict(zip(columns, values))
            db.create_record(table, data)

        elif choice == "2":
            table = input("Enter table name: ")
            limit = int(input("Enter number of records to fetch: "))
            records = db.read_records(table, limit)
            print(f"\nRecords from {table}:")
            for record in records:
                print(record)

        elif choice == "3":
            table = input("Enter table name: ")
            columns = input("Enter column names to update (comma-separated): ").split(",")
            values = input("Enter new values (comma-separated): ").split(",")
            data = dict(zip(columns, values))
            condition = input("Enter condition (e.g., id=1): ")
            db.update_record(table, data, condition)

        elif choice == "4":
            table = input("Enter table name: ")
            condition = input("Enter condition (e.g., id=1): ")
            db.delete_record(table, condition)

        elif choice == "5":
            db.close_connection()
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()