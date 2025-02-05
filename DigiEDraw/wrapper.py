
# wrapper.py
from flask import Flask, request
import main
import os

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    uuid = data['uuid']
    filepath = data['filepath']
    db = os.getenv('REDIS_HOST', 'redis')
    eps = data.get('eps', '1')
    
    try:
        main.main(uuid, filepath, db, eps)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

if __name__ == '__main__':
    # Update the config path in main.py
    main.config_path = "/app"
    app.run(host='0.0.0.0', port=5001)
