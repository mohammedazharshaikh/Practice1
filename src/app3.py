# from flask import Flask, render_template, request, redirect, url_for
# import pandas as pd
# import os

# app = Flask(__name__)

# # Configuration
# app.config['UPLOAD_FOLDER'] = 'static/images'  # Ensure this directory exists
# data = pd.read_csv('people.csv')  # Load the data

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Check if the post request has the file part
#         if 'file' not in request.files:
#             return redirect(request.url)
#         file = request.files['file']
#         name_query = request.form['name'].strip()
#         if file and name_query:
#             # Save the new picture
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             # Update the DataFrame and CSV
#             data.loc[data['Name'].str.lower() == name_query.lower(), 'Picture'] = filename
#             data.to_csv('people.csv', index=False)
#             return redirect(url_for('index'))
#     return render_template('index1.html')

# # @app.route('/update_picture', methods=['GET', 'POST'])
# # def update_picture():
# #     if request.method == 'POST':
# #         name_query = request.form['name'].strip()
# #         if 'file' not in request.files:
# #             return render_template('update_picture.html', message="No file part")
# #         file = request.files['file']
# #         if file.filename == '':
# #             return render_template('update_picture.html', message="No selected file")
# #         if file:
# #             filename = secure_filename(file.filename)
# #             file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #             file.save(file_path)
# #             # Update the record
# #             data.loc[data['Name'].str.lower() == name_query.lower(), 'Picture'] = filename
# #             data.to_csv('people.csv', index=False)  # Save changes back to CSV
# #             return render_template('update_picture.html', message="File uploaded and saved.")
# #     return render_template('update_picture.html')
# #
# @app.route('/update_picture', methods=['GET', 'POST'])
# def update_picture():
#     name_query = ''  # Default empty
#     message = ''
#     if request.method == 'POST':
#         name_query = request.form['name'].strip()
#         if 'file' not in request.files:
#             message = "No file part"
#         file = request.files['file']
#         if file.filename == '':
#             message = "No selected file"
#         if file and message == '':
#             filename = secure_filename(file.filename)
#             file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(file_path)
#             # Update the record
#             data.loc[data['Name'].str.lower() == name_query.lower(), 'Picture'] = filename
#             data.to_csv('people.csv', index=False)  # Save changes back to CSV
#             message = "File uploaded and saved."
#     return render_template('update_picture.html', name=name_query, message=message)


# if __name__ == '__main__':
#     app.run(debug=True)

#2

# from flask import Flask, render_template, request, redirect, url_for
# import pandas as pd
# import os
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# # Configuration
# app.config['UPLOAD_FOLDER'] = 'static/images'  # Ensure this directory exists
# app.config['CSV_FILE'] = 'people.csv'

# # Ensure the upload directory exists
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# data = pd.read_csv(app.config['CSV_FILE'])  # Load the data

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return render_template('index2.html')

# @app.route('/update_picture', methods=['GET', 'POST'])
# def update_picture():
#     if request.method == 'POST':
#         name_query = request.form['name'].strip()
#         if 'file' not in request.files:
#             return render_template('update_picture.html', name=name_query, message="No file part")
#         file = request.files['file']
#         if file.filename == '':
#             return render_template('update_picture.html', name=name_query, message="No selected file")
#         if file:
#             filename = secure_filename(file.filename)
#             file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             # Remove old file if exists
#             old_filename = data.loc[data['Name'].str.lower() == name_query.lower(), 'Picture'].values[0]
#             if old_filename and os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], old_filename)):
#                 os.remove(os.path.join(app.config['UPLOAD_FOLDER'], old_filename))
#             # Save the new file
#             file.save(file_path)
#             print("Upload folder path:", app.config['UPLOAD_FOLDER'])
#             # print("Old file path:", old_file_path)
#             print("New file path:", file_path)

#             # Update the record
#             data.loc[data['Name'].str.lower() == name_query.lower(), 'Picture'] = filename
#             data.to_csv(app.config['CSV_FILE'], index=False)  # Save changes back to CSV
#             return render_template('update_picture.html', name=name_query, message="File uploaded and saved.", filename=filename)
#     else:
#         return render_template('update_picture.html')

