from flask import Flask,render_template

app=Flask(__name__)


@app.route('/home',methods=["POST","GET"])
def home():
    return render_template('home.html')



if(__name__ =='__main__'): #if you run the above main file then on;y run the application
    app.run(debug=True)
