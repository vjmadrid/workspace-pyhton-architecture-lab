# -*- coding: utf-8 -*-


class NotSupportedException(Exception):

    def __init__(self, message, errors):
        super(NotSupportedException, self).__init__(message)
        self.errors = errors


class CustomException(Exception):

    def __init__(self, *args, **kwargs):
        super(CustomException, self).__init__(*args, **kwargs)


def raise_custom_exception():
    raise CustomException('Test to raise custom exception')
