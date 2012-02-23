# -*- coding: UTF-8 -*-
from django.db import connection

class SQLViewMiddleware(object):
    def process_response(self, request, response):
        for sql in connection.queries:
            print sql
        return response
