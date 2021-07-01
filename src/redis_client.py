import redis

from src.config import host, port, db, decode_responses


r = redis.Redis(host=host, port=port, db=db, decode_responses=decode_responses)


def get_value_object(key):
    return r.hgetall(key)
