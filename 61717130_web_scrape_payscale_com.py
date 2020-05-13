
import requests
from bs4 import BeautifulSoup 
import csv
import os

# setup the default file lookup location to cwd
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


url = 'https://www.payscale.com/research/US/Job/Accounting-and-Finance'

# get the response from the url provided
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

job_data = []

with open(os.path.join(__location__,'output.csv'), 'w+') as f:
    writer = csv.writer(f)
    for jobs in soup.find_all('a', class_ = "subcats__links__item"):
        job_data.append(jobs.text)        
    writer.writerow(job_data)






