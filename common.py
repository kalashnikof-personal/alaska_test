from dataclasses import asdict
import json
import random
import requests
import string
import unittest

from bear import Bear, BearType


class Common(unittest.TestCase):
    BASE_URL = "http://0.0.0.0:8091"
    ENDPOINT_BEAR = "/bear"
    ENDPOINT_INFO = "/info"

    METHOD_GET = "GET"
    METHOD_POST = "POST"
    METHOD_PUT = "PUT"
    METHOD_DELETE = "DELETE"

    ALL_BEAR_TYPES = [bt.value for bt in BearType]
    ALL_BEAR_VALUES = Bear.__annotations__.keys()
    MANDATORY_BEAR_VALUES = [bv for bv in ALL_BEAR_VALUES if bv != "bear_id"]

    def make_request(self,
                     method: str = METHOD_GET,
                     endpoint: str = ENDPOINT_BEAR,
                     id_: int = None,
                     payload: str = None,
                     ):
        url = self.BASE_URL + endpoint
        if id_:
            url += "/" + str(id_)
        return requests.request(method, url, data=payload)

    @staticmethod
    def generate_random_str(min_length=5):
        return "".join(random.choice(string.ascii_letters) for _ in range(random.randint(min_length, 20)))

    def generate_bear(self, bear_type):
        return Bear(
            bear_type=bear_type,
            bear_name=self.generate_random_str(),
            bear_age=round(random.uniform(1, 50), 1),
        )
