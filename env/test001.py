from flask import Flask

# appにFlaskを定義して使えるようにする
app = Flask(__name__)

# @マークはデコレータ
@app.route("/")

# "Hello World"を出力する関数
def hello():
    mes = "Hello World"
    return mes

# プログラムが呼ばれた時に以下の動作をさせる
if __name__ == "__main__":
    app.run()
