from flask import Flask, request, jsonify
import script
import threading


app = Flask(__name__)

def run_script():
    script.main()

@app.route('/trigger_script', methods=['POST'])
def trigger_script():
    # Call your script here
    thread = threading.Thread(target=run_script)
    thread.start()
    return jsonify({'message': 'Script is being run in another thread'}), 200

if __name__ == '__main__':
    app.run()
