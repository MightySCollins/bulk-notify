from twilio.rest import Client

from handlers.base import BaseHandler


class TwillioHandler(BaseHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = Client(self.config['sid'], self.config['token'])

    def handle(self, data):
        assert 'number' in data
        message = self.client.messages.create(
            to=data['number'],
            body=self.handle_template('sms', data),
            from_=self.config['from']
        )
        print("Sent message {sid} to {number}".format(sid=message.sid, number=data['number']))
        # print(f"Sent message {message.sid} to {data['number']}")