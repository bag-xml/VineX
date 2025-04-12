from flask import Flask, request, jsonify, make_response
import config

from modules import updateManager
from modules import feedManager
from modules import postManager

print(f"[Info] XML Welcomes you to the AMBER backend for bag.xml, made by Daphne Elena Coemen!")
print(f"[Info] AMBER Backend, version 2.0.0, Python build and MySQL optimized.")

app = Flask(__name__)

@app.route('/update', methods=['GET'])
def checkForUpdates():
    version = request.args.get('v')
    amalgum = request.args.get('a')
    return updateManager.checkForUpdate(version, amalgum)

@app.route('/home', methods=['GET'])
def homeFeed():
    return feedManager.loadHomeFeed()

@app.route('/news', methods=['GET'])
def newsFeed():
    return feedManager.loadRecentsFeed()

@app.route('/post-page', methods=['GET'])
def blogpostpage():
    return feedManager.loadBlogsFeed() 

@app.route('/posts', methods=['GET'])
def loadPost():
    id = request.args.get('ix')
    return postManager.loadPost(id)


if __name__ == '__main__':
    app.run(port=config.PORT, host="0.0.0.0", debug=False)
    print(f"[Core] Shutdown sequence completed.")