from flask import *
import pickle
import numpy as np
import pandas as pd
import sklearn
import re
import random
from random import *


from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
from flask_mail import Mail
from flask import Flask, url_for
import json


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('front_page.html')

@app.route('/diabetes_pred')
def diabetes():
    return render_template('diabetes_prediction.html')

def ValuePredictor_diabetes(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,8)
    loaded_model = pickle.load(open("Pickle_files/diabetes_model.pkl", "rb"))
    result_diabetes = loaded_model.predict(to_predict)
    return result_diabetes[0]


@app.route('/diabetes_result', methods=['GET','POST'])
def diabetes_result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if (len(to_predict_list)==8):
            result_diabetes = ValuePredictor_diabetes(to_predict_list)

    if (int(result_diabetes) == 1):
        prediction = 'You Have A Risk Of Diabetes'
    else:
        
        prediction = 'You dont have any Risk Of Diabetes'

    return(render_template('diabetes_prediction.html', prediction_diabetes = prediction))


@app.route('/heart_pred')
def heart():
    return render_template('heart_prediction.html')

def ValuePredictor_heart(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,13)
    loaded_model = pickle.load(open("Pickle_files/heart_model.pkl", "rb"))
    result_heart = loaded_model.predict(to_predict)
    return result_heart[0]


@app.route('/heart_result', methods=['GET','POST'])
def heart_result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if (len(to_predict_list)==13):
            result_heart = ValuePredictor_heart(to_predict_list)

    if (int(result_heart) == 1):
        prediction = 'You Have A Risk Of Heart Attack'
    else:
        prediction = 'You Don"t Have Any Risk Of Heart Attack'

    return(render_template('heart_prediction.html', prediction_heart = prediction))


@app.route('/lung_cancer_pred')
def lung_cancer():
    return render_template('lung_cancer_prediction.html')

def ValuePredictor_lung_cancer(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,17)
    loaded_model = pickle.load(open("Pickle_files/lung_cancer.pkl", "rb"))
    result_lung_cancer = loaded_model.predict(to_predict)
    return result_lung_cancer[0]


@app.route('/lung_cancer_result', methods=['GET','POST'])
def lung_cancer_result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if (len(to_predict_list)==17):
            result_lung_cancer = ValuePredictor_lung_cancer(to_predict_list)

    if (int(result_lung_cancer) == 1):
        prediction = 'You Have A Risk Of Lung Cancer'
    else:
        prediction = 'You Don"t Have Any Risk Of Lung Cancer'

    return(render_template('lung_cancer_prediction.html', prediction_lung_cancer = prediction))


@app.route('/breast_cancer_pred')
def breast_cancer():
    return render_template('breast_cancer_prediction.html')

def ValuePredictor_breast_cancer(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,15)
    loaded_model = pickle.load(open("Pickle_files/breast_cancer.pkl", "rb"))
    result_breast_cancer = loaded_model.predict(to_predict)
    return result_breast_cancer[0]


@app.route('/breast_cancer_result', methods=['GET','POST'])
def breast_cancer_result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if (len(to_predict_list)==15):
            result_breast_cancer = ValuePredictor_breast_cancer(to_predict_list)

    if (int(result_breast_cancer) == 1):
        prediction = 'You Have A Risk Of Breast Cancer'
    else:
        prediction = 'You Don"t Have Any Risk Of Breast Cancer'

    return(render_template('breast_cancer_prediction.html', prediction_breast_cancer = prediction))


@app.route('/liver_pred')
def liver():
    return render_template('liver_prediction.html')

def ValuePredictor_liver(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,10)
    loaded_model = pickle.load(open("Pickle_files/liver_model.pkl", "rb"))
    result_liver = loaded_model.predict(to_predict)
    return result_liver[0]


@app.route('/liver_result', methods=['GET','POST'])
def liver_result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if (len(to_predict_list)==10):
            result_liver = ValuePredictor_liver(to_predict_list)

    if (int(result_liver) == 1):
        prediction = 'You Have A Risk Of Liver Problem'
    else:
        prediction = 'You Don"t Have Any Risk Of Liver Problem'

    return(render_template('liver_prediction.html', prediction_liver = prediction))


@app.route('/fever')
def fever():
    return render_template('fever.html')

@app.route('/fever_result',methods=['GET','POST'])
def fever_result():
    age = request.form.get('Age')
    if int(age) <= int(1):
        return render_template("fever_1.html")
    elif int(age) >= int(2) and int(age) <= int(17):
        return render_template("fever_2.html")
    elif int(age) >= int(18):
        return render_template("fever_3.html")
    else:
        return "Enter the valid age...!";

