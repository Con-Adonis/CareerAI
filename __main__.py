import os
import sys
from src.scraping.scraper import driverSetup
import src.user.welcome as welcome

def main():
    driverSetup()
    print("Web driver setup complete.")
    welcome.main()

if __name__ == "__main__":
    main()