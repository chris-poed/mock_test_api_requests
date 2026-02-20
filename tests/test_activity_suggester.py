from unittest.mock import Mock
from pytest import mark
from lib.activity_suggester import ActivitySuggester
import requests

class TestActivitySuggester():

    @mark.it('Test activity suggester with mock API request')
    def test_activity_suggester_with_mock_API_request(self):
        requester_mock = Mock(name='requester')
        response_mock = Mock(name='response')

        requester_mock.get.return_value = response_mock

        response_mock.json.return_value = {
        "activity": "Write a short story",
        "type": "recreational",
        "participants": 1,
        "price": 0,
        "link": "",
        "key": "6301585",
        "accessibility": 0.1
    }
        
        activity_suggester = ActivitySuggester(requester_mock)
        assert activity_suggester.suggest() == "Why not: Write a short story"
