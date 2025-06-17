from sqlalchemy import create_engine, inspect
import json

print("Running schema_reader.py")

# === CONFIG ===
DB_USER = "postgres"
DB_PASSWORD = "Admin123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "my_test_db"
SCHEMA_NAME = "gpm"

def get_schema():
    print("Connecting to database...")

    try:
        engine = create_engine(
            f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
        inspector = inspect(engine)

        print("Connected. Reading schema...")
        schema_map = {}

        tables = inspector.get_table_names(schema=SCHEMA_NAME)
        print(f"Found {len(tables)} tables in schema '{SCHEMA_NAME}'.")

        for table in tables:
            columns = inspector.get_columns(table, schema=SCHEMA_NAME)
            fks = inspector.get_foreign_keys(table, schema=SCHEMA_NAME)

            schema_map[table] = {
                "columns": [col["name"] for col in columns],
                "foreign_keys": [
                    {
                        "column": fk["constrained_columns"],
                        "references": fk["referred_table"],
                        "referred_columns": fk["referred_columns"]
                    } for fk in fks
                ]
            }

        return schema_map

    except Exception as e:
        print(f"Error: {e}")
        return {}

if __name__ == "__main__":
    schema = get_schema()

    if not schema:
        print("No schema found or failed to connect.")
    else:
        print("Schema Summary:")
        for table, info in schema.items():
            print(f"\nTable: {table}")
            print(f"  Columns: {', '.join(info['columns'])}")
            if info['foreign_keys']:
                print(f"  Foreign Keys:")
                for fk in info['foreign_keys']:
                    print(f"    {fk['column']} → {fk['references']}({fk['referred_columns']})")

        with open("schema_map.json", "w") as f:
            json.dump(schema, f, indent=2)
            print("Schema saved to schema_map.json")
