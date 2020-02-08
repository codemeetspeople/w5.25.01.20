import redis


connection_pool = None


def get_connection():
    global connection_pool

    if not connection_pool:
        connection_pool = redis.ConnectionPool(
            host='localhost',
            port=6379,
            db=0,
            decode_responses=True
        )
    return redis.Redis(connection_pool=connection_pool)
