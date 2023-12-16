Hi, thanks for the answer and the opportunity to prove yourself. 
At the top of my code I usually declare imports of all the libraries I plan to use. Using APIs and libraries saves a lot of my time. I don’t need to write requests manually and create a message object and then encrypt it, libraries do this for me. Each action literally takes one line of code.

Did I use op in this code?
I didn't use OOP in this code because I don't have a class that would have encapsulated fields and methods inside.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']
With this line, I told Google what I planned to do with its code and what permissions I would need for this. I chose the lowest priority so that my application did not need to be verified by Google, but only the user’s consent to provide data was enough.

create_draft
In this method I create a draft letter. With the first parameter I indicate that it will be a letter and not a label or something else, with the second parameters I indicate the sender's email and the third and last parameter I pass the created letter which is already encoded and has information about the recipient, the subject of the letter and the text of the letter itself

def main(emailAddress, subject, myMessage):
Function take in parameters email, subject, message that I took earlier from inputs. In the first two lines this function I pass a token thanks to which I can use the API and make requests to Google.

message = EmailMessage()
message["To"] = emailAddress
message["From"] = "me"
message["Subject"] = subject
message.set_content(myMessage)

encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
In these lines I instantiate the message. Where I indicate my recipient, sender, subject of the letter and my message.

service = build("gmail", "v1", credentials=creds)
create_message = {"message": {"raw": encoded_message}}
Next, I initialize the service for letters and create a letter object, which will then be passed in the parameters of the function create_draft.

try:
    create_draft(service, "me", create_message)
    print("Draft sended")
except Exception as e:
    print(f"Error occured: {e}")
In this code, my previously created objects are passed in the parameters of the create_draft function for later sending them through the Google API. They are wrapped in try/catch order to error can be tracked. If an unexpected error occurred, I could see it in the console and my program would catch it and continue working.
