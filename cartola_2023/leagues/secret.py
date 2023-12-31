from decouple import config
import os


def get_secret(sercret: str):
    if os.environ.get(sercret) is None:
        print("Using decouple")
        return config(sercret)
    print("Using os")
    return os.environ.get(sercret)
