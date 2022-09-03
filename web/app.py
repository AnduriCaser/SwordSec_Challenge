from flask import Flask
from flask import Flask, request, jsonify
from missions import create_file, create_user
from db import db_session ,init_db
from model import UserModel
import redis
import sys
from rq import Queue


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    with app.app_context():
        init_db()

    return app


app = create_app()
redis_client = redis.Redis("redis", 6379)
redis_queue = Queue(connection=redis_client)


@app.route('/users', methods=['POST'])
def users():
    try:
        if type(request.get_json()) == list:
            users = request.get_json()
            task = redis_queue.enqueue(create_user, users)

            return jsonify({'status': 'OK'}, 201)
        else:
            file = request.get_json()['file']
            task_save = redis_queue.enqueue(create_file, file)

            return jsonify({'status_file': 'OK'}, 201)

    except Exception as e:
        return e.args


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
