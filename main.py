from validate_email_address import validate_email

emails = open("emails.txt").read().split('\n')
valid_emails = open('valid_emails.txt', 'a')

for email in emails:
    isvalid = validate_email(email, verify=True)
    if isvalid:
        valid_emails.write(email)
        valid_emails.write('\n')

valid_emails.close()