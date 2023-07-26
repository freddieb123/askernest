from flask import Flask, request, jsonify, g, render_template
import script
import threading
import logging



app = Flask(__name__)
app.debug = True
logging.basicConfig(level=logging.INFO)


def run_script():
    with app.app_context():
        g.books = script.main()


@app.route('/trigger_script', methods=['POST'])
def trigger_script():
    # Call your script here
    thread = threading.Thread(target=run_script)
    thread.start()
    message = 'Script is being run in another thread'
    app.logger.info(message)
    return jsonify({'message': message}), 200

@app.route('/')
def home():
    # Check if book recommendations are available
    books = getattr(g, 'books', None)
    print("second")
    if books is None:
        return "No book recommendations available. Try again later."
    # Pass recommendations to template
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
