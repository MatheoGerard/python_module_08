import dotenv
import os

if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")
    find: bool = dotenv.load_dotenv(".env.example")

    if find:
        print("Configuration loaded:")

        value: str | None = os.getenv("MATRIX_MODE")
        if value:
            print(f"Mode: {value}")
        else:
            print("MATRIX_MODE not find!")

        value = os.getenv("DATABASE_URL")
        if value:
            print(f"Database: {value}")
        else:
            print("DATABASE_URL not find!")

        value = os.getenv("API_KEY")
        if value:
            print(f"API Access: {value}")
        else:
            print("API_KEY not find!")

        value = os.getenv("LOG_LEVEL")
        if value:
            print(f"Log Level: {value}")
        else:
            print("LOG_LEVEL not find!")

        value = os.getenv("ZION_ENDPOINT")
        if value:
            print(f"Zion Network: {value}")
        else:
            print("ZION_ENDPOINT not find!\n")
    else:
        print(".env not find!")
