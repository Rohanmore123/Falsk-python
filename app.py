from flask import Flask, render_template, request, redirect, url_for, session, flash
app=Flask(__name__)


projetcs=[
  {
    'id':1,
    'title':'Time series Forecasting',
    'description':'This is the first project'
  },
  {
    'id':2,
    'title':'Titanic survival prediction',
    'description':'This is the second project'
  },
  {
    'id':3,
    'title':'Rag chatbot',
    'description':'This is the third project'
  }
]
@app.route('/')
def hello_world():
  return render_template('home.html',project=projetcs)



if __name__=='__main__':
  app.run(host= '0.0.0.0',debug=True)
