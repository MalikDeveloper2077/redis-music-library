import redis

host = 'localhost'
port = 6379
db = 0
decode_responses = True
song_key_prefix = 'song'

r = redis.Redis(host=host, port=port, db=db, decode_responses=decode_responses)
