from flask import render_template, request ,redirect , url_for , session, flash
from flask import Blueprint
from connectdb import *
from register import *
from login import *
from viewex import *
from addex import *
from delete import *
from edit import *
from admin import *
from reminder import *
from addbill import *
from flask_wtf import FlaskForm
from wtforms import DateField , validators,SubmitField,SelectField,StringField,FloatField,DateTimeLocalField
views = Blueprint(__name__,"views")

class expenseForm(FlaskForm):
    expense = SelectField(u'Expense/Earning', choices=[('expense', 'Expense'),('earn', 'Earn')],validators=(validators.DataRequired(),))
    date = DateField('Expense Date', format='%Y-%m-%d' , validators=(validators.DataRequired(),))
    category = SelectField(u'Expense category', choices=[('Rent', 'Rent'),('Travel', 'Travel'),('Food', 'Food'),('Bills', 'Bills'),('Others', 'Others')],validators=(validators.DataRequired(),))
    note = StringField('Note',validators=(validators.DataRequired(),) )
    currency = SelectField(u'Currency', choices=[('Euro', '€'),('USD', '$'),('INR', '₹'),('YEN', '¥'),('Other', 'Other')],validators=(validators.DataRequired(),))
    amount = FloatField('Amount', [validators.DataRequired()])
    submit = SubmitField('Submit')

class billForm(FlaskForm):
    billtype = StringField('Bill Type',validators=(validators.DataRequired(),) )
    billdue = DateTimeLocalField('Bill Due', format='%Y-%m-%d %H:%M' , validators=(validators.DataRequired(),))
    billamt = FloatField('Bill Amount', [validators.DataRequired()])
    submit = SubmitField('Submit')

@views.route("/")
def home():
    return render_template('home.html')

@views.route("/guest")
def guest():
    return render_template('guest.html')

@views.route("/expenses")
def expenses():
    form = expenseForm()
    return render_template('expenses.html',form=form)

@views.route("/actions", methods=['POST','GET'])
def actions():
    form = expenseForm()
    bills = billForm()
    if request.method == 'POST':
        if request.form.get('action1') == 'Add':
            return render_template("addex.html",form=form)
        elif  request.form.get('action2') == 'View':
            username, id = session['username'],session['id']
            expenses,total = viewex(username,id)
            return render_template("viewex.html",expenses= expenses,total=total)
        elif request.form.get('action3') == 'Bill':
            return render_template("addbill.html",bills =bills )
        exp, date, category, note, cur, amt = request.form['expense'],request.form['date'],request.form['category'],request.form['note'],request.form['currency'],request.form['amount']
        if exp and date and category and note and cur and amt:
            flash('Expense Added')
            username, id = session['username'],session['id']
            addex(id,username,exp,date,category,note,cur,amt)
            return render_template("home.html")
        

@views.route('/delete',methods=['POST','GET'])
def delete():
    if request.method == 'POST':
        flash('Expense Deleted')
        id = request.form.get('action1')
        delex(id)
        username, id = session['username'],session['id']
        expenses,total = viewex(username,id)
        return render_template("viewex.html",expenses= expenses,total=total)


@views.route('/edit',methods=['POST','GET'])
def edit():
    form = expenseForm()
    if request.method == 'POST':
        if(request.form.get('action1')):
            id = request.form.get('action1')
            session['eid'] = id
            return render_template("edit.html",form=form)
        exp, date, category, note, cur, amt = request.form['expense'],request.form['date'],request.form['category'],request.form['note'],request.form['currency'],request.form['amount']
        if exp and date and category and note and cur and amt:
            flash('Expense Edited')
            eid = session['eid']
            edex(exp,date,category,note,cur,amt,eid)
            username, id = session['username'],session['id']
            expenses,total = viewex(username,id)
            return render_template("viewex.html",expenses= expenses,total=total)


@views.route("/loancalc")
def loancalc():
    return render_template('loancalc.html')

@views.route("/login")
def login():
    return render_template('login.html')

@views.route('/successful' , methods=['POST','GET'])
def successful():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        pno = request.form['pno']
        psw = request.form['password']
        psw_repeat = request.form['c_password']
        if psw != psw_repeat:
            return redirect(url_for('views.login'))
        else:
            register(email,pno,username,psw)
            return redirect(url_for('views.home'))
        

@views.route('/user' , methods=['POST','GET'])
def user():
    if request.method == 'POST':
        email = request.form['email']
        psw = request.form['password']
        adminlog = False
        if email.endswith("@admin.com"):
            adminlog,id = a_login(email,psw)
        else:
            loggedin,id,uname = loginf(email,psw)
        if adminlog:
            users = admin()
            return render_template("admin.html",users=users)
        elif loggedin:
            session['username'] = uname
            session['id'] = id
            flash('Login successful')
            return render_template("home.html")
        else:
            flash('Invalid Credentials')
            return redirect(url_for('views.login'))
    return render_template("home.html")

@views.route('bills',methods=['POST','GET'])
def bills():
    if request.method == 'POST':
        billtype = request.form['billtype']
        billdue = request.form['billdue']
        billamt = request.form['billamt']
        uid,uname = session['id'],session['username']
        abill(uid,billtype,billdue,billamt)
        message = 'Bill added'
        flash(message)
        return redirect(url_for('views.home'))