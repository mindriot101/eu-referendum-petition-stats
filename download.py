#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import json

if __name__ == '__main__':
    s = requests.Session()
    while True:

        output_filename = 'data-{}.json'.format(int(time.time()))

        print('Downloading')
        json_data = s.get(
            'https://petition.parliament.uk/petitions/131215.json'
        ).json()
        print('Writing to file {}'.format(output_filename))
        with open(output_filename, 'w') as outfile:
            json.dump(output_filename, outfile)

        print('Sleeping')

        time.sleep(60)