# if __name__ == '__main__':
#     app.run(debug=True)
#3

# from flask import Flask, render_template, request, redirect, url_for
# import pandas as pd
# import os
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# # Configuration
# app.config['UPLOAD_FOLDER'] = 'static/images'  # Ensure this directory exists
# app.config['CSV_FILE'] = 'people.csv'
# data = pd.read_csv(app.config['CSV_FILE'])  # Load the data
# data['Picture'].fillna('', inplace=True)  # Ensure no null values in the Picture column

# # Ensure the upload directory exists
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# @app.route('/', methods=['GET'])
# def home():
#     return render_template('index2.html')

# @app.route('/update_picture', methods=['GET', 'POST'])
# def update_picture():
#     global data
#     message = ''
#     if request.method == 'POST':
#         name_query = request.form['name'].strip()
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             if not filename:  # Check if filename is not empty
#                 message = 'File name is invalid.'
#                 return render_template('update_picture.html', message=message)
#             file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             print("fp", file_path)

#             # Check for existing picture and delete if present
#             existing_record = data[data['Name'].str.lower() == name_query.lower()]
#             if not existing_record.empty and existing_record['Picture'].iloc[0]:
#                 old_filename = existing_record['Picture'].iloc[0]
#                 old_file_path = os.path.join(app.config['UPLOAD_FOLDER'], old_filename)
#                 print("old fp", old_file_path)
#                 print("o fn", old_filename)
#                 if old_filename and os.path.exists(old_file_path):
#                     os.remove(old_file_path)

#             # Save the new file
#             file.save(file_path)
#             print("saved fp", file_path)

#             # Update or add the record
#             if not existing_record.empty:
#                 data.loc[data['Name'].str.lower() == name_query.lower(), 'Picture'] = filename
#             else:
#                 # Add new entry if name does not exist
#                 data = data.append({'Name': name_query, 'Picture': filename}, ignore_index=True)
#                 print("data", data)

#             # Save changes back to CSV
#             data.to_csv(app.config['CSV_FILE'], index=False)
#             message = 'File uploaded and saved.'
#         else:
#             message = 'Invalid file or file not provided.'
#     return render_template('update_picture.html', message=message)

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

# if __name__ == '__main__':
#     app.run(debug=True)
#4 mostly same as 3 here proble is replacing image but those dont have image is not able to add new one for them.

# from flask import Flask, render_template, request, redirect, url_for
# import pandas as pd
# import os
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# # Configuration
# app.config['UPLOAD_FOLDER'] = 'static/images'  # Ensure this directory exists
# app.config['CSV_FILE'] = 'people.csv'
# data = pd.read_csv(app.config['CSV_FILE'])  # Load the data
# data['Picture'].fillna('', inplace=True)  # Ensure no null values in the Picture column

# # Ensure the upload directory exists
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# @app.route('/', methods=['GET'])
# def home():
#     return render_template('index2.html')

# @app.route('/update_picture', methods=['GET', 'POST'])
# def update_picture():
#     global data  # Declare data as global to modify it within the function
#     message = ''
#     if request.method == 'POST':
#         name_query = request.form['name'].strip()
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             if not filename:  # Ensure the filename is not empty
#                 message = 'File name is invalid.'
#                 return render_template('update_picture.html', message=message)

#             file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

#             # Check for existing picture and delete if present
#             existing_record = data[data['Name'].str.lower() == name_query.lower()]
#             if not existing_record.empty and existing_record['Picture'].iloc[0]:
#                 old_filename = existing_record['Picture'].iloc[0]
#                 old_file_path = os.path.join(app.config['UPLOAD_FOLDER'], old_filename)
#                 if old_filename and os.path.exists(old_file_path):
#                     os.remove(old_file_path)

#             # Save the new file
#             file.save(file_path)

