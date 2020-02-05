#!/usr/bin/env python3
import json
import requests
import urllib.parse



class FailedAuthentication(Exception):
    def __init__(self, value=''):
        self.value = value
    def __str__(self):
        return repr(self.value)



class RESTSession(object):
    TESLA_CLIENT_ID="81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384"
    TESLA_CLIENT_SECRET="c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3"

    def __init__(self, username, password, uri='https://owner-api.teslamotors.com'):
        self.uri = urllib.parse.urljoin(uri,'')
        self.username = username
        self.login(password)

    def login(self, password):
        endpoint = 'oauth/token'
        auth_uri = urllib.parse.urljoin(self.uri, endpoint)
        self.sess = requests.Session()
        self.sess.headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=UTF-8'
            });
        d = json.dumps({
                'grant_type': "password",
                'client_id': RESTSession.TESLA_CLIENT_ID,
                'client_secret': RESTSession.TESLA_CLIENT_SECRET,
                'email': self.username, 
                'password': password
                })
        r = self.sess.post(
            auth_uri,
            data=d)
        if r.status_code != 200:
            print(r)
            print(r.text)
            raise FailedAuthentication
        else:
            token = json.loads(r.text)['access_token']
            self.sess.headers["Authorization"] = "Bearer {}".format(token)

    def post(self, uri, data={}, params={}):
        full_uri = urllib.parse.urljoin(self.uri, uri)
        return self.sess.post(full_uri, data=data, params=params)

    def get(self, uri, params={}):
        full_uri = urllib.parse.urljoin(self.uri, uri)
        return self.sess.get(full_uri, params=params)

    def patch(self, uri, data={}, params={}):
        full_uri = urllib.parse.urljoin(self.uri, uri)
        return self.sess.patch(full_uri, data=data, params=params)

    def put(self, uri, data={}, params={}):
        full_uri = urllib.parse.urljoin(self.uri, uri)
        return self.sess.put(full_uri, data=data, params=params)

    def delete(self, uri, data={}, params={}):
        full_uri = urllib.parse.urljoin(self.uri, uri)
        return self.sess.delete(full_uri, data=data, params=params)