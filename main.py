import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_time():
    return str(datetime.now().timestamp())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)