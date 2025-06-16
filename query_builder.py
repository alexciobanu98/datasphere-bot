# query_builder.py

def get_sql_from_question(question: str) -> str:
    q = question.lower()

    if "projects by status" in q:
        return 'SELECT "name", "status" FROM gpm."Project" LIMIT 5;'

    elif "total invoices" in q:
        return '''
        SELECT p."name" AS project_name, SUM(ci."totalAmount") AS total_invoice_amount
        FROM gpm."CompanyInvoice" ci
        JOIN gpm."Project" p ON ci."projectId" = p."id"
        GROUP BY p."name"
        ORDER BY total_invoice_amount DESC
        LIMIT 5;
        '''

    else:
        return "-- Sorry, I don’t understand that question yet."
