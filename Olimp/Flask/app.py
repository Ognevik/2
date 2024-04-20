from flask import Flask 
from datetime import datetime 
  
app = Flask(__name__) 
  
@app.route('/') 
def get(): 
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    return { 
        "message": "Это страница сервиса flask компании xsoft", 
        "time": time 
    } 
  
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)