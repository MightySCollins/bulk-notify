import re
import os


class BaseHandler:
    def __init__(self, config):
        self.config = config

    def handle(self, data):
        raise NotImplementedError('No handle method found')

    def handle_template(self, type, data):
        return self.parse_template(data, self.read_template(type))

    def read_template(self, file):
        filename = os.path.join('templates', self.config['templates'][file])
        with open(filename, 'r') as template:
            return template.read()

    def parse_template(self, data, template):
        for tag in re.findall('{{(.*?)}}', template):
            assert tag in data
            # if tag not in data:
            #     raise Exception(f'Template tag {tag} is not in CSV')
            template = template.replace('{{%s}}'% tag, data[tag])
        return template