#             # Update or add the record
#             if not existing_record.empty:
#                 data.loc[data['Name'].str.lower() == name_query.lower(), 'Picture'] = filename
#             else:
#                 # Add new entry if name does not exist
#                 new_entry = {'Name': name_query, 'Picture': filename}
#                 data = data.append(new_entry, ignore_index=True)

#             # Save changes back to CSV
#             data.to_csv(app.config['CSV_FILE'], index=False)
#             message = 'File uploaded and saved.'
#         else:
#             message = 'Invalid file or file not provided.'
#     return render_template('update_picture.html', message=message)

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

# if __name__ == '__main__':
#     app.run(debug=True)
# 5

# from flask import Flask, render_template, request, redirect, url_for
# import pandas as pd
# import os
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# # Configuration
# app.config['UPLOAD_FOLDER'] = 'static/images'  # Ensure this directory exists
# app.config['CSV_FILE'] = 'people.csv'
# data = pd.read_csv(app.config['CSV_FILE'])  # Load the data
# data['Picture'].fillna('', inplace=True)  # Ensure no null values in the Picture column

# # Ensure the upload directory exists
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# @app.route('/', methods=['GET'])
# def home():
#     return render_template('index2.html')

# @app.route('/update_or_add_picture', methods=['GET', 'POST'])
# def update_or_add_picture():
#     global data
#     message = ''
#     if request.method == 'POST':
#         name_query = request.form['name'].strip().lower()
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

#             # Check if the entry exists
#             existing_record = data[data['Name'].str.lower() == name_query]
#             if not existing_record.empty:
#                 # Delete the old picture if it exists
#                 old_filename = existing_record['Picture'].iloc[0]
#                 if old_filename:
#                     old_file_path = os.path.join(app.config['UPLOAD_FOLDER'], old_filename)
#                     if os.path.exists(old_file_path):
#                         os.remove(old_file_path)

#             # Save the new file
#             file.save(file_path)

#             # Update or add the record
#             if not existing_record.empty:
#                 data.loc[data['Name'].str.lower() == name_query, 'Picture'] = filename
#             else:
#                 # Add new entry if name does not exist
#                 new_entry = {'Name': name_query.capitalize(), 'Picture': filename, 'Keywords': ''}
#                 data = data.append(new_entry, ignore_index=True)

#             # Save changes back to CSV
#             data.to_csv(app.config['CSV_FILE'], index=False)
#             message = 'Picture updated or added successfully for "{}".'.format(name_query.capitalize())
#         else:
#             message = 'Invalid file or file not provided.'
#     return render_template('update_or_add_picture.html', message=message)

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

# if __name__ == '__main__':
#     app.run(debug=True)

#6
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
from werkzeug.utils import secure_filename

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
    return render_template('index2.html')

@app.route('/update_or_add_picture', methods=['GET', 'POST'])
def update_or_add_picture():
    global data
    message = ''
    if request.method == 'POST':
        name_query = request.form['name'].strip().lower()
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if filename:  # Check if filename is not empty
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                # Check if the entry exists
                existing_record = data[data['Name'].str.lower() == name_query]
                if not existing_record.empty:
                    # Delete the old picture if it exists
                    old_filename = existing_record['Picture'].iloc[0]
                    if old_filename:
                        old_file_path = os.path.join(app.config['UPLOAD_FOLDER'], old_filename)
                        if os.path.exists(old_file_path):
                            os.remove(old_file_path)


                # Save the new file
                file.save(file_path)

                # Update or add the record
                if not existing_record.empty:
                    data.loc[data['Name'].str.lower() == name_query, 'Picture'] = filename
                else:
                    # Add new entry if name does not exist
                    new_entry = {'Name': name_query.capitalize(), 'Picture': filename, 'Keywords': ''}
                    data = data.append(new_entry, ignore_index=True)

                # Save changes back to CSV
                data.to_csv(app.config['CSV_FILE'], index=False)
                message = 'Picture updated or added successfully for "{}".'.format(name_query.capitalize())
            else:
                message = 'No valid filename provided.'
        else:
            message = 'Invalid file or file not provided.'
    return render_template('update_or_add_picture.html', message=message)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

if __name__ == '__main__':
    app.run(debug=True)
