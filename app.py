from flask import Flask, jsonify, request

import funcs
app = Flask(__name__)

@app.route('/')#Retrieve all users sorted by rank
def get_all_users():
    return jsonify(funcs.get_all_users()),200

@app.route('/user/<user>')
def get_user(user):
    print(user)
    return  jsonify(funcs.get_user(user).to_dict()),200

@app.route('/<song>')
def get_all_song_users(song):
    return jsonify(funcs.get_song_users(song)),200

@app.route('/create',methods=['POST','PUT'])
def insert_user():
    print(request.json)
    if funcs.user_exists(request.json['username']):
        return jsonify(funcs.update_user(request.json['username'],request.json['song'],request.json['highscore'])), 200
    else:
        return jsonify(funcs.create_user(request.json['username'],request.json['song'],request.json['highscore'])), 200

if __name__ == '__main__':
    app.run()