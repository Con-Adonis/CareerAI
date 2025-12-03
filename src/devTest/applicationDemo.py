import os
import time
from sentence_transformers import SentenceTransformer, util
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# sentence transformer model config
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
similarityScore = 0.85
mockApplication = os.path.abspath("mock_job_app.html")

def stringComparison(str1, str2):
    sentences = [str1, str2]
    return (model.encode(sentences, convert_to_tensor=True))

print(stringComparison("hello world", "hello world"))
