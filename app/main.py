from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('main.html')

@app.route('/detail', methods = ['POST', 'GET'])
def detail():
   if request.method == 'POST':
      detail = dict()
      detail['Name'] = request.form.get('Name')
      detail['StudentNumber'] = request.form.get('StudentNumber')
      detail['Gender'] = request.form.get('Gender')
      detail['Major'] = request.form.get('Major')
      return render_template("detail.html",detail = detail)

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name')
      result['StudentNumber'] = request.form.get('StudentNumber')
      result['Gender'] = request.form.get('Gender')
      result['Major'] = request.form.get('Major')
      college = request.form.get('College')
      if(college in ['불교대학', '문과대학', '법과대학', '사회과학대학', '경찰사법대학', '경영대학', '사범대학', '미래융합대학']): total = 6938000
      elif(college in ['이과대학']): total = 8050000
      elif(college in ['바이오시스템대학', '공과대학', '예술대학']): total = 9160000
      elif(college in ['약학대학']): total = 11316000
      result['Tuition'] = format(int(total * (1 - int(request.form.get('Scholarship'))/100)), ',d')
      return render_template("result.html",result = result)

@app.route('/calculate', methods = ['POST', 'GET'])
def calculate():
   if request.method == 'POST':
      detail = dict()
      detail['Name'] = request.form.get('Name')
      detail['StudentNumber'] = request.form.get('StudentNumber')
      detail['Gender'] = request.form.get('Gender')
      detail['Major'] = request.form.get('Major')
      return render_template('calculate.html',detail=detail)

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)
