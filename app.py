import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>서버가 html도 보내주나? </h1>"

@app.route("/html_tag")    #라우팅
def html_tag():
    return """
    <h1>첫번째 줄!!!</h1>
    <h2>두번째 줄 !!</h2>
    """
@app.route("/html_file")
def html_file():
    return render_template("html_file.html")
    
@app.route("/welcome/<string:name>")
def welcome(name):
    return render_template("welcome.html", people=name)
    
@app.route("/cube/<int:num>")
def cube(num):
    triple = num*num*num
    return render_template("cube.html",number=triple,num=num)
    
@app.route('/lunch')
def lunch():
    menu = ["삽겹살","김밥","닭갈비","돈까스","소고기"]
    pick = random.choice(menu)
    return render_template("lunch.html",menu=pick)

@app.route('/lotto')
def lotto():
    numbers = list(range(1,46))
    a = random.sample(numbers,6)
    s=sorted(a)
    return render_template("lotto.html",num=s)
    
@app.route('/google')
def naver():
    return render_template("google.html")