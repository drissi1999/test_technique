from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Expression(BaseModel):
    expression: str

def init_db():
    conn = sqlite3.connect('operations.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS operations (
                        id INTEGER PRIMARY KEY,
                        expression TEXT,
                        result REAL
                    )''')
    conn.commit()
    conn.close()

init_db()

@app.post("/calculate")
def calculate(expression: Expression):
    try:
        result = evaluate_rpn(expression.expression)
        conn = sqlite3.connect('operations.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO operations (expression, result) VALUES (?, ?)", (expression.expression, result))
        conn.commit()
        conn.close()
        return {"expression": expression.expression, "result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/operations")
def get_operations():
    conn = sqlite3.connect('operations.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM operations")
    operations = cursor.fetchall()
    conn.close()
    return operations

@app.get("/operations/csv")
def get_operations_csv():
    import csv
    from fastapi.responses import FileResponse
    
    conn = sqlite3.connect('operations.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM operations")
    operations = cursor.fetchall()
    conn.close()
    
    with open("operations.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Expression", "Result"])
        writer.writerows(operations)
    
    return FileResponse("operations.csv", media_type='text/csv', filename="operations.csv")
