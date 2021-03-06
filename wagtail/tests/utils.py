from contextlib import contextmanager
import warnings

from django.contrib.auth import get_user_model
from django.utils import six


class WagtailTestUtils(object):
    def login(self):
        # Create a user
        user = get_user_model().objects.create_superuser(username='test', email='test@email.com', password='password')

        # Login
        self.client.login(username='test', password='password')

        return user

    def assertRegex(self, *args, **kwargs):
        six.assertRegex(self, *args, **kwargs)

    @staticmethod
    @contextmanager
    def ignore_deprecation_warnings():
        with warnings.catch_warnings(record=True) as warning_list:  # catch all warnings
            yield

        # rethrow all warnings that were not DeprecationWarnings
        for w in warning_list:
            if not issubclass(w.category, DeprecationWarning):
                warnings.showwarning(message=w.message, category=w.category, filename=w.filename, lineno=w.lineno, file=w.file, line=w.line)
