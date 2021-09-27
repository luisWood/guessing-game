def guess(redis_instance):
    return {"guessed_number": redis_instance.get("guessed_number").decode('utf-8'),
            "attempt": redis_instance.get("attempt").decode('utf-8')}


def handle_greater(redis_instance):
    max_guess = int(redis_instance.get("max_guess").decode('utf-8'))
    min_guess = int(redis_instance.get("guessed_number").decode('utf-8')) + 1

    redis_instance.set("min_guess", min_guess)
    redis_instance.set("guessed_number", (max_guess + min_guess) // 2)
    redis_instance.set("attempt", int(redis_instance.get("attempt").decode('utf-8')) + 1)


def handle_lower(redis_instance):
    max_guess = int(redis_instance.get("guessed_number").decode('utf-8')) - 1
    min_guess = int(redis_instance.get("min_guess").decode('utf-8'))

    redis_instance.set("max_guess", max_guess)
    redis_instance.set("guessed_number", (max_guess + min_guess) // 2)
    redis_instance.set("attempt", int(redis_instance.get("attempt").decode('utf-8')) + 1)


def handle_equal(redis_instance):
    return {"message": "Number is predicted successfully! Your selected number is " + redis_instance.get(
        "guessed_number").decode('utf-8'),
            "attempt": redis_instance.get("attempt").decode("utf-8")
            }
