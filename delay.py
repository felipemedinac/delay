from flask import Flask, request
import time

app = Flask(__name__)


#@app.route("/")
#def home():
#    return "Welcome !!"

@app.route('/time')
def query_example():
    t = int(request.args.get("t"))
    time.sleep(t)
    return f'<h1> Latency added to this request is {t}</h1>'.format(t)



if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True, port=80)
