# from __future__ import print_function
import base64
from email.message import EmailMessage
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

# setting the permissions to edit drafts
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

# function where I create draft
def create_draft(service, user_id, message_body):
    try:
        draft = service.users().drafts().create(userId=user_id, body=message_body).execute()
        return draft
    except HttpError as error:
        print(f'An error occurred: {error}')
        return error

# main function where I create draft
def main(emailAddress, subject, myMessage):

# token.json access
    flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', SCOPES)
    creds = flow.run_local_server(port=0)

# Make the API request
    message = EmailMessage()
    message["To"] = emailAddress
    message["From"] = "me"
    message["Subject"] = subject
    message.set_content(myMessage)

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    service = build("gmail", "v1", credentials=creds)
    create_message = {"message": {"raw": encoded_message}}

    try:
        create_draft(service, "me", create_message)
        print("Draft sended")
    except Exception as e:
        print(f"Error occured: {e}")


if __name__ == '__main__':
    input("Please, input real email address")
    emailAddress = input("Input your email: ")
    subject = input("Input your subject: ")
    myMessage = input("Input your message: ")
    main(emailAddress, subject, myMessage)