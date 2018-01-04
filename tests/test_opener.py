# coding: utf-8
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest

import fs
import fs.errors


class TestWebradioOpener(unittest.TestCase):

    def test_open_plist(self):
        x = fs.open_fs('webradio://http://di.fm/mp3/chillout.pls')
        x.close()