@app.route('/cough')
def cough():
    return render_template('cough.html')

@app.route('/cough_result',methods=['GET','POST'])
def cough_result():
    age = request.form.get('Age')
    if int(age) <= int(2):
        return render_template("cough_1.html")
    elif int(age) >= int(2) and int(age) <= int(11):
        return render_template("cough_2.html")
    elif int(age) >= int(12) and int(age) <= int(17):
        return render_template("cough_3.html")
    elif int(age) >= int(18):
        return render_template("cough_4.html")
    else:
        return "Enter the valid age...!";






@app.route('/head_ache')
def head_ache():
    return render_template('head_ache.html')

@app.route('/head_ache_result',methods=['GET','POST'])
def head_ache_result():
    age = request.form.get('Age')
    if int(age) <= int(12):
        return render_template("head_ache_1.html")
    elif int(age) > int(12) and int(age) <= int(17):
        return render_template("head_ache_2.html")
    elif int(age) > int(17) and int(age) <= int(65):
        return render_template("head_ache_3.html")
    elif int(age) > int(65):
        return render_template("head_ache_4.html")


@app.route('/heart_treatment')
def heart_treatment():
    return render_template('heart_treatment.html')

@app.route('/heart_doctors',methods=['GET','POST'])
def heart_doctors():
    location = request.form.get('location')
    if int(location) == int(0):
        return render_template("heart_Ludhiana_doctors.html")
    elif int(location) == int(1):
        return render_template("heart_Amritsar_doctors.html")
    elif int(location) == int(2):
        return render_template("heart_Jalandhar_doctors.html")
    


@app.route('/cancer_treatment')
def cancer_treatment():
    return render_template('cancer_treatment.html')

@app.route('/cancer_doctors',methods=['GET','POST'])
def cancer_doctors():
    location = request.form.get('location')
    if int(location) == int(0):
        return render_template("cancer_Ludhiana_doctors.html")
    elif int(location) == int(1):
        return render_template("cancer_Amritsar_doctors.html")
    elif int(location) == int(2):
        return render_template("cancer_Jalandhar_doctors.html")
    


@app.route('/diabetes_treatment')
def diabetes_treatment():
    return render_template('/diabetes_treatment.html')

@app.route('/diabetes_doctors',methods=['GET','POST'])
def diabetes_doctors():
    location = request.form.get('location')
    if int(location) == int(0):
        return render_template("diabetes_Ludhiana_doctors.html")
    elif int(location) == int(1):
        return render_template("diabetes_Amritsar_doctors.html")
    elif int(location) == int(2):
        return render_template("diabetes_Jalandhar_doctors.html")
    
    
# MY db connection
local_server= True
##app = Flask(__name__)
app.secret_key='tanmoy'


# this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/databas_table_name'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/appointmentdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)



# here we will create db models that is tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    usertype=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000))

class Patients(db.Model):
    pid=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50))
    name=db.Column(db.String(50))
    gender=db.Column(db.String(50))
    slot=db.Column(db.String(50))
    disease=db.Column(db.String(50))
    time=db.Column(db.String(50),nullable=False)
    date=db.Column(db.String(50),nullable=False)
    dept=db.Column(db.String(50))
    number=db.Column(db.String(50))

class Doctors(db.Model):
    did=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50))
    doctorname=db.Column(db.String(50))
    dept=db.Column(db.String(50))

class Trigr(db.Model):
    tid=db.Column(db.Integer,primary_key=True)
    pid=db.Column(db.Integer)
    email=db.Column(db.String(50))
    name=db.Column(db.String(50))
    action=db.Column(db.String(50))
    timestamp=db.Column(db.String(50))





# here we will pass endpoints and run the fuction
@app.route('/consultation')
def index():
    return render_template('index.html')
    


@app.route('/doctors',methods=['POST','GET'])
def doctors():

    if request.method=="POST":

        email=request.form.get('email')
        doctorname=request.form.get('doctorname')
        dept=request.form.get('dept')

        query=db.engine.execute(f"INSERT INTO `doctors` (`email`,`doctorname`,`dept`) VALUES ('{email}','{doctorname}','{dept}')")
        flash("Information is Stored","primary")

    return render_template('doctor.html')



