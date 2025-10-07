from dotenv import load_dotenv
from extract import extract
from transform import transform
from load import load

def configure():
    load_dotenv()

def main():
    configure()

    all_data = extract("Kraków")
    transformed_data = transform(all_data)
    load(transformed_data, "testFile.csv")

main()