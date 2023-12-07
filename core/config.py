from dotenv import load_dotenv
from os import getenv
load_dotenv()

TOKEN = getenv("TOKEN")
ADMIN_ID = getenv("ADMIN_ID")

URL= getenv("URL")
DOMAIN= getenv("DOMAIN")

HEADERS= {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.1.1215 Yowser/2.5 Safari/537.36"
}

