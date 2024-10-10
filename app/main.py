# Importing required functions 
from flask import Flask, render_template
from tinydb import TinyDB, Query
from datetime import date, timedelta
import os

# Flask constructor 
app = Flask(__name__)
DATA_DIR = os.environ.get('DATA_DIR')


@app.route('/')
def homepage():
    print("is this running?")
    dataDB = TinyDB(DATA_DIR+'data.json')
    today = (str(date.today()))
    yesterday = (str(date.today() - timedelta(days=1)))
    # Fetching data for Sunday and Monday
    todayData = calculateDay(today, dataDB)
    yesterdayData = calculateDay(yesterday, dataDB)

    # Return the components to the HTML template 
    return render_template(
        template_name_or_list='index.html',
        data1=todayData,
        data2=yesterdayData
        # data1=calculateDay(str(date.today())),
		# data2=calculateDay(str(date.today() - timedelta(days=1))),
    )

def calculateDay(something, database):
    data = []
    Data = Query()
    results = database.search(Data.date.search(something))
    for item in results:
        # print(item['date'].split()[1])
        point = {
            "x": item['date'],
            "y": item['duration'] / 60
        }
        data.append(point)

    return data

# Main Driver Function 
if __name__ == '__main__':
    # Run the application on the local development server
    app.run(host='0.0.0.0', debug=True)


