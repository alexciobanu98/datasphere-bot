# main.py

from query_builder_openai import get_sql_from_question
from sql_runner import run_query

def main():
    print("Ask a question about your data (type 'exit' to quit):")

    while True:
        question = input("You: ")

        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        sql = get_sql_from_question(question)
        print(f"\nGenerated SQL:\n{sql}\n")

        if sql.startswith("-- Sorry"):
            continue

        run_query(sql)
        print("\n" + "-"*60 + "\n")

if __name__ == "__main__":
    main()
