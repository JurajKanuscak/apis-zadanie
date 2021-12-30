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
#------------------------------------------------------------------------
#AUTHOR https://apis-zadanie-eshop.herokuapp.com/author

@app.route("/author", methods=["GET"])
def get_author():
  select = ddl_readline("ddl/Select.ddl", 1)
  cursor.execute(select)
  author = cursor.fetchall()
  return jsonify(author), 200

@app.route("/author", methods=["POST"])
def post_author():
  author = dict(request.get_json(force=True))
  values = [author["AuthorName"]]
  insert = ddl_readline("ddl/Insert.ddl", 1, values)
  cursor.execute(insert)
  database.commit()
  values = [author["AuthorName"]]
  select = ddl_readline("ddl/Select.ddl", 9, values)
  cursor.execute(select)
  author = cursor.fetchall()[0]
  return jsonify(author), 200

@app.route("/author/<identificator>", methods=["PUT"])
def put_author(identificator):
  author = dict(request.get_json(force=True))
  update = ddl_readline("ddl/Update.ddl", 1, [author["AuthorName"], author["idAuthor"]])
  cursor.execute(update)
  database.commit()
  return jsonify(f"Author with ID {identificator} has been updated"), 201

@app.route("/author/<identificator>", methods=["DELETE"])
def delete_author(identificator):
  delete = ddl_readline("ddl/Delete.ddl", 1, [identificator])
  cursor.execute(delete)
  database.commit()
  return jsonify(f"Author with ID {identificator} has been deleted"), 204


#------------------------------------------------------------------------
#BOOK https://apis-zadanie-eshop.herokuapp.com/book

@app.route("/book", methods=["GET"])
def get_book():
  select = ddl_readline("ddl/Select.ddl", 2)
  cursor.execute(select)
  book = cursor.fetchall()
  return jsonify(book), 200

@app.route("/book/<identificator>", methods=["PUT"])
def put_book(identificator):
  book = dict(request.get_json(force=True))
  update = ddl_readline("ddl/Update.ddl", 2, [book["idCategory"], book["Title"], book["ISBN"], book["Year"], book["Price"], book["Pages"], book["BookDesc"], book["BookLink"], book["idBook"]])
  cursor.execute(update)
  database.commit()
  return jsonify(f"Product with ID {identificator} has been updated"), 201

@app.route("/book/<identificator>", methods=["DELETE"])
def delete_book(identificator):
  delete = ddl_readline("ddl/Delete.ddl", 2, [identificator])
  cursor.execute(delete)
  database.commit()
  return jsonify(f"Book with ID {identificator} has been deleted"), 204

#------------------------------------------------------------------------
#CATEGORY https://apis-zadanie-eshop.herokuapp.com/category


@app.route("/category", methods=["GET"])
def get_category():
  select = ddl_readline("ddl/Select.ddl", 3)
  cursor.execute(select)
  category = cursor.fetchall()
  return jsonify(category), 200

@app.route("/category/<identificator>", methods=["PUT"])
def put_category(identificator):
  category = dict(request.get_json(force=True))
  update = ddl_readline("ddl/Update.ddl", 3, [category["CategoryDesc"], category["idCategory"]])
  cursor.execute(update)
  database.commit()
  return jsonify(f"Category with ID {identificator} has been updated"), 201

@app.route("/category/<identificator>", methods=["DELETE"])
def delete_category(identificator):
  delete = ddl_readline("ddl/Delete.ddl", 3, [identificator])
  cursor.execute(delete)
  database.commit()
  return jsonify(f"Category with ID {identificator} has been deleted"), 204

#------------------------------------------------------------------------
#CUSTOMER https://apis-zadanie-eshop.herokuapp.com/customer

@app.route("/customer", methods=["GET"])
def get_customer():
  select = ddl_readline("ddl/Select.ddl", 4)
  cursor.execute(select)
  customer = cursor.fetchall()
  return jsonify(customer), 200

@app.route("/customer/<identificator>", methods=["PUT"])
def put_customer(identificator):
  customer = dict(request.get_json(force=True))
  update = ddl_readline("ddl/Update.ddl", 4, [customer["Name"], customer["Surname"], customer["City"], customer["State"], customer["ZipCode"], customer["idCustomer"]])
  cursor.execute(update)
  database.commit()
  return jsonify(f"Customer with ID {identificator} has been updated"), 201

@app.route("/customer/<identificator>", methods=["DELETE"])
def delete_customer(identificator):
  delete = ddl_readline("ddl/Delete.ddl", 4, [identificator])
  cursor.execute(delete)
  database.commit()
  return jsonify(f"Customer with ID {identificator} has been deleted"), 204

#------------------------------------------------------------------------
#ORDER https://apis-zadanie-eshop.herokuapp.com/order

@app.route("/order", methods=["GET"])
def get_order():
  select = ddl_readline("ddl/Select.ddl", 5)
  cursor.execute(select)
  order = cursor.fetchall()
  return jsonify(order), 200

@app.route("/order", methods=["POST"])
def post_order():
  order = dict(request.get_json(force=True))
  values = [order["idCustomer"], order["OrderDate"], order["Price"]]
  insert = ddl_readline("ddl/Insert.ddl", 5, values)
  cursor.execute(insert)
  database.commit()
  select = ddl_readline("ddl/Select.ddl", 5, values)
  cursor.execute(select)
  order = cursor.fetchall()[0]
  return jsonify(order), 200

@app.route("/order/<identificator>", methods=["PUT"])
def put_order(identificator):
  order = dict(request.get_json(force=True))
  update = ddl_readline("ddl/Update.ddl", 5, [order["idCustomer"], customer["OrderDate"], customer["Price"], customer["idOrder"]])
  cursor.execute(update)
  database.commit()
  return jsonify(f"Order with ID {identificator} has been updated"), 201

@app.route("/order/<identificator>", methods=["DELETE"])
def delete_order(identificator):
  delete = ddl_readline("ddl/Delete.ddl", 5, [identificator])
  cursor.execute(delete)
  database.commit()
  return jsonify(f"Order with ID {identificator} has been deleted"), 204


if __name__ == "__main__":
  app.run()
