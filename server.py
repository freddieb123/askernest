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
    with app.app_context():
        g.books = script.main()

@app.route("/submitFormData", methods=["POST"])
def handle_form_submission():
    print('route started1')
    data = request.json
    name = data["name"]
    age = data["age"]
    location = data["location"]
    interests = data["interests"]
    print('route started')

    if submit_form_data(name, age, location, interests):
        return jsonify({"message": "Data inserted successfully"}), 200
    else:
        return jsonify({"message": "Error inserting data into Airtable"}), 500

@app.route('/', methods=['GET', 'POST'])
def home():
    # Check if book recommendations are available
    #books = results.results()
    #print(books)
    #if books is None:
        return render_template('index.html')
    #else:
        #response = make_response(render_template('index.html', books=books), 200)


if __name__ == '__main__':
    app.run(debug=True)
