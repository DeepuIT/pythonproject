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
        # yes
    return render_template('index.html',output = output)
 
if __name__ == '__main__': 
	app.run(debug = True)