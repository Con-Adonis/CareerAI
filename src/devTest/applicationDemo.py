import os
import time
from sentence_transformers import SentenceTransformer, util
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#configuration and constants
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
similarityScore = 0.85
mockApplication = os.path.abspath("mock_job_app.html")

def stringComparison(str1, str2):
    print(f"{str1} and {str2}: {util.pytorch_cos_sim(model.encode(str1), model.encode(str2)).item()}")
    return util.pytorch_cos_sim(model.encode(str1), model.encode(str2)).item()

def runApplicationDemo():
