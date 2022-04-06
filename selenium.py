
from __future__ import print_function
import datetime
from datetime import date
from email.message import Message
import time
from tkinter import E
from webbrowser import Chrome
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.options import Options

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import glob
import os
# import config_remedy_email
import pymsteams

import win32com.client
import datetime as dt
# from xlsx2html import xlsx2html
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
# import config_outlook_email
# import xlrd
import time
import sys
from datetime import datetime, timedelta
import pandas as pd
# import numpy as np
from IPython.core.display import display, HTML
import pandas

# pass_str = os.environ.get("remedy_pass_str")
# pass_str = config_remedy_email.remedy_pass_str
# email_body = config_remedy_email.email_body
# email_from = config_remedy_email.email_from
# email_to = config_remedy_email.email_to
# smtp_server = config_remedy_email.smtp_server
# port_number = config_remedy_email.port_number
# remedy_email_id=config_remedy_email.remedy_email_id
# no_of_iterations=config_remedy_email.no_of_iterations
# time_interval=config_remedy_email.time_interval


# email_body = 'Hi'
# email_from = 'saurabh.patil@teradata.com'
# smtp_server = config_remedy_email.smtp_server
# port_number = config_remedy_email.port_number
no_of_iterations = 30
time_interval = 1900

email_to = 'UE230007@Teradata.com'
pass_str = 'Python(0)'
unilever_id = 'patil.saurabh@unilever.com'
email_cc = 'Malwadkar, Aniket <Aniket.Malwadkar@Teradata.com> ; Saoji, Saurabh <Saurabh.Saoji@Teradata.com>'
# email_cc = ''
email_subject = 'ServiceNow-Incident Report'


