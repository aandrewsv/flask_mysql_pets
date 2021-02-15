from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL("pets")
    pets = mysql.query_db("SELECT * FROM pets;")
    print(pets)
    return render_template("index.html",all_pets = pets)

@app.route("/new_pet", methods=["POST"])
def add_new_pet_to_db():
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(na)s, %(ty)s, NOW(), NOW());"
    data = {
        'na': request.form["name"],
        'ty': request.form["type"]
    }
    db = connectToMySQL("pets")
    db.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)