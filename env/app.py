from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    list={"0","1","2","3","4","5","6","7","8","9"}
    d=dict(好きな色='紫',好きな科目='科目',好きなゲーム='FPS')
    flag=True
    return render_template('index.html',list=list,d=d,flag=flag)

if __name__ == "__main__":
    app.run(port=8080)