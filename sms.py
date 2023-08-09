from twilio.rest import Client

message_text = ''
recipient_number = ''


def send_sms():
    account_sid = 'AC92c272072cced50fffd18799fb511dae'
    auth_token = 'a7e0f64dc655e84c1baa5cb20cb9af05'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = message_text,
        from_= '+12296963923',
        to = recipient_number
    )

    print('sms sent')


