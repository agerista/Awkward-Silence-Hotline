from twilio.rest import Client
import os

AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
CALLER_ID = os.environ.get("TWILIO_CALLER_ID")


def eval_phone(phone_raw):

    phone_digits = []
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    for char in phone_raw:
        if char in numbers:
            phone_digits.append(char)
    if phone_digits[0] != 1:
        phone_digits.insert(0, "1")

    if len(phone_digits) == 11:
        phone_digits.insert(0, "+")
        recepient_phone = phone_digits.join()
        response = send_sms_message(recepient_phone)
    else:
        response = "not a valid phone number.  try again!"

    return response


def send_sms_message(recepient_phone):

    sms_string = get_message()
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        to=recepient_phone,
        from_=CALLER_ID,
        body=sms_string,
        media_url="http://www.nicknotas.com/wp-content/uploads/2012/08/Troy_and_LeVar_Burton.jpg",
    )

    return """confirmed!  sent '%s' to %s """ % (sms_string, recepient_phone)


def get_message():
    """TODO  build dynamic message generation here
    """
    return "     .   .  <crickets>    .    .   :/     .    erm...     ......."
