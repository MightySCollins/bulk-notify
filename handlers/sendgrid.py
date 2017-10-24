import sendgrid
from sendgrid.helpers.mail import *

from handlers.base import BaseHandler


class Sendgrid(BaseHandler):
    def handle(self, data):
        if 'email' not in data:
            raise Exception('An email address is required')
        from_email = Email(self.config['from']['email'], self.config['from']['name'])
        to = Email(data['email'], self.build_name(data))

        mail = Mail(from_email=from_email, subject=self.config['subject'], to_email=to)
        mail.add_content("text/plain", self.handle_template('plain', data))
        mail.add_content("text/html", self.handle_template('html', data))
        sg = sendgrid.SendGridAPIClient(
            apikey=self.config['api_key'])
        response = sg.client.mail.send.post(request_body=mail.get())
        if response.status_code == 200:
            pass

    def build_name(self, data):
        if data['first_name'] and data['last_name']:
            return f"{data['first_name']} {data['last_name']}"
        return None