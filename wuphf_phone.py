import os
from twilio.rest import Client


def wuphf_phone(msg):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml='<Response><Say>{}</Say></Response>'.format(msg),
        to='+971585310804',
        from_='+19032284789'
    )

    print(call.sid)
    print("A Call was Made")

wuphf_phone('epic')