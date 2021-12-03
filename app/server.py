from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('user_info.html')

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
   name=request.form.get('name')
   address=request.form.get('address')
   card=request.form.get('card')
   return render_template("submit.html",name=name, address=address, card=card)

@app.route('/user_info', methods = ['POST', 'GET'])
def user_info():
   if request.method == 'POST':
      book = request.form.get('book')
      if(book in ['book5', 'book6']): cost = 17000
      elif(book in ['book1']): cost = 15000
      elif(book in ['book2']): cost = 14000
      elif(book in ['book3']): cost = 15500
      elif(book in ['book4']): cost = 14400
      elif(book in ['book7']): cost = 14800
      return render_template("user_info.html", cost=cost)

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)
