from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('user_info.html')

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
   book = request.form.get('book')
   name=request.form.get('name')
   address=request.form.get('address')
   card=request.form.get('card')
   return render_template("submit.html",book=book,name=name, address=address, card=card)

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

      book_title = books[book]

      return render_template("user_info.html", cost=cost,book_title = book_title)

@app.route('/select')
def select_book():
   return render_template("select.html")

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)

books = {'book1':"내 집 마련 가계부",
'book2':"오리 집에 왜 왔니",
'book3':"내 마음을 담은 집",
'book4':"내 집 없는 부자는 없다",
'book5':"지금이라도 집을 사야할까요?",
'book6':"강남에 집 사고 싶어요",
'book7':"노후를 위해 집을 이용하라"}