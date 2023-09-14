from flask import Flask, request
import requests

TEMPLATE = """
<HTML>
    <BODY>
        <h1> Sample App </h1>
        <form method = "POST" enctype = "multipart/form-data">
            Insert Image Here<br />
            <input type = "file" name = "image" /> <br />
            <button type = "submit"> Submit </button>
        </form>
        
        Prediction: {res}
    </BODY>
</HTML>

"""

app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def home():
    res = "None"
    if request.method == "POST":

        f = request.files["image"]  
        f.save("targetfile.jpg")
        img = {'image': open("targetfile.jpg", 'rb')}

        res = requests.post("http://127.0.0.1:5000/getPredictions", files = img)
        res = res.json()["prediction"]
    return TEMPLATE.format(res = res)

if __name__ == "__main__":
    app.run(port = 8080, debug = True)