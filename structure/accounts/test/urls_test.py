'''
This file contains 
    - URL testing '
'''

from django.test import SimpleTestCase
from django.urls import (
    resolve,
    reverse
)
from structure.accounts.views.initUser import (
    RegisterView
)

class AccountsTestURL(SimpleTestCase):

    def test_Create_URL (self):
        resolver = resolve('/customer/')
        self.assertEqual(resolver.func.__name__,RegisterView.as_view().__name__)

