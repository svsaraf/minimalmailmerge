import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

def main():
    """Shows basic usage of the Gmail API.
    Creates a Gmail draft with "Hello World".
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Create a draft message
    message = MIMEText('Hello World')
    message['to'] = 'recipient@example.com'  # Replace with actual recipient
    message['subject'] = 'Test Draft'
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

if __name__ == '__main__':
    main()