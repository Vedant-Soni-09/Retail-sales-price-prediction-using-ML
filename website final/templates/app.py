from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def Retail_price_pred():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('index.html',pred='You should sell the goods at'+ Retail_price_pred() +'in corresponding to wholsael price' .format(output))
    elif output>str(0.5):
        return render_template('index.html',pred='You should sell the goods at'+ Retail_price_pred() + 'in corresponding to wholsael price' .format(output))
    else:
        return render_template('index.html',pred="You should'nt sell the goods at"+ Retail_price_pred() + "as it's holiday." .format(output))
    


if __name__ == '__main__':
    app.run(debug=True)