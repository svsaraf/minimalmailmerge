import os
import base64
import csv
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from jinja2 import Template

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

def read_template(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def read_template_vars(csv_path):
    with open(csv_path, mode='r', newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        return list(reader)  # Return all rows as a list of dictionaries

def create_draft(service, message_body, recipient_email, subject):
    # Create a draft message
    message = MIMEText(message_body)
    message['to'] = recipient_email
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    draft = {
        'message': {
            'raw': raw_message
        }
    }

    # Create the draft
    try:
        create_draft = service.users().drafts().create(userId='me', body=draft).execute()
        print(f'Draft created with ID: {create_draft["id"]}')
    except Exception as error:
        print(f'An error occurred: {error}')

def main():
    """Creates Gmail drafts using a Jinja2 template from an external file."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Read template and template variables
    template_string = read_template('template.txt')
    template_vars_list = read_template_vars('template_vars.csv')

    # Create a Jinja2 template
    template = Template(template_string)

    # Loop through each row in the CSV and create a draft
    for template_vars in template_vars_list:
        print(template_vars)
        message_body = template.render(template_vars)
        create_draft(service, message_body, template_vars['recipient_email'], template_vars['subject'])

if __name__ == '__main__':
    main()