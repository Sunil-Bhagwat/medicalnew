# from distutils.command.config import config
from flask import Flask ,render_template,jsonify,request
from models.utils import Medical
import config

app = Flask(__name__)

@app.route("/")
def hello():
    print("we are running flask home api")

    return render_template("index.html")

@app.route("/predict_charge",methods = ["POST","GET"])
def predicted_charge():

    # data = request.form

    # print("data :",data)

    # age = eval(data["age"])
    # sex = data["sex"]
    # bmi = eval(data["bmi"])
    # children = eval(data["children"])
    # smoker = data["smoker"]
    # region = data["region"]
    if request.method == "GET":
        print("we are checking GET method")

        age = int(request.args.get("age"))
        sex = request.args.get("sex")
        bmi = float(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")

        ist = Medical(age,sex,bmi,children,smoker,region)
        charge = ist.predicted_charges()
        print(charge)
        return render_template("index.html",prediction=charge)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=True)

