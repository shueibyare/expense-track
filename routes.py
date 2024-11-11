

from application import  app,db
from flask import render_template,redirect,flash,url_for
from application.form import UserDataForm
from application.models import IncomeExpenses
@app.route("/")
def index():
    return render_template("index.html", title='index')

@app.route('/add', methods = ["POST", "GET"])
def add_expense():
    form = UserDataForm()
    if form.validate_on_submit():
        entry = IncomeExpenses(type=form.type.data, category=form.category.data, amount=form.amount.data)
        db.session.add(entry)
        db.session.commit()
        flash(f"{form.type.data} has been added to {form.type.data}s", "success")
        return redirect(url_for('index'))
    return render_template('add.html', title="Add expenses", form=form)

