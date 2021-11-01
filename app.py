import datetime
# from bokeh.plotting.figure import figure
# from bokeh.embed import components
from flask import Flask, render_template,request,redirect
from werkzeug.utils import redirect
from decimal import Decimal
app=Flask(__name__)




@app.route('/home',methods=['GET','POST'])
def home():
    
    return render_template('home.html')


@app.route('/aboutus',methods=['GET','POST'])
def aboutus():
    if(request.method=='POST'):
        return render_template('aboutus.html')
    else:
        return render_template('aboutus.html')

@app.route('/register',methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route('/sectorwisecomp',methods=['GET','POST'])
def sectorwisecomp():
    return render_template('sectorwisecomp.html')

@app.route('/hotstocks',methods=['GET','POST'])
def hotstocks():
    return render_template('hotstocks.html')


@app.route('/')
def homek():
    return render_template('home.html')
    





if __name__=="__main__":
    app.run(debug=True)