# -*- coding: utf-8 -*-
import os

from cliff.command import Command
from datakit import CommandHelpers
import requests

from datakit_dworld.dworld_mixin import DworldMixin


class Summary(DworldMixin, CommandHelpers, Command):
    "Update summary for dataset on data.world"

    def take_action(self, parsed_args):
        friendly_name = '{0}/{1}'.format(
            self.configs['username'], self.get_project_slug())
        try:
            payload = self.build_payload(parsed_args)
        except FileNotFoundError:
            summary_path = self.get_summary_path()
            self.log.warning(
                'Summary file not found! Downloading existing summary.')
            self.download_summary(summary_path)
            return

        self.log.info((
            'Attempting to update summary for dataset '
            '{0} on data.world').format(friendly_name))
        summary_length = self.update_summary(
            self.configs['username'], self.get_project_slug(), payload)
        self.log.info('Updated summary ({0} bytes) for dataset {1}'.format(
            summary_length, friendly_name))

    def build_payload(self, parsed_args):
        return {
            'summary': self.read_summary_content(),
        }

    def download_summary(self, output_path):
        url = 'https://api.data.world/v0/datasets/{0}/{1}'.format(
            self.configs['username'], self.get_project_slug())

        r = requests.get(url, headers=self.get_auth_headers())
        r.raise_for_status()

        try:
            summary = r.json()['summary']
        except KeyError:
            self.log.warning(
                'No summary found for this dataset! Using built-in template.')
            template_path = os.path.join(
                os.path.dirname(__file__), 'assets', 'summary_template.md')
            with open(template_path, 'r') as template_file:
                summary = template_file.read()

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as output_file:
            bytes_written = output_file.write(summary)
        self.log.info('Wrote {0} bytes to {1}'.format(
            bytes_written, os.path.abspath(output_path)))

    def update_summary(self, dataset_owner, dataset_id, payload):
        url = 'https://api.data.world/v0/datasets/{0}/{1}'.format(
            dataset_owner, dataset_id)

        r = requests.patch(url, json=payload, headers=self.get_auth_headers())
        r.raise_for_status()

        return len(payload['summary'])

    def get_project_slug(self):
        try:
            return self.get_settings_data()['slug']
        except KeyError:
            settings_path = os.path.abspath(self.get_settings_path())
            raise KeyError(
                'Couldn\'t find `slug` in your project-level config. '
                'Make sure it exists in {0}.'.format(settings_path))

    def get_summary_path(self):
        return os.path.join(
            self.get_project_path(), 'publish', 'distro_summary.md')

    def read_summary_content(self):
        with open(self.get_summary_path(), 'r') as summary_file:
            return summary_file.read()
