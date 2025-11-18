import os
import sys
from src.scraping.scraper import driverSetup

def main():
    driverSetup()
    print("Web driver setup complete.")

if __name__ == "__main__":
    main()