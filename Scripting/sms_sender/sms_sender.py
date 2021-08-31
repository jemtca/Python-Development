from twilio.rest import Client

def send_sms(message):
    account_sid = '' # it can be found in the dashboard of a Twilio account
    auth_token = '' # it can be found in the dashboard of a Twilio account
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_ = '', # phone number including prefix (from, Twilio phone number)
        body = message, # text message
        to = '' # phone number including prefix (to)
    )

    print('Message sent!')

if __name__ == '__name__':
    send_sms('type_your_message_in_here') # function with one argument: message text
