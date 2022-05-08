from firebase_admin import credentials,firestore,initialize_app

cred = credentials.Certificate(r"/home/aionso1/mysite/tilesplayware-firebase-adminsdk-6t132-e19e5290be.json")
default_app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('users')

def get_all_users():
    return sorted([doc.to_dict() for doc in todo_ref.stream()],key=lambda x: x['highscore'],reverse=True)

def get_user(user):
    return todo_ref.document(user).get()

def get_song_users(song):
    users = get_all_users()
    song_users = [su for su in users if song in su['scores']]
    return sorted(song_users,key=lambda x: x['scores'][song],reverse=True)


def create_user(user,song,score):
    print("create")
    todo_ref.document(user).set({
        "username":user,
        "highscore": score,
        "scores": {song:score}
    })
    return {"username":user,
        "highscore": score,
        "scores": {song:score}}

def user_exists(user):
    return True if get_user(user).to_dict() != None else False
def update_user(user,song,score):
    username = get_user(user).to_dict()
    if song in username['scores']:
        if username['scores'][song] < score:
            username['highscore'] = username['highscore'] + score - username['scores'][song]
            username['scores'][song] = score
    else:
        username['scores'][song] = score
        username['highscore'] += score
    todo_ref.document(user).update(username)
    return username

get_all_users()