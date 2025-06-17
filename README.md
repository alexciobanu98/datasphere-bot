# Datasphere Bot

Command-line tool that connects to a PostgreSQL database and lets you run queries using natural language. It reads your database structure, translates plain English questions into SQL (using OpenAI if available), runs the query, and prints the results as a table in the terminal.

## Features

- Connects to a local PostgreSQL database
- Automatically maps tables, columns, and relationships
- Accepts natural language questions and turns them into SQL
- Runs the query and shows results in a clean table
- Works with or without an OpenAI API key

## How it Works

The tool reads your database schema and saves it to a file. When you ask a question, it either:
- Uses a set of hardcoded examples (for offline use) or
- Sends your question and schema to OpenAI to generate SQL.

It then runs the SQL and prints the results.

## Setup

1. Clone this repository:
git clone https://github.com/alexciobanu98/datasphere-bot.git
cd datasphere-bot


2. Install the dependencies:
pip install -r requirements.txt


3. Create a `.env` file in the root folder and add your OpenAI API key:

OPENAI_API_KEY=your_api_key_here



4. Make sure your PostgreSQL database is running and accessible locally.

5. Run the schema reader to generate the schema map:



6. Start the bot:

python main.py



## Example Questions

You can ask questions like:
- total invoices by project
- list projects and their status
- jobs assigned to each foreman
- top 5 clients by invoice value

If OpenAI is not used, the tool will use predefined examples.

## File Overview

- `main.py` — runs the console loop
- `schema_reader.py` — connects to the DB and saves the schema to `schema_map.json`
- `sql_runner.py` — runs SQL queries and prints results
- `query_builder.py` — basic hardcoded question-to-SQL mapping
- `query_builder_openai.py` — OpenAI integration for dynamic SQL generation
- `.env` — stores your API key (not tracked in Git)
- `.gitignore` — excludes temp files and credentials
- `requirements.txt` — dependencies

## Notes

- Schema must be loaded first before asking questions
- Only tested on PostgreSQL so far



