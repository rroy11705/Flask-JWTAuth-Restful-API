try:
    from pymongo import MongoClient
    from pymongo.errors import ConnectionFailure
    from dotenv import load_dotenv, find_dotenv
    import os

except Exception as e:
    print(f"Error Loading Library: {e}")


DEBUG = True
try:
    client = MongoClient('mongodb://%s:%s@127.0.0.1' % (os.getenv('MONGO_USER_NAME'), os.getenv('MONGO_USER_PASSWORD')))
    DATABASE = client['AuthAPI']

except ConnectionFailure as e:
    print("Connection Error:", e)