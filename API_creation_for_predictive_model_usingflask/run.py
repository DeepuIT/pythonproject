from flask import Flask,render_template,request
import pickle
app = Flask(__name__) 
 
@app.route('/',methods = ['GET','POST'])
def hello_world(): 
    if request.method == 'POST':
        model = pickle.load(open('model.pkl','rb'))
        values = dict(request.form)
        #print(dict(request.form))
        sepal_length = float(values['sepal_length'])
        sepal_width = float(values['sepal_width'])
        petal_length = float(values['petal_length'])
        petal_width = float(values['petal_width'])
        output = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])[0]
        print(output)
    else:
        output = 'not predicted yet'        
    return render_template('index.html',output = output)

@app.route('/real_estate',methods = ['GET','POST'])
def hello_world2(): 
    if request.method == 'POST':
        model = pickle.load(open('model2.pkl','rb'))
        values = dict(request.form)
        #print(dict(request.form))
        transaction_date = int(values['transaction_date'])
        house_age = float(values['house_age'])
        distance_to_nearest_station = float(values['distance_to_nearest_station'])
        number_of_convenience_stores = int(values['number_of_convenience_stores'])
        latitude = float(values['latitude'])
        longitude = int(values['longitude'])       
        output = model.predict([[transaction_date,house_age,distance_to_nearest_station,number_of_convenience_stores,latitude,longitude]])[0]
        print(output)
    else:
        output = 'not predicted yet'        
    return render_template('index2.html',output = output)
 
if __name__ == '__main__': 
	app.run(debug = True)