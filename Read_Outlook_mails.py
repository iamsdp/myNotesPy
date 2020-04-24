import win32com.client

"""
We read it mails from old->New when we use GetFirst() and to get previous mail we use GetNext(). 
We can read mail New->old by using GetLast(). We get latest mail first here. To get next mail, we use GetPrevious().
"""

def extract(count):
    """Get emails from outlook."""
    items = []
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6) # "6" refers to the inbox - return "inbox"

    """
    # Navigate to subFolder
    your_folder = outlook.Folders['XXXXXXX'].Folders['Inbox'].Folders['PQR']
    # Here 'xxxxxx' mention here -> "Default name in tree of folders in mail box". In may case it was my org mail address.
    msgs = your_folder.Items
    ms = msgs.GetFirst()
    print(getattr(ms, "Subject", "<UNKNOWN>"))
    """

    messages = inbox.Items
    # print(type(messages)) Its a class
    
    message = messages.GetFirst()
    #GetFirst returns the oldest mail in Inbox & GetLast() return latest mail ....
    # print(type(message))

    i = 0
    while message:
        try:
            msg = dict()
            msg["Subject"] = getattr(message, "Subject", "<UNKNOWN>")
            msg["SentOn"] = getattr(message, "SentOn", "<UNKNOWN>")
            msg["EntryID"] = getattr(message, "EntryID", "<UNKNOWN>")
            msg["Sender"] = getattr(message, "Sender", "<UNKNOWN>")
            msg["Size"] = getattr(message, "Size", "<UNKNOWN>")
            msg["Body"] = getattr(message, "Body", "<UNKNOWN>")
            items.append(msg)

        except Exception as ex:
            print("Error processing mail", ex)
        i += 1
        if i < count:
            message = messages.GetNext()
            # We can use GetPrevious() when we use GetLast() 
        else:
            return items


    return items


def show_message(items):
    """Show the messages."""
    items.sort(key=lambda tup: tup["SentOn"])
    # for i in items:
        # print(i["SentOn"], i["Subject"])



def main():
    """Fetch and display top message."""
    items = extract(6)
    # sending "6" here because, we want 6 mails to be read.
    show_message(items)


if __name__ == "__main__":
    main()
