
from flask import Flask, request, jsonify
import sqlite3

app = Flask("AP-Commuteication")

# Set up the database connection
def get_db_connection():
    conn = sqlite3.connect('routes.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/submit-rating', methods=['POST'])
def submit_rating():
    data = request.get_json()
    rating = data['rating']
    route_id = data['routeId']

    conn = get_db_connection()
    conn.execute('INSERT INTO route_ratings (route_id, rating) VALUES (?, ?)', (route_id, rating))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)