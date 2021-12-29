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

#------------------------------------------------------------------------
#CATEGORY https://apis-zadanie-eshop.herokuapp.com/category


@app.route("/category", methods=["GET"])
def get_category():
  select = ddl_readline("ddl/Select.ddl", 3)
  cursor.execute(select)
  category = cursor.fetchall()
  return jsonify(category), 200

#------------------------------------------------------------------------
#CUSTOMER https://apis-zadanie-eshop.herokuapp.com/customer

@app.route("/customer", methods=["GET"])
def get_customer():
  select = ddl_readline("ddl/Select.ddl", 4)
  cursor.execute(select)
  customer = cursor.fetchall()
  return jsonify(customer), 200

#------------------------------------------------------------------------
#ORDER https://apis-zadanie-eshop.herokuapp.com/order

@app.route("/order", methods=["GET"])
def get_order():
  select = ddl_readline("ddl/Select.ddl", 5)
  cursor.execute(select)
  order = cursor.fetchall()
  return jsonify(order), 200






if __name__ == "__main__":
  app.run()
