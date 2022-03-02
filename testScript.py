# -*- coding: utf-8 -*-
import unittest
from unittest import mock
from main import getCommits


class TestAPI(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    expectedDict = {
        "567-HW4a": 4,
        "AAVE-Defi-Sample": 2,
        "Adidas-Confirmed-Practice": 2,
        "Crypto-Lottery": 1,
        "DigiBot": 30,
        "DigiBot-V2": 3,
        "HW4": 2,
        "ssw345project": 13,
        "SupremeBot": 30,
        "sw345": 13,
        "sw567": 12,
        "TappingApp": 4,
        "Twitch-Quiz-Monitor": 5,
        "web3webpage": 7,
        "YeezySupplyAlarm-BypassGenerator": 16,
    }

    @mock.patch("main.getCommits", return_value=expectedDict)
    def testGetCommits(self, mock_get):
        expectedDict = {
            "567-HW4a": 4,
            "AAVE-Defi-Sample": 2,
            "Adidas-Confirmed-Practice": 2,
            "Crypto-Lottery": 1,
            "DigiBot": 30,
            "DigiBot-V2": 3,
            "HW4": 2,
            "ssw345project": 13,
            "SupremeBot": 30,
            "sw345": 13,
            "sw567": 12,
            "TappingApp": 4,
            "Twitch-Quiz-Monitor": 5,
            "web3webpage": 7,
            "YeezySupplyAlarm-BypassGenerator": 16,
        }
        self.assertEqual(getCommits(), expectedDict, "Commits don't match")


if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()
