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
    age = data["age"]
    location = data["location"]
    interests = data["interests"]
    print data

    if submit_form_data(name, age, location, interests):
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
    if books is None:
        return render_template('index.html')
    else:
        # Redirect to the new page with books data as a query parameter
        return redirect(url_for('display_books', books=books))

@app.route('/display_books')
def display_books():
    # Retrieve the books data from the query parameter
    books = request.args.get('books')

    # Render the template with the books data
    return render_template('books_table.html', books=books)


if __name__ == '__main__':
    app.run(debug=False)
