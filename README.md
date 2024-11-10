PdfScrapper
This Python script crawls a website for PDF links and downloads them to your local machine.

Prerequisites
Make sure you have the following installed:

Python 3.x
Git
Setting Up the Repository
1. Clone the repository:
Open your terminal (or Git Bash) and run the following command to clone the repository to your local machine:

bash
Copy code
git clone https://github.com/Devendra2016/pdf-scrapper.git
2. Navigate into the project directory:
Change into the directory of the cloned repository:

bash
Copy code
cd pdf-scrapper
Running the Script
3. Run the PdfScrapper script:
To run the script, use the following command:

bash
Copy code
python PdfScrapper.py
This will crawl the specified website, find PDF links, and download them to a folder named downloaded_python_pdfs in your project directory.

Folder Structure
The downloaded PDFs will be saved in a folder named downloaded_python_pdfs inside the project directory.

plaintext
Copy code
pdf-scrapper/
│
├── PdfScrapper.py      # The script that scrapes and downloads PDFs
├── downloaded_python_pdfs/   # Folder where PDFs are saved
└── README.md          # This file
Troubleshooting
Permission errors: If you encounter a PermissionError when trying to save PDFs, ensure you have the correct permissions for the folder where you are saving the PDFs.
