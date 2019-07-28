# -*- coding: utf-8 -*-
"""
Set up an alert when job opening changes at delta.com.
I have removed all the actual URLs since I don't know if its ok to put everything out there
Depending on the website, it may require different post parameter
and values. Mine requires a job id and usersession id
TODO: Add alert when the value changes and send email to me
Author: Yanchun Stanley
"""
import requests
from bs4 import BeautifulSoup
import time
import smtplib


# Its nice to track the times this has been looping
counter = 0
# It is true by default
while True:
    # Landing page
    url = "https://delta.greatjob.net/jobs/EntryServlet"
    # Browsers
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    # Create a session. Download the page
    s = requests.Session()
    
    response = s.get(url, headers=headers, timeout=5)

    soup = BeautifulSoup(response.text, "lxml")
    
    # You don't need a dictionary for it if it's just one thing. But I like it its more organized and reaable. 
    job_to_browse = {
            "job":<actual value>,
            "PSUID":""
            } 
    
    #strip out the line that contains the value I am looking for
    psuid_line = str(soup.find('div', id = 'layoutDiv2').find('input',type = 'hidden'))
    
    # Need the value after the PSUID
    if psuid_line.find("PSUID") > 0:

        lst = psuid_line.split()
        temp= lst[len(lst)-1].split('"')
        psuid = temp[1]
        #print (str(psuid))
        
    job_to_browse['PSUID'] = psuid
    
    print (job_to_browse)
    
    # The actual URL I will scrape for certain value change
    job_url = '<actual url>'% psuid    
    print (job_url)
    
    job_response = s.get(job_url, headers=headers, timeout=5)
    #print (job_response.text)
    
    soup_job = BeautifulSoup(job_response.text, 'lxml')
       
    # Put your own search value in the quote in the if condition below
    if (str(soup_job).find("No Jobs Found")) > 0:
        print ("Counter: %s"%counter)
        print ("No Jobs Found. :/ continue waiting for 8 hours (for testing purpose set to 1 minute for now)....")
        # wait for 8 hours then loop again
        #time.sleep(28800)
        time.sleep(60)
        counter += 1
        continue
    else:
        print ("Found new jobs! Search is over!")
        break  