def is_alert_present():
    try:
        WebDriverWait(chrome_options, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = chrome_options.switch_to.alert
        alert.accept()
        # print("alert accepted")
    except TimeoutException:
        print("no alert")


# opt = Options()
# opt.add_experimental_option("debuggerAddress","localhost:8989")
# driver = webdriver.Chrome(executable_path= "C:\\Users\\sp250123\\AppData\\Local\\Programs\\Python\\Python39\\SnowPy\\chromedriver.exe", chrome_options=opt)
# chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Users\sp250123\OneDrive - Teradata\Documents\ChromeFilesDebugLogs"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.set_capability('unhandledPromptBehavior', 'accept')
# usernameStr = saikrishna.kandimalla@unilever.com
# passwordStr = ""
# usernameStr = unilever_id
# passwordStr = pass_str

print(unilever_id)
chrome_options = webdriver.Chrome(chrome_options=chrome_options)
chrome_options.get('https://unilever.service-now.com')
print("Page Title is : %s" % chrome_options.title)
print("Waiting for 20 Sec...")
time.sleep(20)

print("\nEntering Username...")
username = chrome_options.find_element(By.ID,"i0116")
# print("Waiting for 2 Sec...")
# time.sleep(2)
username.send_keys(unilever_id)
print("Waiting for 2 Sec...")
time.sleep(2)
chrome_options.find_element(By.ID,"idSIButton9").click()
print("Waiting for 3 Sec...")
time.sleep(3)

# password = chrome_options.find_element(By.ID,"passwordInput")
print("\nEntering Password...")
password = chrome_options.find_element(By.ID,"i0118")
password.send_keys(pass_str)
print("Waiting for 2 Sec...")
time.sleep(2)
chrome_options.find_element(By.ID,"idSIButton9").click()
status_val = [is_alert_present() for c in range(0,5)]

# print("Waiting for 5 Sec...")
# time.sleep(5)
print("\nComplete login by MFA/OTP/CALL in 20 sec....")



# chrome_options.find_element_by_id("authenticateButton").click()
# chrome_options.find_element_by_id("idSubmit_SAOTCC_Continue").click()

# This will click on first Mechanism whatever is on Screen !!!
chrome_options.find_element(By.XPATH,"//*[@id='idDiv_SAOTCS_Proofs']/div[1]/div").click()

status_val = [is_alert_present() for c in range(0,5)]
# print("Waiting for 20 Seconds...")
time.sleep(20)

# chrome_options.find_element(By.XPATH,"//*[@id='idSubmit_SAOTCC_Continue']").click()
# time.sleep(10)
# chrome_options.find_element_by_id("favorites_tab").click()
# status_val = [is_alert_present() for c in range(0,5)]
# time.sleep(10)
# print("ddddd")
# chrome_options.find_element_by_xpath("//*[@id='favorite-collapse-c3e81d461be9ec1039bf975e0d4bcbe7']/li[5]/a/div[2]/span").click()


print('Pressing Button - "Favorites"')
chrome_options.find_element(By.XPATH,"//*[@id='favorites_tab']").click()
print("Waiting for 5 Seconds...")
time.sleep(5)


print("\n\nWhile loop is starting...!")

while True:

    srtHandle = chrome_options.window_handles
    chrome_options.switch_to.window(chrome_options.window_handles[-1])

    print("\nClicking on - Filter Navigator.....")
    chrome_options.find_element(By.XPATH,"/html/body/div[5]/div/div/nav").click()

    time.sleep(3)
    print("\nClicking on - 'Reports - View / Run'.....")
    # chrome_options.find_element(By.XPATH,"//*[@id='gsft_nav']/div/magellan-favorites-list/ul/li/div/div[1]/a/div[2]/span").click()
    chrome_options.find_element(By.LINK_TEXT,"Reports - View / Run").click()

    status_val = [is_alert_present() for c in range(0,5)]
    time.sleep(2)
    
    # chrome_options.switch_to_frame("gsft_main")
    print("\nSwitching to Frame....")
    chrome_options.switch_to.frame("gsft_main")

    print("\nClicking on 'My Reports'....")
    chrome_options.find_element(By.XPATH,"//*[@id='li_my_reports_tab']/span").click()
    status_val = [is_alert_present() for c in range(0,5)]
    # print("Waiting for 5 Seconds...")
    # time.sleep(5)

    # Report Wrapper 
    # chrome_options.find_element(By.XPATH,"//*[@id='ng-app']/div/div[2]").click()
    # status_val = [is_alert_present() for c in range(0,5)]
    # print("Waiting for 5 Seconds...")
    # time.sleep(5)
    
    
    print("\nClicking on Current_Month_incidents button .... !!!")
    # chrome_options.find_element(By.XPATH,"//*[@id='report-list']/tbody/tr[1]/td[4]/a").click()
    chrome_options.find_element(By.LINK_TEXT,"Current_Month_incidents").click()
    status_val = [is_alert_present() for c in range(0,5)]
    # print("Waiting for 5 Seconds...")
    # time.sleep(5)
    
    # chrome_options.find_element_by_xpath("//*[@id='run-report']").click()
    # status_val = [is_alert_present() for c in range(0, 5)]
    # time.sleep(10)
    
    print("\n\nChecking if any incident is in New/Open/On-hold/In-Progress state..!!!")

    table_value = "/html/body/div[2]/div[1]/div/article/div[5]/section/div/div[1]/div[2]/span/div/div[2]/table/tbody/tr/td/div/table/tbody/tr"
    
    # table_value="// *[ @class ='data_list_table list_table table table-hover  list_header_search_disabled'] / tbody / tr[1] / td[1]"
    # time.sleep(10)
    # print("\nTable_value -->",table_value)
    values_info = chrome_options.find_element(By.XPATH,table_value).text
    # values_info = chrome_options.find_element_by_xpath(table_value).text
    # print("\nTable Values info-->", values_info)
    

    
    if values_info == "No records to display":

        print("\nNo Open/On Hold incidents in our Queue to display")

        # Send an Email to Team
        outlook = win32com.client.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = email_to
        mail.CC = email_cc
        mail.Subject = email_subject
        mail.HTMLBody = """<html>
                    <head></head>
                    <body>
                    <p>Hi All,<br>
                    <br>
                    <h5>No New/Open/On Hold incidents in our Queue to display.</h5>
                    <br><br>
                    <table border="1">
                <caption>Incidents' Count</caption>
                <tr>
                    <th>State</th>
                    <th>Count</th>
                </tr>
                <tr>
                    <td>New</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>In Progress</td>
                    <td>0</td>
                </tr>
                <tr>
                    <td>On Hold</td>
                    <td>0</td>
                </tr>
                </table>

                    <br>
                    <p>Regards,<br>
                        Teradata Platform Team<br>
                        Teradata @ Unilever<br>
                        Team On-Cal: +91 744-741-3560<br>
                        Team Email: UE230007@Teradata.com<br>
                    </p>
                    </body>
                </html>"""
        mail.Send()

        print("\nEmail Sent to the team.")
        
        ### Send Message on Teams Channel -------------------------
        # myTeamsMessage = pymsteams.connectorcard("https://teradata.webhook.office.com/webhookb2/a8ab3789-b485-47fb-9d6b-25ff7190ce81@9151cbaa-fc6b-4f48-89bb-8c4a71982138/IncomingWebhook/2182cc29be9a43b8b1cf73883d891430/17165453-05ba-4551-ac1b-9f1351e366a6")
        # empty_string="No Open/On Hold incidents in our Queue to display"
        # # Default message
        # myTeamsMessage.text(empty_string)
        # myTeamsMessage.send()

        # print("\nNext sync in 10 Min...")
        # time.sleep(600)
        # chrome_options.find_element(By.XPATH,"//*[@id='run-report']").click()
        # status_val = [is_alert_present() for c in range(0, 5)]

        # print("\nNext sync in 10 Min...")
        # time.sleep(600)
        # chrome_options.find_element(By.XPATH,"//*[@id='run-report']").click()
        # status_val = [is_alert_present() for c in range(0, 5)]

        # print("\nNext sync in 10 Min...")
        # time.sleep(600)

        print("\nwill check after 25 Minutes ... ")
        time.sleep(1500)

    else:

        print("Incidents found in our queue ....")

        print("\n\nRunning the report ....")
        chrome_options.find_element(By.XPATH,"//*[@id='run-report']").click()
        status_val = [is_alert_present() for c in range(0, 5)]
        # print("Waiting for 10 Seconds...")
        # time.sleep(10)
        
        print("Clicking on report-container")
        chrome_options.find_element(By.XPATH,"//*[@id='report-container']").click()
        status_val = [is_alert_present() for c in range(0, 5)]
        # print("Waiting for 10 Seconds...")
        # time.sleep(10)

        print("Clicking on report-container-builder")
        chrome_options.find_element(By.XPATH,"//*[@id='report-container-builder']").click()
        # print("Waiting for 10 Seconds...")
        # time.sleep(10)


        all_New = chrome_options.find_elements(By.XPATH,"//*[@class='vt' and contains(text(),'New')]")
        # print(len(all_New))

        all_In_Progress = chrome_options.find_elements(By.XPATH,"//*[@class='vt' and contains(text(),'In Progress')]")
        # print(len(all_In_Progress))

        all_On_Hold = chrome_options.find_elements(By.XPATH,"//*[@class='vt' and contains(text(),'On Hold')]")
        # print(len(all_On_Hold))
 
        all_Resolved = chrome_options.find_elements(By.XPATH,"//*[@class='vt' and contains(text(),'Resolved')]")
        # print(len(all_Resolved))

        all_Closed = chrome_options.find_elements(By.XPATH,"//*[@class='vt' and contains(text(),'Closed')]")
        # print(len(all_Closed))
        
        # all_spans = chrome_options.find_elements_by_xpath("//span[@class='list_decoration_cell col-control col-small col-center ']")
        # for span in all_spans:
        #     print(span.text)
        # print("gggg6")

        a = len(all_On_Hold)
        b = len(all_Closed)
        c = len(all_In_Progress)
        d = len(all_Resolved)
        
        cnt_new = len(all_New)
        cnt_in_progress = c
        cnt_on_hold = a

        print("\nCurrent incident Count:")
        print("New: ", cnt_new)
        print("On Hold: ",a)
        print("Closed ",b)
        print("In Progress: ",c)
        print("Resolved: ",d)

        total = a + b + c + d

        row_count = len(chrome_options.find_elements(By.XPATH,"/html/body/div[2]/div[1]/div/article/div[5]/section/div/div[1]/div[2]/span/div/div[2]/table/tbody/tr/td/div/table/tbody/tr"))
        col_count = len(chrome_options.find_elements(By.XPATH,"/html/body/div[2]/div[1]/div/article/div[5]/section/div/div[1]/div[2]/span/div/div[2]/table/tbody/tr/td/div/table/tbody/tr[1]/td"))

        # print("Num of Row ",row_count)
        # print("Num of colmn ",col_count)

        first_part = "/html/body/div[2]/div[1]/div/article/div[5]/section/div/div[1]/div[2]/span/div/div[2]/table/tbody/tr/td/div/table/tbody/tr["
        second_part = "]/td["
        third_part = "]"
        n = 1
        m = 3


        data_list_final = []
        for n in range(1, row_count + 1):
            data_list = []
            for m in range(1, 13):
                final_part = first_part + str(n) + second_part + str(m) + third_part
                table_data = chrome_options.find_element(By.XPATH,final_part).text
                data_list.append(table_data)

            aa = [str(x) for x in data_list]

            data_list_final.append(aa)


        d = ['aa', 'bb', 'Number', 'Opened', 'Short description', 'Caller', 'Priority', 'State', 'Assignment group','Assigned to', 'Updated', 'Updated by']
        data_list_final.insert(0, d)


        i = 1
        for row in data_list_final:
            row.append(i)
            i += 1
        # print(data_list_final)

        if total != 0:
            dd = []
            dd.append(
                """<TABLE BORDER="5"  background-color: gold  class="table table-bordered" style="border-color:white   WIDTH="50%"   CELLPADDING="4" CELLSPACING="3" >""")

            for [a, b, c, d, e, f, g, h, i, j, k, l, m] in data_list_final:

                # print(a,b,c,d)
                if str(m) == '1':
                    m = "S.No"
                   # print(c)
                else:
                    m = m - 1
                
                dd.append("<tr>")
                # dd.append ("<td>" + str(a) + ":" + str(b) + "</td>")
                # print(type(b))
                # print(b)
                if m == "S.No":
                    dd.append("""<td style="color:black"  width="3%" bgcolor=#00CC88 style="text-align:center" > """ + str(m) + "</td>")
                    dd.append("""<td style="color:black"  width="10%" bgcolor=#00CC88 style="text-align:center">""" + str(c) + "</td>")
                    dd.append("""<td style="color:black"  width="20%" bgcolor=#00CC88 style="text-align:left">""" + str(d) + "</td>")
                    dd.append("""<td style="color:black"   width="35%"bgcolor=#00CC88 style="text-align:center" >""" + str(e) + "</td>")
                    dd.append("""<td style="color:black"  width="7%" bgcolor=#00CC88 style="text-align:center"  >""" + str(f) + "</td>")
                    dd.append("""<td style="color:black"  width="10%" bgcolor=#00CC88 style="text-align:center"  >""" + str(g) + "</td>")
                    dd.append("""<td style="color:black"  width="15%" bgcolor=#00CC88 style="text-align:center"  >""" + str(h) + "</td>")
                    dd.append("""<td style="color:black"  width="30%" bgcolor=#00CC88 style="text-align:center"  >""" + str(i) + "</td>")
                    dd.append("""<td style="color:black"  width="30%" bgcolor=#00CC88 style="text-align:center"  >""" + str(j) + "</td>")
                    dd.append("""<td style="color:black"  width="30%" bgcolor=#00CC88 style="text-align:center"  >""" + str(k) + "</td>")
                    dd.append("""<td style="color:black"  width="30%" bgcolor=#00CC88 style="text-align:center"  >""" + str(l) + "</td>")
                else:
                    dd.append("""<td style="color:black"  width="3%" bgcolor=#F5EEF8 style="text-align:center" > """ + str(m) + "</td>")
                    dd.append("""<td style="color:black"  width="10%" bgcolor=#F5EEF8 style="text-align:center">""" + str(c) + "</td>")
                    dd.append("""<td style="color:black"  width="20%" bgcolor=#F5EEF8 style="text-align:left">""" + str(d) + "</td>")
                    dd.append("""<td style="color:black"   width="35%"bgcolor=#F5EEF8 style="text-align:center" >""" + str(e) + "</td>")
                    dd.append("""<td style="color:black"  width="10%" bgcolor=#F5EEF8 style="text-align:center"  >""" + str(f) + "</td>")
                    dd.append("""<td style="color:black"  width="7%" bgcolor=#F5EEF8 style="text-align:center"  >""" + str(g) + "</td>")
                    dd.append("""<td style="color:black"  width="10%" bgcolor=#F5EEF8 style="text-align:center"  >""" + str(h) + "</td>")
                    dd.append("""<td style="color:black"  width="15%" bgcolor=#F5EEF8 style="text-align:center"  >""" + str(i) + "</td>")
                    dd.append("""<td style="color:black"  width="30%" bgcolor=#F5EEF8 style="text-align:center"  >""" + str(j) + "</td>")
                    dd.append("""<td style="color:black"  width="30%" bgcolor=#F5EEF8 style="text-align:center"  >""" + str(k) + "</td>")
                    dd.append("""<td style="color:black"  width="30%" bgcolor=#F5EEF8 style="text-align:center"  >""" + str(l) + "</td>")

                dd.append("</tr>")
                # i += 1
            dd.append("</table>")
            # print(dd)
            final_table = '\n '.join(dd)

            # email_user = email_from
            # email_send = (', ').join(email_to.split(','))
            # print(str(email_user))
            # print(str(email_send))

            today = date.today()
            today_format = str(today.strftime("%d-") + today.strftime("%b-") + today.strftime("%Y"))
            
            html = """
            <html>
              <head></head>
              <body>
                <p>Hi All,<br>
                   Please find below status report of all the incidents in Teradata Platform queue for   {0[today_format]}  . </br>

                    <table border="1">
                <caption>Incidents' Count</caption>
                <tr>
                    <th>State</th>
                    <th>Count</th>
                </tr>
                <tr>
                    <td>New</td>
                    <td>{0[cnt_new]}</td>
                </tr>
                <tr>
                    <td>In Progress</td>
                    <td>{0[cnt_in_progress]}</td>
                </tr>
                <tr>
                    <td>On Hold</td>
                    <td>{0[cnt_on_hold]}</td>
                </tr>
                </table>

                </p>
              </body>
            </html>
            """.format(locals())


            blank_line = """<h4>Change Details:</h4>"""
            blank_line0 = """<h4>Incident Details:</h4>"""
            blank_line1 = """<br>"""

            # xlsx_file = open(r"C:\Users\sk186103\.PyCharmCE2019.1\config\scratches\Changes.xlsx", 'rb')
            # xlsx_file = pd.read_excel(r"C:\Users\sk186103\.PyCharmCE2019.1\config\scratches\Changes.xlsx", sheet_name=1)
            # out_file = io.StringIO()
            # xlsx2html(xlsx_file, out_file, locale='en')
            # out_file.seek(0)
            # abc = out_file.read()
            # out_stream = xlsx2html(r"C:\Users\sk186103\.PyCharmCE2019.1\config\scratches\Changes.xlsx")
            # out_stream.seek(0)
            # abc = out_stream.read()

            sign = """<html>
              <head></head>
              <body>
                <p>Regards,<br>
                   Teradata DBA - Unilever Platform Services<br>
                        DBA On-Call: +91 7447413560<br>
                        DBA Email: UE230007@Teradata.com<br>

                </p>
              </body>
            </html>"""

            html = html + blank_line0 + blank_line1 + final_table + sign

            # MS Teams Msg Module
            # URL we recieved from Webhook
            # myTeamsMessage = pymsteams.connectorcard(https://teradata.webhook.office.com/webhookb2/a8ab3789-b485-47fb-9d6b-25ff7190ce81@9151cbaa-fc6b-4f48-89bb-8c4a71982138/IncomingWebhook/93aeaf1a0fe34fe18b6a650f26104c16/17165453-05ba-4551-ac1b-9f1351e366a6)
            # myTeamsMessage = pymsteams.connectorcard("https://teradata.webhook.office.com/webhookb2/a8ab3789-b485-47fb-9d6b-25ff7190ce81@9151cbaa-fc6b-4f48-89bb-8c4a71982138/IncomingWebhook/2182cc29be9a43b8b1cf73883d891430/17165453-05ba-4551-ac1b-9f1351e366a6")
            # Default message
            # date_part = datetime.now().strftime("%Y-%m-%d %H:%M")
            # date_time_part = f"Hi All - \n  Please find below status report of all the incidents in Teradata Platform queue for {date_part}  ."
            # myTeamsMessage.text((date_time_part))
            # myTeamsMessage.send()
            # myTeamsMessage.text((final_table))
            # myTeamsMessage.send()


            # EMAIL MODULE
            outlook = win32com.client.Dispatch('outlook.application')
            mail = outlook.CreateItem(0)
            mail.To = email_to
            mail.CC = email_cc
            mail.Subject = email_subject
            mail.HTMLBody = html
            mail.Send()
            print("Email sent...Please check your Inbox !!!")


            # break_count = break_count + 1
            print("\n\nNext sync in 25 Minutes.....")
            time.sleep(1500)
