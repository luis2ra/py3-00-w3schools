import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='no-reply@blapp.pe',
    to_emails='luis2ra@gmail.com')

message.dynamic_template_data = {
    'Subject': 'Gracias2 por registrarte a BlappNews',
    'names': 'Luisito2'
}

message.template_id = 'd-0979085e9593452da3a2b8e9a219cad0'

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