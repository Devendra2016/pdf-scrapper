import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

# Define the file path for saving PDFs
file_path = "downloaded_python_pdfs"

# Ensure the directory exists and has proper permissions
if not os.path.exists(file_path):
    try:
        os.makedirs(file_path, exist_ok=True)
        print(f"Directory '{file_path}' created successfully.")
    except PermissionError:
        print(f"Permission denied: Unable to create directory '{file_path}'. Please check permissions.")
        exit()

# URL of the page containing PDF links
url = input('Enter URL:')

# Send a GET request to fetch the page content
response = requests.get(url)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# List to hold all PDF links
pdf_links = []

# Loop through all the <a> tags and extract PDF links
for link in soup.find_all('a'):
    href = link.get('href')
    
    # Ensure the href exists and ends with '.pdf' (valid PDF link)
    if href and href.endswith('.pdf'):
        pdf_url = url + href
        pdf_links.append(pdf_url)

# Download and save each PDF file
for pdf_url in pdf_links:
    try:
        # Send a GET request to download the PDF
        pdf_response = requests.get(pdf_url)
        
        # Decode the URL-encoded file name
        pdf_name = urllib.parse.unquote(pdf_url.split("/")[-1])
        
        # Replace URL-encoded characters with desired formatting (optional)
        pdf_name = pdf_name.replace('%28', '(').replace('%29', ')').replace('%20', ' ').replace('%2C', ',')
        
        # Save the PDF file to the specified directory
        with open(f'{file_path}/{pdf_name}', 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)
        
        # Print download status
        print(f"Downloaded: {pdf_name}")
    
    except PermissionError:
        print(f"Permission denied while downloading {pdf_url}. Please check directory permissions.")
    except Exception as e:
        print(f"Failed to download {pdf_url}. Error: {e}")

# Print final completion message
print("Download completed.")
