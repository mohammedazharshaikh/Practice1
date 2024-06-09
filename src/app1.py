from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the data
data = pd.read_csv('people.csv')  # Update the path to where your CSV file is stored.

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name_query = request.form['name']
        if name_query:
            # Search for the name in the dataframe
            result = data[data['Name'].str.lower() == name_query.lower()]
            if not result.empty:
                picture = result.iloc[0]['Picture']
                return render_template('result.html', picture=picture, name=name_query)
            else:
                return render_template('index1.html', message="No name found.")
        else:
            return render_template('index1.html', message="Please enter a name.")
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)
