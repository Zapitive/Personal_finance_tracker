from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from views import views
from reminder import *
from apscheduler.schedulers.background import BackgroundScheduler


application = Flask(__name__)

bootstrap = Bootstrap5(application)
application.register_blueprint(views, url_prefix="/")
application.secret_key = 'Hello'

def prins():
   reminder()

scheduler = BackgroundScheduler()
scheduler.add_job(func=prins, trigger="interval", seconds=60)
scheduler.start()

if __name__ == '__main__':
   application.run(debug = True, port =5000)

