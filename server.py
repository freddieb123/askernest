from flask import Flask, request, jsonify
import script

app = Flask(__name__)

@app.route('/trigger_script', methods=['POST'])
def trigger_script():
    # Call your script here
    script.main()
    return jsonify({'message': 'Script triggered successfully'}), 200

if __name__ == '__main__':
    app.run(port=5000)
