from dotenv import load_dotenv
from extract import extract

def configure():
    load_dotenv()

def main():
    configure()
    extract("Kraków")

main()