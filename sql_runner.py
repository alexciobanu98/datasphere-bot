# sql_runner.py

from sqlalchemy import create_engine, text
from tabulate import tabulate

# === CONFIG ===
DB_USER = "postgres"
DB_PASSWORD = "Admin123"  # ← Use your working password
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "my_test_db"

def run_query(sql_query: str):
    try:
        engine = create_engine(
            f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
        with engine.connect() as connection:
            result = connection.execute(text(sql_query))
            rows = result.fetchall()
            headers = list(result.keys())
            rows_as_lists = [list(row) for row in rows]

            if not rows:
                print("ℹ️ Query returned no results.")
                return

            print(tabulate(rows_as_lists, headers=headers, tablefmt="grid"))
    except Exception as e:
        print(f"❌ Error running query:\n{e}")
