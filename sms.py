from twilio.rest import Client


def send_sms(message, recipient):
    account_sid = 'AC92c272072cced50fffd18799fb511dae'
    auth_token = '********************************'

    client = Client(account_sid, auth_token)

    #message to be sent
    message_text = message

    #reciever s phone number
    recipient_number = recipient

    message = client.messages.create(
        body = message_text,
        from_= '+12296963923',
        to = recipient_number
    )

    #affirmation
    print('sms sent')

