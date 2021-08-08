##-*- coding: utf-8 -*-

__author__ = 'Víctor Madrid'
__credits__ = ['Víctor Madrid']
__copyright__ = 'Copyright 2021'

__license__ = 'MIT'
__version__ = '1.0.0'
__maintainer__ = ''
__email__ = ''
__status__ = 'Production'

class NotSupportedException(Exception):

    def __init__(self, message, errors):
        super(NotSupportedException, self).__init__(message)
        self.errors = errors