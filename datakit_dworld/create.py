# -*- coding: utf-8 -*-
import os
from urllib.parse import urlparse

from cliff.command import Command
from datakit import CommandHelpers
import requests

from datakit_dworld.dworld_mixin import DworldMixin


class Create(DworldMixin, CommandHelpers, Command):
    "Create dataset for project on data.world"

    def get_parser(self, prog_name):
        parser = super(Create, self).get_parser(prog_name)
        parser.add_argument(
            '-s', '--slug', help="Slug for this project's URLs on data.world")
        return parser

    def take_action(self, parsed_args):
        payload = self.build_payload(parsed_args)
        self.log.info(
            'Attempting to create dataset {0}/{1} on data.world'.format(
                self.configs['username'], payload['title']))
        dataset_url = self.create_dataset(payload)
        self.log.info('Dataset created: {0}'.format(dataset_url))

    def build_payload(self, parsed_args):
        return {
            'title': self.get_project_slug(parsed_args),
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

        dataset_url = r.json()['uri']
        url_path = urlparse(dataset_url).path
        url_slug = url_path.split('/')[-1]

        settings_data = self.get_settings_data()
        settings_data['slug'] = url_slug
        self.save_settings_data(settings_data)

        return dataset_url

    def get_project_slug(self, parsed_args):
        try:
            return parsed_args.slug.strip()
        except AttributeError:
            raise AttributeError(
                'Must pass project slug for URLs with `--slug`')

    def read_summary_template(self):
        template_path = os.path.join(
            os.path.dirname(__file__), 'assets', 'summary_template.md')
        with open(template_path, 'r') as template_file:
            return template_file.read()
