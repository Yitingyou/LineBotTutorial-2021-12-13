from __future__ import unicode_literals
from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests
import json
import configparser
import os
from urllib import parse
app = Flask(__name__, static_url_path='/static')
UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])


config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))
my_line_id = config.get('line-bot', 'my_line_id')
end_point = config.get('line-bot', 'end_point')
client_id = config.get('line-bot', 'client_id')
client_secret = config.get('line-bot', 'client_secret')
HEADER = {
    'Content-type': 'application/json',
    'Authorization': F'Bearer {}'# your code here
}


@app.route("/", methods=['POST'])
def index():
    # your code here
    return 'OK'


@app.route("/callback", methods=['POST'])
def callback():
    # your code here
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    # your code here
    return 'OK'


@app.route("/sendTextMessageToMe", methods=['POST'])
def sendTextMessageToMe():
    # your code here
    return 'OK'


def getNameEmojiMessage():
    message = dict()
    # your code here
    return message


def getCarouselMessage(data):
    message = dict()
    # your code here
    return message


def getLocationConfirmMessage(title, latitude, longitude):
    message = dict()
    # your code here
    return message


def getCallCarMessage(data):
    message = dict()
    # your code here
    return message


def getPlayStickerMessage():
    message = dict()
    # your code here
    return message


def getMRTVideoMessage():
    message = dict()
    # your code here
    return message


def getMRTSoundMessage():
    message = dict()
    # your code here
    return message


def getTaipei101ImageMessage(originalContentUrl=F"{end_point}/static/taipei_101.jpeg"):
    return getImageMessage(originalContentUrl)


def getImageMessage(originalContentUrl):
    message = dict()
    # your code here
    return message


def getTaipei101LocationMessage():
    message = dict()
    # your code here
    return message


def replyMessage(payload):
    # your code here
    return 'OK'


def pushMessage(payload):
    # your code here
    return 'OK'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload_file', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            img_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(img_path)
            # your code here
    return 'OK'


@app.route('/line_login', methods=['GET'])
def line_login():
    if request.method == 'GET':
        code = request.args.get("code", None)
        state = request.args.get("state", None)

        if code and state:
            # your code here
            content = None
            name = content["displayName"]
            userID = content["userId"]
            pictureURL = content["pictureUrl"]
            statusMessage = content["statusMessage"]
            return render_template('profile.html', name=name, pictureURL=
                                   pictureURL, userID=userID, statusMessage=
                                   statusMessage)
        else:
            return render_template('login.html', client_id=client_id,
                                   end_point=end_point)


if __name__ == "__main__":
    app.debug = True
    app.run()
