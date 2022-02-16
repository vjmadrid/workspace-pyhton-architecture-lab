# -*- coding: utf-8 -*-


class NotificationHandler:

    def __init__(self, enabled=True):
        if enabled:
            self.enabled = True
        else:
            self.enabled = False
