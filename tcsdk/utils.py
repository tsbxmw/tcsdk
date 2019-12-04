import socket
import sys

from tcsdk.common import default


class Utils(object):

    @property
    def py_version(self):
        return sys.version_info[0]

    @classmethod
    def convert_request_body(cls, data):
        data = cls.to_bytes(data)

        if hasattr(data, '__len__'):
            return data

        return data

    @classmethod
    def version_to_headers(cls):
        return {
            "tcsdk_version": default.TCSDK_VERSION
        }

    @classmethod
    def normalize_endpoint(cls, endpoint):
        while endpoint.endswith("/"):
            endpoint = endpoint[:-1]
        if not endpoint.startswith('http://') and not endpoint.startswith('https://'):
            return 'http://' + endpoint
        else:
            return endpoint

    @classmethod
    def urlparse(cls, endpoint):
        if cls.py_version == 2:
            from urlparse import urlparse
        else:
            from urllib.parse import urlparse
        return urlparse(endpoint)


    @classmethod
    def urlquote(cls, key, safe=None):
        if cls.py_version == 2:
            from urllib import quote as urlquote
        else:
            from urllib.parse import quote as urlquote
        return urlquote(key, safe=safe)


    @classmethod
    def is_ip_or_localhost(cls, netloc):
        """ip or localhost judge"""
        is_ipv6 = False
        right_bracket_index = netloc.find(']')
        if netloc[0] == '[' and right_bracket_index > 0:
            loc = netloc[1:right_bracket_index]
            is_ipv6 = True
        else:
            loc = netloc.split(':')[0]

        if loc == 'localhost':
            return True

        try:
            if is_ipv6:
                socket.inet_pton(socket.AF_INET6, loc)  # IPv6
            else:
                socket.inet_aton(loc) #Only IPv4
        except socket.error:
                return False

        return True

    @classmethod
    def determine_endpoint_type(cls, netloc, is_cname):
        if cls.is_ip_or_localhost(netloc):
            return default.ENDPOINT_TYPE_IP

        if is_cname:
            return default.ENDPOINT_TYPE_CNAME

        return default.ENDPOINT_TYPE_IP

    @classmethod
    def to_bytes(cls, data):
        if cls.py_version == 2:
            from urllib import quote as urlquote, unquote as urlunquote
            from urlparse import urlparse

            def to_bytes(data):
                """unicode to utf-8"""
                if isinstance(data, unicode):
                    return data.encode('utf-8')
                else:
                    return data
            return to_bytes(data)
        else:
            if isinstance(data, str):
                return data.encode(encoding='utf-8')
            else:
                return data

    @classmethod
    def to_string(cls, data):
        """data to str"""
        if cls.py_version == 2:
            return cls.to_bytes(data)
        else:
            if isinstance(data, bytes):
                return data.decode('utf-8')
            else:
                return data

    @classmethod
    def to_unicode(cls, data):
        """data to unicode"""
        if cls.py_version == 2:
            if isinstance(data, bytes):
                return data.decode('utf-8')
            else:
                return data
        else:
            return cls.to_string(data)

    @classmethod
    def stringify(cls, input):
        if cls.py_version == 2:
            if isinstance(input, dict):
                return dict([(cls.stringify(key), cls.stringify(value)) for key, value in input.iteritems()])
            elif isinstance(input, list):
                return [cls.stringify(element) for element in input]
            elif isinstance(input, unicode):
                return input.encode('utf-8')
            else:
                return input
        else:
            return input