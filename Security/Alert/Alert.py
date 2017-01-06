from twilio.rest import TwilioRestClient


class Alert:
    def __init__(self, account, token, to_number, from_number):
        self.account = account
        self.token = token
        self.to_number = to_number
        self.from_number = from_number
        self.client = TwilioRestClient(self.account, self.token)

    def send_message(self, message):
        self.client.messages.create(to="+{0}".format(self.to_number), from_="+{0}".format(self.from_number),
                                    body="{0}".format(message))
