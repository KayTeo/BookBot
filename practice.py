
from bs4 import BeautifulSoup as bs
import requests

URL = "https://venus.wis.ntu.edu.sg/PortalServices/ServiceListModule/LaunchService.aspx?type=1&launchSvc=https%3A%2F%2Fsso%2Ewis%2Entu%2Eedu%2Esg%2Fwebexe88%2Fowa%2Fsso%5Fredirect%2Easp%3Ft%3D1%26app%3Dhttps%3A%2F%2Fwis%2Entu%2Eedu%2Esg%2Fpls%2Fwebexe88%2Ffb%5Fstudent%2Emain%5Fall"
HEADERS = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

s = requests.session()


