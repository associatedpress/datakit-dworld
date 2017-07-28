# -*- coding: utf-8 -*-
import os

from cliff.command import Command
from datakit import CommandHelpers
import requests


class Create(CommandHelpers, Command):
    "Create dataset for project on data.world"

    plugin_slug = 'datakit-dworld'

    def take_action(self, parsed_args):
        payload = self.build_payload()
        self.log.info(
            'Attempting to create dataset {0}/{1} on data.world'.format(
                self.configs['username'], payload['title']))
        dataset_url = self.create_dataset(payload)
        self.log.info('Dataset created: {0}'.format(dataset_url))

    def build_payload(self):
        return {
            'title': self.get_project_slug(),
            'summary': self.read_summary_template(),
            'visibility': 'PRIVATE',
        }

    def create_dataset(self, payload):
        url = 'https://api.data.world/v0/datasets/{0}'.format(
            self.configs['username'])
        headers = {
            'Authorization': 'Bearer {0}'.format(self.configs['api_token']),
            'Content-Type': 'application/json',
        }

        r = requests.post(url, json=payload, headers=headers)
        r.raise_for_status()

        return r.json()['uri']

    def get_project_slug(self):
        return os.path.basename(os.getcwd())

    def read_summary_template(self):
        template_path = os.path.join(
            os.path.dirname(__file__), 'assets', 'summary_template.md')
        with open(template_path, 'r') as template_file:
            return template_file.read()
