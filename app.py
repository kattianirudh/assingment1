from ast import keyword
from colorama import Cursor
from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
import pyodbc
# import functions py file
from functions import *

app = Flask(__name__)
# CORS(app)
server = 'adb6.database.windows.net'
database = 'assignment1'
username = 'axk3905'
password = 'Password@123'
driver = '{ODBC Driver 18 for SQL Server}'

class Main():
    cursor = ''
    data = ''
    @app.route('/')
    def index():
        cursor = Main.connect_db()
        data = get_sql_data(cursor)
        return render_template('displaydata.html', data=data)

    @app.route('/upload', methods=['POST'])
    def upload():
        isImageAvaiable = False
        isCsvAvaiable = False
        if request.method == 'POST':
            if 'images' in request.files:
                file_extension = request.files['images'].filename.split('.')[-1]
                if file_extension in ['png', 'jpg', 'jpeg']:
                    process_image(request.files['images'])
                isImageAvaiable = True

            if 'csv' in request.files:
                isCsvAvaiable = True
        
            return render_template('uploaded.html', isImageAvaiable=isImageAvaiable, isCsvAvaiable=isCsvAvaiable)
        else:
            return jsonify({'outside the scope': False})
    
    @app.route('/uploadcsv', methods=['POST'])
    def uploadcsv():
        if request.method == 'POST':
            if 'csv' in request.files:
                csv = request.files['csv']
                csv.save(csv.filename)
                return jsonify({'success': True})
            else:
                return jsonify({'success': False})
        else:
            return jsonify({'success': False})

    @app.route('/get_images')
    def get_images():
        return jsonify({'images': True})

    @app.route('/get_csv')
    def get_csv():
        return jsonify({'csv': True})

    @app.route('/filter', methods=['POST'])
    def filter():
        if request.method == 'POST':
            if 'name' in request.form or 'salary' in request.form:
                cursor = Main.connect_db()
                data = get_sql_data(cursor)
                filtered_data = []
                name = request.form['name']
                salary = request.form['salary']
                print("Name: ", name)
                if name:
                    for row in data:
                        print("Row: ", row[1] == name)
                        if row[1] == name:
                            filtered_data.append(row)
                if salary and salary > 0:
                    for row in filtered_data:
                        if row[2] >= salary:
                            filtered_data.append(row)
        return render_template('filterednames.html', data=filtered_data)
                
    def process_image(self, image):
        cursor = self.connect_db()

    def connect_db():
        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        return cursor


    @app.route('/updatedata', methods=['POST'])
    def updatedata():
        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        print("id is--------------------------------------------"+ request.form['id'])
        if request.method == 'POST':
            id = ''
            name = ''
            salary = ''
            image = ''
            keywords = ''
            if 'id' in request.form:
                id = request.form['id']
            if 'name' in request.form:
                name = request.form['name']
            if 'salary' in request.form:
                salary = request.form['salary']
            if 'image' in request.form:
                image = request.form['image']
            if 'keywords' in request.form:
                keywords = request.form['keywords']

            cursor = Main.connect_db()
            cursor.execute("UPDATE Employees SET Name = %s, Salary = %s, Picture = %s, Keywords = %s WHERE Id = %s;", (name, salary, image, keywords, id))
            cnxn.commit()

            return jsonify({'success': True})
        else:
            return jsonify({'success': False})

        

if __name__ == "__main__":

  app.logger.debug("Loading ")

  app.run(
    host='0.0.0.0', 
    port=9001)

        
    

