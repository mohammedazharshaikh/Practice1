# from flask import Flask, request, render_template
# import pandas as pd

# app = Flask(__name__)

# # Load the data
# data = pd.read_csv('people.csv')  # Ensure this path points to your CSV file.

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         name_query = request.form['name']
#         if name_query:
#             # Search for the name in the dataframe
#             result = data[data['Name'].str.lower() == name_query.lower()]
#             if not result.empty:
#                 picture = result.iloc[0]['Picture']
#                 return render_template('result.html', picture=picture, name=name_query)
#             else:
#                 return render_template('index1.html', message="No name found.")
#         else:
#             return render_template('index1.html', message="Please enter a name.")
#     return render_template('index1.html')

# @app.route('/low_salary')
# def low_salary():
#     # Filter entries with salary less than 99000
#     filtered_data = data[data['Salary'] < 99000]
#     pictures = filtered_data['Picture'].tolist()
#     return render_template('low_salary.html', pictures=pictures)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the data
data = pd.read_csv('people.csv')  # Ensure this path points to your CSV file.
data['Salary'] = pd.to_numeric(data['Salary'], errors='coerce')  # Convert salary to numeric, handling errors.

@app.route('/')
def low_salary():
    # Filter entries with salary less than 99000
    filtered_data = data[data['Salary'] < 99000]
    # Ensure we have valid picture filenames
    pictures = filtered_data['Picture'].dropna().tolist()
    return render_template('low_salary.html', pictures=pictures)

if __name__ == '__main__':
    app.run(debug=True)
