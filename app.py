from flask import Flask, request
import json
from slack import send_notification

app = Flask(__name__)

@app.route('/monitorbot', methods=['POST'])
def foo():
    data = request.get_json(silent=True)
    if data[0]["event"] == "check.down":
        url = data[0]["check"]["url"]
        msg = "*Website {} is currently down *".format(url)
        send_notification(msg)
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    app.run()