import os
from django.core.management import call_command

fixtures_dir = os.path.join(os.getcwd(), 'fixtures')

for filename in os.listdir(fixtures_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(fixtures_dir, filename)
        print(f'Loading fixture: {file_path}')
        call_command('loaddata', file_path)
