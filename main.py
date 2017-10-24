import yaml
import csv

from handlers.twillio import TwillioHandler#, Sendgrid

with open('config.yml', 'r') as config_file:
    config = yaml.load(config_file)

with open(config['file'], 'r') as csv_file:
    for data in csv.DictReader(csv_file):
        # if config['sendgrid']['enabled']:
        #     Sendgrid(config['sendgrid']).handle(data)
        if config['twillio']['enabled']:
            TwillioHandler(config['twillio']).handle(data)