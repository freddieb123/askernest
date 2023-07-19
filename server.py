from flask import Flask, request, jsonify
import script
import threading
import logging


app = Flask(__name__)
app.debug = True
logging.basicConfig(level=logging.INFO)


def run_script():
    script.main()

@app.route('/trigger_script', methods=['POST'])
def trigger_script():
    # Call your script here
    thread = threading.Thread(target=run_script)
    thread.start()
    message = 'Script is being run in another thread'
    app.logger.info(message)
    return jsonify({'message': message}), 200

if __name__ == '__main__':
    app.run()
