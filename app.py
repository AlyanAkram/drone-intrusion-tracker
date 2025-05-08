from flask import Flask, render_template, request, redirect
import csv
import os
from map_generator import *

app = Flask(__name__)

CSV_FILE = 'data/sightings.csv'

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = [
        request.form['date'],
        request.form['time'],
        request.form['location'],
        request.form['latitude'],
        request.form['longitude'],
        request.form['drone_type'],
        request.form['source']
    ]
    # Append to CSV
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)

    # Regenerate the map
    generate_map()

    return redirect('/map')

@app.route('/map')
def map_view():
    return app.send_static_file('drone_map.html')

# Generate map on server start
if not os.path.exists('drone_map.html'):
    generate_map()

if __name__ == '__main__':
    app.run(debug=True)
