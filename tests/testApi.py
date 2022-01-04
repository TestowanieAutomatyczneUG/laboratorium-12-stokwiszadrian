import json
import unittest
from assertpy import assert_that
from unittest.mock import MagicMock


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.test = MagicMock()
        self.test.get.return_value = json.loads("""{
      "results": [
        {
          "gender": "male",
          "name": {
            "title": "mr",
            "first": "brad",
            "last": "gibson"
          },
          "location": {
            "street": "9278 new road",
            "city": "kilcoole",
            "state": "waterford",
            "postcode": "93027",
            "coordinates": {
              "latitude": "20.9267",
              "longitude": "-7.9310"
            },
            "timezone": {
              "offset": "-3:30",
              "description": "Newfoundland"
            }
          },
          "email": "brad.gibson@example.com",
          "login": {
            "uuid": "155e77ee-ba6d-486f-95ce-0e0c0fb4b919",
            "username": "silverswan131",
            "password": "firewall",
            "salt": "TQA1Gz7x",
            "md5": "dc523cb313b63dfe5be2140b0c05b3bc",
            "sha1": "7a4aa07d1bedcc6bcf4b7f8856643492c191540d",
            "sha256": "74364e96174afa7d17ee52dd2c9c7a4651fe1254f471a78bda0190135dcd3480"
          },
          "dob": {
            "date": "1993-07-20T09:44:18.674Z",
            "age": 26
          },
          "registered": {
            "date": "2002-05-21T10:59:49.966Z",
            "age": 17
          },
          "phone": "011-962-7516",
          "cell": "081-454-0666",
          "id": {
            "name": "PPS",
            "value": "0390511T"
          },
          "picture": {
            "large": "https://randomuser.me/api/portraits/men/75.jpg",
            "medium": "https://randomuser.me/api/portraits/med/men/75.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/men/75.jpg"
          },
          "nat": "IE"
        }
      ],
      "info": {
        "seed": "fea8be3e64777240",
        "results": 1,
        "page": 1,
        "version": "1.3"
      }
    }""")

    def test_randomuser_name(self):
        assert_that(self.test.get("https://randomuser.me/api/")["results"]).extracting("name").contains({
            "title": "mr",
            "first": "brad",
            "last": "gibson"
          })

    def test_randomuser_email(self):
        assert_that(self.test.get("https://randomuser.me/api/")["results"]).extracting("email").is_equal_to(["brad.gibson@example.com"])

    def test_randomuser_login(self):
        assert_that(self.test.get("https://randomuser.me/api/")["results"][0]["login"]).is_equal_to({
            "uuid": "155e77ee-ba6d-486f-95ce-0e0c0fb4b919",
            "username": "silverswan131",
            "password": "firewall",
            "salt": "TQA1Gz7x",
            "md5": "dc523cb313b63dfe5be2140b0c05b3bc",
            "sha1": "7a4aa07d1bedcc6bcf4b7f8856643492c191540d",
            "sha256": "74364e96174afa7d17ee52dd2c9c7a4651fe1254f471a78bda0190135dcd3480"
          })

    def test_randomuser_error(self):
        self.test.get.return_value = json.loads("""
        {
            "error": "Uh oh, something has gone wrong. Please tweet us @randomapi about the issue. Thank you."
        }
        """)
        assert_that(self.test.get("https://randomuser.me/api/")).does_not_contain_key("results")

    def test_randomuser_multipleresults(self):
        self.test.get()["info"] = {
            "seed": "fea8be3e64777240",
            "results": 200,
            "page": 1,
            "version": "1.3"
        }
        assert_that(self.test.get("https://randomuser.me/api/200")["info"]).is_equal_to({"results": 200}, include="results")

    def tearDown(self):
        self.test = None