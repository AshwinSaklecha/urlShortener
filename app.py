from flask import Flask, request, jsonify, redirect
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
import random
import string

load_dotenv()

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get('long_url')
    custom_code = data.get('custom_code')

    if not long_url:
        return jsonify({"error": "Long URL is required"}), 400

    cursor = mysql.connection.cursor()

    # Check if custom code is provided
    if custom_code:
        cursor.execute("SELECT * FROM urls WHERE short_code = %s", (custom_code,))
        if cursor.fetchone():
            return jsonify({"error": "Custom code already in use"}), 400
        short_code = custom_code
    else:
        # Generate a random short code
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # Save the URL mapping in the database
    cursor.execute("INSERT INTO urls (long_url, short_code) VALUES (%s, %s)", (long_url, short_code))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"long_url": long_url, "short_code": short_code}), 201

@app.route('/<short_code>')
def redirect_url(short_code):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT long_url FROM urls WHERE short_code = %s", (short_code,))
    result = cursor.fetchone()
    cursor.close()

    if result:
        long_url = result[0]
        return redirect(long_url)
    else:
        return jsonify({"error": "URL not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
