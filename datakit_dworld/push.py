# -*- coding: utf-8 -*-
import glob
import os

from cliff.command import Command
from datakit import CommandHelpers
import requests

from datakit_dworld.dworld_mixin import DworldMixin


class Push(DworldMixin, CommandHelpers, Command):
    "Upload data files to data.world"

    def get_parser(self, prog_name):
        parser = super(Push, self).get_parser(prog_name)
        parser.add_argument(
            '-s',
            '--source-dir',
            default=os.path.join('data', 'public'),
            help='Directory of files to upload (default: data/public)'
        )
        return parser

    def take_action(self, parsed_args):
        dataset_id = '{0}/{1}'.format(
            self.configs['username'], self.get_project_slug())

        data_public_dir = os.path.join(os.getcwd(), parsed_args.source_dir)
        file_paths = glob.glob(os.path.join(data_public_dir, '**'))

        if not file_paths:
            self.log.info((
                'No files found to upload in {0}. You might want to specify '
                'an alternate directory with --source-dir.'
            ).format(parsed_args.source_dir))
            return

        self.log.info((
           'Attempting to upload {0} files to dataset {1} on data.world'
        ).format(len(file_paths), dataset_id))

        for path in file_paths:
            self.upload_file(path, dataset_id)

        self.log.info('Done')

    def get_mime_type(self, path):
        extension = os.path.splitext(path)[-1]

        if extension == '.csv':
            return 'text/csv'

        if extension == '.xls':
            return (
                'application/' +
                'vnd.openxmlformats-officedocument.spreadsheetml.sheet')

        if extension == '.xlsx':
            return 'application/vnd.ms-excel'

        return 'application/octet-stream'

    def get_project_slug(self):
        return self.get_settings_data()['slug']

    def upload_file(self, path, dataset_id):
        url = 'https://api.data.world/v0/uploads/{0}/files/{1}'.format(
            dataset_id, os.path.basename(path))
        headers = {
            'Authorization': 'Bearer {0}'.format(self.configs['api_token']),
            'Content-Type': self.get_mime_type(path),
        }

        with open(path, 'rb') as input_file:
            r = requests.put(url, data=input_file, headers=headers)

        r.raise_for_status()

        self.log.debug('Uploaded {0} to {1}'.format(
            os.path.basename(path), dataset_id))
