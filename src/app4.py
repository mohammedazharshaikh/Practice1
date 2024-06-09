from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/images'  # Ensure this directory exists
app.config['CSV_FILE'] = 'people.csv'
data = pd.read_csv(app.config['CSV_FILE'])  # Load the data
data['Picture'].fillna('', inplace=True)  # Ensure no null values in the Picture column

# Ensure the upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET'])
def home():
    return render_template('index3.html')

@app.route('/remove_entry', methods=['GET', 'POST'])
def remove_entry():
    global data
    message = ''
    if request.method == 'POST':
        name_query = request.form['name'].strip().lower()
        # Find if the entry exists
        existing_record = data[data['Name'].str.lower() == name_query]
        if not existing_record.empty:
            # Delete the picture if it exists
            old_filename = existing_record['Picture'].iloc[0]
            if old_filename:
                old_file_path = os.path.join(app.config['UPLOAD_FOLDER'], old_filename)
                if os.path.exists(old_file_path):
                    os.remove(old_file_path)
            # Remove the data entry
            
            data = data[data['Name'].str.lower() != name_query]
            data.to_csv(app.config['CSV_FILE'], index=False)
            message = 'The entry for "{}" was removed successfully.'.format(name_query.capitalize())
        else:
            message = 'Error: No entry found for the name "{}".'.format(name_query.capitalize())
    return render_template('remove_entry.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
