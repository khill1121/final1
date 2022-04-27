from flask import Flask, render_template

app = Flask(__name__)
application = app

import csv

def convert_to_dict(filename):
    datafile = open(filename, newline='')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = list(my_reader)
    datafile.close()
    return list_of_dicts

county_list = convert_to_dict("county.csv")

pairs_list = []
for r in county_list:
    pairs_list.append((r['County'], r['Name']))

@app.route('/')
def index():
    return render_template('index.html', pairs = pairs_list, the_title="Florida Citrus Industry from 2002 to 2021")

@app.route('/county/<num>')
def detail(num):
    try:
        county_dict = county_list[int(num)-1]
    except:
        return f"<h1> Invalid value for county: {num} </h1>"
    return render_template('county.html', county=county_dict, the_title=county_dict['Name'])

if __name__ == '__main__':
    app.run(debug=True)
