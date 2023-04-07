from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from views import views
from reminder import *
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

bootstrap = Bootstrap5(app)
app.register_blueprint(views, url_prefix="/")
app.secret_key = 'Hello'

def prins():
   reminder()

scheduler = BackgroundScheduler()
scheduler.add_job(func=prins, trigger="interval", seconds=60)
scheduler.start()

if __name__ == '__main__':
   app.run(debug = True, port =5000)

