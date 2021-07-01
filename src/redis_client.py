import redis

from src.config import host, port, db, decode_responses


def get_redis_connection():
    return redis.Redis(host=host, port=port, db=db, decode_responses=decode_responses)


def get_value_object(redis_connection, key):
    return redis_connection.hgetall(key)
