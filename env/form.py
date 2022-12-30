from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/form",methods=['GET'])
def form():
    request_data=request.args.get('data')
    return render_template('form.html',request_data=request_data)

if __name__ == "__main__":
    app.run()
