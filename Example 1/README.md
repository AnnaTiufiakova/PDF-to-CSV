# Extract Data from PDF to CSV

## 1 Navigate to your local folder
Open a terminal and navigate to your folder:

```
cd /path/to/your/local-folder
```

## 2 Install required libraries 
Install `pdfplumber` and `pandas` for extracting text from PDFs:

```
pip install pdfplumber pandas
```

## 3 Load required files
Load the PDF file and the python script in your local directory. 

## 4 Specify source file path
Before running the script, update the pdf_path variable in the code:

```
pdf_path = "//path//to//bank_statement_1.pdf"  # Change this to your PDF file path
```

## 5 Run the script
Save the changes and run the script:

```
python extract_pdf.py
```

## 6 View the Extracted CSV
The extracted data will be saved in extracted_data.csv and can be opened in Excel or any data tool. By default, the file is saved in the same folder where the script is executed.