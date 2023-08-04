from flask import Flask, request, jsonify, g, render_template, make_response, redirect
import script
import threading
import logging
import results
from airtable_utils import submit_form_data


app = Flask(__name__, template_folder='Templates')
app.debug = True
logging.basicConfig(level=logging.INFO)


def run_script():
    #with app.app_context():
    books = script.main()
    return books

@app.route("/submitFormData", methods=["POST"])
def handle_form_submission():
    data = request.json
    name = data["name"]
    relation = data["relation"]
    age = data["age"]
    grewup= data["grewup"]
    location = data["location"]
    interests = data["interests"]
    relationship = data["relationship"]
    fic_nonfic = data["fic_nonfic"]
    email = data["email"]
    print (data)

    if submit_form_data(name, relation, age, grewup, location, interests, relationship, fic_nonfic, email):
        books = run_script()
        g.books = books  # Set the books variable in the g context
        return jsonify({"message": "Data inserted successfully", "books": books}), 200
    else:
        return jsonify({"message": "Error inserting data into Airtable"}), 500

@app.route('/', methods=['GET', 'POST'])
def home():
    # Initialize books to None
    books = None
    print(books)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)
