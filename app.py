from flask import Flask, render_template, request
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/judge", methods=["POST"])
def judge():
    # クライアントから送られてきた画像を受け取る
    upload = request.files["image"]     #type = file

    # 画像をリサイズする
    buffer = BytesIO()
    img = Image.open(upload)            # type = PIL.JpegImagePlugin.JpegImageFile
    img.thumbnail((500, 500))
    img.save(buffer,format="JPEG")    
    myimage = buffer.getvalue()         # type = bytes
    print(type(myimage))

    # HTMLに渡す用にbase64に変換する
    image_string = base64.b64encode(myimage).decode("utf-8")

    return render_template("judge.html", data = image_string)

if __name__ == "__main__":
    app.run(debug=True)