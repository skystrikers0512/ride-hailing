from flask import Flask, render_template

app = Flask(__name__)

# Sample ride data (in a real system, this would be from a database)
rides = [
    {'id': 1, 'rider': 'Alice', 'driver': 'John Doe', 'status': 'In Progress'},
    {'id': 2, 'rider': 'Bob', 'driver': 'Jane Smith', 'status': 'Completed'}
]

@app.route('/')
def index():
    return render_template('index.html', rides=rides)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    

