# -*- coding: utf-8 -*-
import json
import os

class DworldMixin(object):
    plugin_slug = 'datakit-dworld'

    def get_settings_path(self):
        return os.path.join(os.getcwd(), '.datakit-dworld')

    def get_settings_data(self):
        settings_data = {}
        settings_path = self.get_settings_path()
        if os.path.exists(settings_path):
            with open(settings_path, 'r') as settings_file:
                settings_data = json.load(settings_file)
        return settings_data

    def save_settings_data(self, data):
        settings_path = self.get_settings_path()
        with open(settings_path, 'w') as settings_file:
            json.dump(data, settings_file)