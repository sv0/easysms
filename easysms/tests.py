# -*- coding: utf-8 -*-
import unittest

from . client import EasySMSClient

__author__ = "Slavik Svyrydiuk"
__email__ = "svyrydiuk@gmail.com"


EASYSMS_URL = "https://100500000000:1234567890@api.easysmsapp.com/accounts/100500000000"


class EasySMSClientTestCase(unittest.TestCase):

    def test_init(self):
        """test __init__ method"""
        client = EasySMSClient(EASYSMS_URL)
        self.assertEqual(client.base_url, 'https://api.easysmsapp.com/accounts/100500000000')
        self.assertEqual(client.hostname, 'api.easysmsapp.com')
        self.assertEqual(client.account_id, '100500000000')
        self.assertEqual(client.auth_token, '1234567890')

    def test_parse_easysms_url(self):
        """test _parse_easysms_url method"""
        self.assertEqual(
            EasySMSClient._parse_easysms_url(EASYSMS_URL),
            {
                'hostname': 'api.easysmsapp.com',
                'username': '100500000000',
                'password': '1234567890',
                'base_url': 'https://api.easysmsapp.com/accounts/100500000000',
            }
        )
