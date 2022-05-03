import extract_msg

p = 'C:/Users/*/Desktop/CBA Python/scheduled autosupport (BARBWDD1.localdomain) .msg'
f = r'C:/Users/*/Desktop/CBA Python/scheduled autosupport (BARBWDD1.localdomain) .msg'  # Replace with yours

msg = extract_msg.Message(f)
msg_sender = msg.sender
msg_date = msg.date
msg_subj = msg.subject
msg_message = msg.body

print('Sender: {}'.format(msg_sender))
print('Sent On: {}'.format(msg_date))
print('Subject: {}'.format(msg_subj))
print('Body: {}'.format(msg_message))
print (msg_message)
