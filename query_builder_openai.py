# query_builder_openai.py

import json
import openai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load schema
with open("schema_map.json", "r") as f:
    schema = json.load(f)

# Turn schema into prompt-readable format
def format_schema(schema):
    lines = []
    for table, info in schema.items():
        lines.append(f"Table: {table}")
        lines.append(f"Columns: {', '.join(info['columns'])}")
        if info["foreign_keys"]:
            for fk in info["foreign_keys"]:
                lines.append(f"FK: {fk['column']} → {fk['references']}({fk['referred_columns']})")
        lines.append("")  # Blank line between tables
    return "\n".join(lines)

schema_prompt = format_schema(schema)

# === MAIN FUNCTION ===
def get_sql_from_question(question: str) -> str:
    prompt = f"""
You are a data analyst AI. Given a database schema and a user's natural language question, write an SQL query to answer it.

Schema:
{schema_prompt}

Question:
{question}

SQL:
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # You can use "gpt-3.5-turbo" if GPT-4 is not available
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=300,
        )

        sql = response.choices[0].message.content.strip()
        return sql

    except Exception as e:
        return f"-- Error contacting OpenAI: {e}"
