__author__ = 'fede'

from collections import MutableMapping
from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from itertools import chain

class LSPD(MutableMapping):

    def __init__(self, hashers = None):
        self._dict = {}
        self._hashers = hashers if hashers else (md5, sha1, sha224, sha256, sha384, sha512)

    def calculate_key(self, key):
        return "".join((f(key).digest() for f in self._hashers))

    def __contains__(self, key):
        return self.calculate_key(key) in self._dict

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def __getitem__(self, key):
        return self._dict[self.calculate_key(key)]

    def __setitem__(self, key, value):
        self._dict[self.calculate_key(key)] = value

    def __delitem__(self, key):
        del self._dict[self.calculate_key(key)]

class LSPSSDD(MutableMapping):

    def __init__(self, hashers = None):
        self._short_keys_dict = {}
        self._dict = LSPD(hashers)
        self._short_keys_lenght = len(self._dict.calculate_key("a"))

    def __contains__(self, key):
        if len(key) < self._short_keys_lenght:
            return key in self._short_keys_dict
        else:
            return key in self._dict

    def __iter__(self):
        return chain(iter(self._short_keys_dict), iter(self._dict))

    def __len__(self):
        return len(self._dict) + len(self._short_keys_dict)

    def __getitem__(self, key):
        if len(key) < self._short_keys_lenght:
            return self._short_keys_dict[key]
        else:
            return self._dict[key]

    def __setitem__(self, key, value):
        if len(key) < self._short_keys_lenght:
            self._short_keys_dict[key] = value
        else:
            self._dict[key] = value

    def __delitem__(self, key):
        if len(key) < self._short_keys_lenght:
            del self._short_keys_dict[key]
        else:
            del self._dict[key]


