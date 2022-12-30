from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index2.html')

@app.route("/routing")
def routing():
    return render_template('routing.html')

@app.route('/get',methods=['GET'])
def get():
    get_data=request.args.get('data')
    print("送信したデータは"+ get_data +"です．")
    return render_template('get.html',get_data=get_data)

@app.route('/post',methods=['POST'])
def post():
    post_data=request.form["field"]
    return render_template('post.html',post_data="送信した値は{}です．".format(post_data))


if __name__ == "__main__":
    app.debug = False
    app.run(port=8080)