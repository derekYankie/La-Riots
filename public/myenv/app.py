import csv
from flask import Flask
from flask import render_template
from flask import abort

#Create Flask App
app = Flask(__name__)

#Access CSV File
def get_csv():
    csv_path = './static/la-riots-deaths.csv'
    csv_file = open(csv_path,'rb')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list (csv_obj)
    return csv_list
    

#Route index page
@app.route('/')
def index():
    template = 'index.html'
    #Add csv file to webpage
    object_list =  get_csv()
    return render_template(template, object_list = object_list)
    abort(404)

#Deatil page for each report
@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = get_csv()
    for row in object_list:
        if row['id'] == row_id:
            return render_template(template, object=row)
    
            


#configure flask server
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

