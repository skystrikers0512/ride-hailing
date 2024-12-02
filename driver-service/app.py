from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for drivers (in a real system, this would be from a database)
drivers = [
    {'id': 1, 'name': 'John Doe', 'status': 'Available'},
    {'id': 2, 'name': 'Jane Smith', 'status': 'Unavailable'}
]

@app.route('/')
def index():
    return render_template('index.html', drivers=drivers)

@app.route('/update_status', methods=['POST'])
def update_status():
    driver_id = request.form['driver_id']
    status = request.form['status']
    for driver in drivers:
        if driver['id'] == int(driver_id):
            driver['status'] = status
            return jsonify({'message': f'Driver {driver_id} status updated to {status}'})
    return jsonify({'error': 'Driver not found'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


