from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample payment data (in a real system, this would be from a payment gateway)
payments = [
    {'id': 1, 'rider': 'Alice', 'amount': 15.50, 'status': 'Paid'},
    {'id': 2, 'rider': 'Bob', 'amount': 20.00, 'status': 'Pending'}
]

@app.route('/')
def index():
    return render_template('index.html', payments=payments)

@app.route('/process_payment', methods=['POST'])
def process_payment():
    rider_id = request.form['rider_id']
    amount = request.form['amount']
    for payment in payments:
        if payment['id'] == int(rider_id):
            payment['status'] = 'Paid'
            return jsonify({'message': f'Payment of {amount} processed for rider {rider_id}'})
    return jsonify({'error': 'Payment not found'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

