from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for riders (in a real system, this would be from a database)
riders = [
    {'id': 1, 'name': 'Alice', 'location': 'Downtown'},
    {'id': 2, 'name': 'Bob', 'location': 'Uptown'}
]

@app.route('/')
def index():
    return render_template('index.html', riders=riders)

@app.route('/request_ride', methods=['POST'])
def request_ride():
    rider_id = request.form['rider_id']
    pickup_location = request.form['pickup_location']
    for rider in riders:
        if rider['id'] == int(rider_id):
            rider['location'] = pickup_location
            return jsonify({'message': f'Ride requested for {rider_id} at {pickup_location}'})
    return jsonify({'error': 'Rider not found'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
