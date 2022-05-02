# link : https://stackoverflow.com/questions/20956424/how-do-i-generate-and-open-an-outlook-email-with-python-but-do-not-send
# This mail generate draft :-> using mail.save() method. 

def Emailer(text, subject, recipient):
    import win32com.client as win32

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.HtmlBody = text
    mail.save()

text = "<h1>Zoke!</h1>"   #You can pass HTML code here
Emailer(text,'lets see','Saurabh.Patil@gmail.com')

# try : mail.Display(True)
