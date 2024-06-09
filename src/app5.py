from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

# Configuration
app.config['CSV_FILE'] = 'people.csv'
data = pd.read_csv(app.config['CSV_FILE'])  # Load the data

@app.route('/', methods=['GET'])
def home():
    return render_template('index4.html')

@app.route('/update_keywords', methods=['GET', 'POST'])
def update_keywords():
    message = ''
    if request.method == 'POST':
        name_query = request.form['name'].strip().lower()
        new_keywords = request.form['keywords'].strip()
        # Check if the entry exists
        if name_query in data['Name'].str.lower().values:
            # Update the keywords for the given name
            data.loc[data['Name'].str.lower() == name_query, 'Keywords'] = new_keywords
            # Save changes back to CSV
            data.to_csv(app.config['CSV_FILE'], index=False)
            message = 'Keywords updated successfully for "{}".'.format(name_query.capitalize())
        else:
            message = 'Error: No entry found for the name "{}".'.format(name_query.capitalize())
    return render_template('update_keywords.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
