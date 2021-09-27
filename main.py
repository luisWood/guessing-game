from operations import *
from flask import Flask, request
import redis
app = Flask(__name__)


def setup_redis():
    redis_instance = redis.Redis(host='localhost', port=6379, db=0)
    redis_instance.flushdb()

    redis_instance.set("guessed_number", 50)
    redis_instance.set("min_guess", 1)
    redis_instance.set("max_guess", 100)
    redis_instance.set("attempt", 1)
    return redis_instance


@app.route('/', methods=['POST'])
def make_guess():
    redis_instance = redis.Redis(host='localhost', port=6379, db=0)
    action = request.form.get("action")

    if action == '"start"':
        return guess(redis_instance)
    elif action == '">"':
        handle_greater(redis_instance)
        return guess(redis_instance)
    elif action == '"<"':
        handle_lower(redis_instance)
        return guess(redis_instance)
    elif action == '"="':
        return handle_equal(redis_instance)


if __name__ == '__main__':
    setup_redis()
    app.run()

