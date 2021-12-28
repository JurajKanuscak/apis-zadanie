from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector as sql

def ddl_readline(file_name, line, values=[]):
  if line < 1: raise IndexError()
  with open(file_name) as file:
    content = file.read().split('\n')
    return content[line - 1].format(*values)

app = Flask(__name__)
CORS(app)

database = sql.connect(
  host="147.232.40.14",
  user="mu468fv",
  password="SeuM4oa0",
  database="mu468fv"
)

cursor = database.cursor(dictionary=True)

@app.route("/", methods=["GET"])
def get_book():
  select = ddl_readline("ddl/Select.ddl", 1)
  cursor.execute(select)
  book = cursor.fetchall()
  return jsonify(book), 200




if __name__ == "__main__":
  app.run()