@app.route('/patients',methods=['POST','GET'])
@login_required
def patient():
    doct=db.engine.execute("SELECT * FROM `doctors`")

    if request.method=="POST":
        email=request.form.get('email')
        name=request.form.get('name')
        gender=request.form.get('gender')
        slot=request.form.get('slot')
        disease=request.form.get('disease')
        time=request.form.get('time')
        date=request.form.get('date')
        dept=request.form.get('dept')
        number=request.form.get('number')
        if len(number)<10 or len(number)>10:
            flash("Please give 10 digit number")
            return render_template('patient.html',doct=doct)
        subject="APPOINTMENT BOOKING SYSTEM"

  

        query=db.engine.execute(f"INSERT INTO `patients` (`email`,`name`,	`gender`,`slot`,`disease`,`time`,`date`,`dept`,`number`) VALUES ('{email}','{name}','{gender}','{slot}','{disease}','{time}','{date}','{dept}','{number}')")
        




        flash("Booking Confirmed","info")


    return render_template('patient.html',doct=doct)


@app.route('/bookings')
@login_required
def bookings(): 
    em=current_user.email
    if current_user.usertype=="Doctor":
        query=db.engine.execute(f"SELECT * FROM `patients`")
        return render_template('booking.html',query=query)
    else:
        query=db.engine.execute(f"SELECT * FROM `patients` WHERE email='{em}'")
        return render_template('booking.html',query=query)
    


@app.route("/edit/<string:pid>",methods=['POST','GET'])
@login_required
def edit(pid):
    posts=Patients.query.filter_by(pid=pid).first()
    if request.method=="POST":
        email=request.form.get('email')
        name=request.form.get('name')
        gender=request.form.get('gender')
        slot=request.form.get('slot')
        disease=request.form.get('disease')
        time=request.form.get('time')
        date=request.form.get('date')
        dept=request.form.get('dept')
        number=request.form.get('number')
        if len(number)<10 or len(number)>10:
            flash("Please give 10 digit number","warning")
            return redirect('/bookings')
        db.engine.execute(f"UPDATE `patients` SET `email` = '{email}', `name` = '{name}', `gender` = '{gender}', `slot` = '{slot}', `disease` = '{disease}', `time` = '{time}', `date` = '{date}', `dept` = '{dept}', `number` = '{number}' WHERE `patients`.`pid` = {pid}")
        flash("Slot is Updates","success")
        return redirect('/bookings')
    
    return render_template('edit.html',posts=posts)


@app.route("/delete/<string:pid>",methods=['POST','GET'])
@login_required
def delete(pid):
    db.engine.execute(f"DELETE FROM `patients` WHERE `patients`.`pid`={pid}")
    flash("Slot Deleted Successful","danger")
    return redirect('/bookings')






@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        username=request.form.get('username')
        usertype=request.form.get('usertype')
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()
        if user:
            flash("Email Already Exist","warning")
            return render_template('/signup.html')
        encpassword=generate_password_hash(password)

        new_user=db.engine.execute(f"INSERT INTO `user` (`username`,`usertype`,`email`,`password`) VALUES ('{username}','{usertype}','{email}','{encpassword}')")
        # myquery=User(username=username,usertype=usertype,email=email,password=password)
        # myquery.save()
        # this is method 2 to save data in db
        # newuser=User(username=username,email=email,password=encpassword)
        # db.session.add(newuser)
        # db.session.commit()
        flash("Signup Succes Please Login","success")
        return render_template('login.html')

          

    return render_template('signup.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Success","primary")
            return redirect(url_for('index'))
        else:
            flash("invalid credentials","danger")
            return render_template('login.html')    





    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout SuccessFul","warning")
    return redirect(url_for('login'))



@app.route('/test')
def test():
    try:
        Test.query.all()
        return 'My database is Connected'
    except:
        return 'My db is not Connected'
    

@app.route('/details')
@login_required
def details():
    # posts=Trigr.query.all()
    posts=db.engine.execute("SELECT * FROM `trigr`")
    return render_template('trigers.html',posts=posts)


@app.route('/search',methods=['POST','GET'])
@login_required
def search():
    if request.method=="POST":
        query=request.form.get('search')
        dept=Doctors.query.filter_by(dept=query).first()
        name=Doctors.query.filter_by(doctorname=query).first()
        if name:

            flash("Doctor is Available","info")
        else:

            flash("Doctor is Not Available","danger")
    return render_template('index.html')





##if __name__ == "__main__":
    
app.run(debug=True)