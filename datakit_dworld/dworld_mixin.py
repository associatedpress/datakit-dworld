# -*- coding: utf-8 -*-
import json
import os


class DworldMixin(object):
    plugin_slug = 'datakit-dworld'

    def get_auth_headers(self):
        return {
            'Authorization': 'Bearer {0}'.format(self.configs['api_token']),
            'Content-Type': 'application/json',
        }

    def get_project_path(self):
        return os.getcwd()

    def get_settings_path(self):
        return os.path.join(
            self.get_project_path(), 'config', 'datakit-dworld.json')

    def get_settings_data(self):
        settings_data = {}
        settings_path = self.get_settings_path()
        if os.path.exists(settings_path):
            with open(settings_path, 'r') as settings_file:
                settings_data = json.load(settings_file)
        return settings_data

    def save_settings_data(self, data):
        settings_path = self.get_settings_path()
        settings_dir = os.path.dirname(settings_path)
        os.makedirs(settings_dir, exist_ok=True)
        with open(settings_path, 'w') as settings_file:
            json.dump(data, settings_file)
