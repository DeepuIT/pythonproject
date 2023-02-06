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

@app.route('/flower_nectar',methods = ['GET','POST'])
def hello_world2(): 
    if request.method == 'POST':
        model = pickle.load(open('model2.pkl','rb'))
        values = dict(request.form)
        #print(dict(request.form))
        habitat = int(values['habitat'])
        bagging_hour = float(values['bagging_hour'])
        collection_hour = float(values['collection_hour'])
        temp = float(values['temp'])
        hum = float(values['hum'])
        sugarin24 = float(values['sugarin24'])       
        bagging_unbagged = int(values['bagging_unbagged'])
        rinsing_Y = int(values['rinsing_Y'])
        flower_age_o = int(values['flower_age_o'])
        flower_age_y = int(values['flower_age_y'])
        flower_sex_h = int(values['flower_sex_h'])
        flower_sex_m = int(values['flower_sex_m'])    
        output = model.predict([[habitat,bagging_hour,collection_hour,temp,hum,sugarin24,bagging_unbagged,rinsing_Y,flower_age_o,flower_age_y,flower_sex_h,flower_sex_m]])[0]
        print(output)
    else:
        output = 'not predicted yet'        
    return render_template('index2.html',output = output)
 
if __name__ == '__main__': 
	app.run(debug = True)