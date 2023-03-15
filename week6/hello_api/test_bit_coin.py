import unittest
from unittest import TestCase
from unittest.mock import patch

import bit_coin

class TestExchangeRate(TestCase):
    
    @patch('bit_coin.request_bitcoin_rate')
    def test_convert(self, mock_rates):
        mock_rate = 10000
        example_api_response = {"time":{"updated":"Mar 15, 2023 21:54:00 UTC","updatedISO":"2023-03-15T21:54:00+00:00","updateduk":"Mar 15, 2023 at 21:54 GMT"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"24,474.8095","description":"United States Dollar","rate_float":mock_rate},"GBP":{"code":"GBP","symbol":"&pound;","rate":"20,450.9550","description":"British Pound Sterling","rate_float":20450.955},"EUR":{"code":"EUR","symbol":"&euro;","rate":"23,842.0378","description":"Euro","rate_float":23842.0378}}}
        mock_rates.side_effect = [ example_api_response ]
        converted = bit_coin.convert(5)
        expected = 50000
        self.assertEqual(expected,converted)
        