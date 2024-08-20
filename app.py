from flask import Flask, render_template, request, redirect, url_for, flash
import boto3
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For flash messages

# Initialize the SNS client
sns_client = boto3.client('sns', region_name='eu-west-2')  # Adjust region as needed
sns_topic_arn = 'arn:aws:sns:eu-west-2:335871625378:yummy-foods-sns-topic'  # Replace with your SNS Topic ARN

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        print(f"Received POST data: username={username}, email={email}")  # Debugging
        sns_message = json.dumps({
            'type': 'login',
            'username': username,
            'email': email
        })
        try:
            response = sns_client.publish(TopicArn=sns_topic_arn, Message=sns_message)
            print("SNS publish response:", response)  # Debugging
            flash('Login request sent successfully.')
        except Exception as e:
            flash(f'An error occurred: {str(e)}')
            print(f'Failed to send SNS message: {e}')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        print(f"Received POST data: email={email}")  # Debugging
        sns_message = json.dumps({
            'type': 'signup',
            'email': email
        })
        try:
            response = sns_client.publish(TopicArn=sns_topic_arn, Message=sns_message)
            print("SNS publish response:", response)  # Debugging
            flash('Signup request sent successfully.')
        except Exception as e:
            flash(f'An error occurred: {str(e)}')
            print(f'Failed to send SNS message: {e}')
        return redirect(url_for('signup'))
    return render_template('signup.html')

@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        message_id = request.form['message_id']
        email = request.form['email']
        print(f"Received POST data: message_id={message_id}, email={email}")  # Debugging
        sns_message = json.dumps({
            'type': 'contact_us',
            'message_id': message_id,
            'email': email
        })
        try:
            response = sns_client.publish(TopicArn=sns_topic_arn, Message=sns_message)
            print("SNS publish response:", response)  # Debugging
            flash('Contact Us request sent successfully.')
        except Exception as e:
            flash(f'An error occurred: {str(e)}')
            print(f'Failed to send SNS message: {e}')
        return redirect(url_for('contact_us'))
    return render_template('contact_us.html')

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if request.method == 'POST':
        order_id = request.form['order_id']
        email = request.form['email']
        print(f"Received POST data: order_id={order_id}, email={email}")  # Debugging
        sns_message = json.dumps({
            'type': 'order',
            'order_id': order_id,
            'email': email
        })
        try:
            response = sns_client.publish(TopicArn=sns_topic_arn, Message=sns_message)
            print("SNS publish response:", response)  # Debugging
            flash('Order request sent successfully.')
        except Exception as e:
            flash(f'An error occurred: {str(e)}')
            print(f'Failed to send SNS message: {e}')
        return redirect(url_for('orders'))
    return render_template('orders.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
