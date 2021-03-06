# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class RoleTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                       .roles(sid="RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://ip-messaging.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "channel user",
                "type": "channel",
                "permissions": [
                    "sendMessage",
                    "leaveChannel",
                    "editOwnMessage",
                    "deleteOwnMessage"
                ],
                "date_created": "2016-03-03T19:47:15Z",
                "date_updated": "2016-03-03T19:47:15Z",
                "url": "https://chat.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                            .roles(sid="RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                       .roles(sid="RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://ip-messaging.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                            .roles(sid="RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                       .roles.create(friendly_name="friendly_name", type="channel", permission=['permission'])

        values = {
            'FriendlyName': "friendly_name",
            'Type': "channel",
            'Permission': ['permission'],
        }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://ip-messaging.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "channel user",
                "type": "channel",
                "permissions": [
                    "sendMessage",
                    "leaveChannel",
                    "editOwnMessage",
                    "deleteOwnMessage"
                ],
                "date_created": "2016-03-03T19:47:15Z",
                "date_updated": "2016-03-03T19:47:15Z",
                "url": "https://chat.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                            .roles.create(friendly_name="friendly_name", type="channel", permission=['permission'])

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                       .roles.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://ip-messaging.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://chat.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://chat.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "roles"
                },
                "roles": [
                    {
                        "sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "channel user",
                        "type": "channel",
                        "permissions": [
                            "sendMessage",
                            "leaveChannel",
                            "editOwnMessage",
                            "deleteOwnMessage"
                        ],
                        "date_created": "2016-03-03T19:47:15Z",
                        "date_updated": "2016-03-03T19:47:15Z",
                        "url": "https://chat.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                            .roles.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://chat.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://chat.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "roles"
                },
                "roles": []
            }
            '''
        ))

        actual = self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                            .roles.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                       .roles(sid="RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update(permission=['permission'])

        values = {
            'Permission': ['permission'],
        }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://ip-messaging.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "channel user",
                "type": "channel",
                "permissions": [
                    "sendMessage",
                    "leaveChannel",
                    "editOwnMessage",
                    "deleteOwnMessage"
                ],
                "date_created": "2016-03-03T19:47:15Z",
                "date_updated": "2016-03-03T19:47:15Z",
                "url": "https://chat.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                            .roles(sid="RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update(permission=['permission'])

        self.assertIsNotNone(actual)
