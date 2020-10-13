import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='no-reply@blapp.pe',
    to_emails='luis2ra@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    #sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    SENDGRID_API_KEY='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'
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))