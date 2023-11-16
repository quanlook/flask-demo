# _*_ coding:utf-8 _*_

from flask import Flask, render_template, request,jsonify
app = Flask(__name__)

class ipIfo():

    def __init__(self, ip, hostname, mac):
        self.ip = ip
        self.hostname = hostname
        self.mac = mac

    # toString
    def __repr__(self):
            return f"ipIfo[ip={self.ip},hostname={self.hostname},mac={self.mac}]"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        print(request.form)
        username = request.form.get("username")
        password = request.form.get("pwd")
        if username == "123" and password == "123":
            return "登录成功"
        else:
            return render_template("login.html", msg="登陆失败")
        return 1


@app.route("/ip", methods=["POST"])
def ip():
    res = None
    if request.method == "POST":
        ip = request.json.get("ip")
        hostname = request.json.get("hostname")
        mac = request.json.get("mac")
        res= ipIfo(ip,hostname,mac)
        print(res)
    return res.__dict__



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
