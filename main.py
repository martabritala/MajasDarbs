#from flask import Flask, render_template

#app = Flask(__name__)
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLALchemy

app = Flask('app')
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class test(db.Model):
  col =db.Column(db.String(255), primary_key=True)
  col2 = c) 
    
    def __repr__ (self):
      return '%r' % self.col

@app.route('/')
def root():
  return ("sveika pasule")
#  return render_template('index.html')
#  return render_template('atminasspele.html')

#@app.route('/atminasspele')
#def spele():
 # return render_template('atminasspele.html')

#@app.route('/kalkulators')
#def kalkulators():
#  return render_template('kalkulators.html')
  
#@app.route('/saites')
#def saites():
#  return render_template('saites.html')
#@app.route('/veidotaji')
#def veidotaji():
#  return render_template('veidotaji.html')

#@app.route('/rezultati')
#def results():
#  return render_template('rezultati.html')

@app.route('/postgreSQL')
def postgreSQL():
  result=test.query.all()
  return '%r' % result

#app.run(host='0.0.0.0', port=8020)
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)