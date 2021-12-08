from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def mainpage():
   return render_template("main.html")

@app.route('/login', methods = ['POST', 'GET'])
def login():
   error = None
   if request.method == 'POST':
      if request.form['username'] != 'ossp' or request.form['password'] != 'ossp1234':
         error = '아이디 또는 비밀번호가 올바르지 않습니다. 다시 입력해 주십시오'
      else:
         return render_template("select.html")
   return render_template("login.html", error = error)

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
   book = request.form.get('book')
   book_len = request.form.get('book_len')
   name=request.form.get('name')
   address=request.form.get('address')
   card=request.form.get('card')
   return render_template("submit.html",book=book,name=name, address=address, card=card,book_len=book_len)

@app.route('/user_info', methods = ['POST', 'GET'])
def user_info():
   if request.method == 'POST':
      book = request.form.get('book')

      book_list = request.form.getlist('book')
      book_len = len(book_list)

      book_title = books[book]

      return render_template("user_info.html", book_title = book_title,book_len = book_len)

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