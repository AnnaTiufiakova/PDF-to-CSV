import pdfplumber
import pandas as pd


def extract_transactions(pdf_path, output_csv):
    transactions = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split("\n")
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 6:  # Ensure the line has enough elements
                        try:
                            dia, mes = (
                                parts[0],
                                parts[1],
                            )  # First two elements are dia and mes
                            if (
                                dia.isdigit() and mes.isdigit()
                            ):  # Validate date format
                                officina = parts[2] 
                                descripcion = " ".join(
                                    parts[3:-5]
                                ) 
                                doc = parts[-5] 
                                debito = " ".join(
                                    parts[-4:-2]
                                ).replace("$","").replace(",","")  
                                credito = " ".join(
                                    parts[-2:]
                                ).replace("$","").replace(",","")  

                                transactions.append(
                                    [
                                        dia,
                                        mes,
                                        officina,
                                        descripcion,
                                        doc,
                                        debito,
                                        credito,
                                    ]
                                )
                        except Exception:
                            continue

    # Convert extracted data into a DataFrame
    columns = ["Dia", "Mes", "Officina", "Descripcion", "Doc", "Debito", "Credito"]
    df = pd.DataFrame(transactions, columns=columns)

    # Save the extracted transactions to a CSV file
    df.to_csv(output_csv, index=False)
    print(f"Transactions extracted and saved to {output_csv}")


# Example path and output path
pdf_path = "path//to//bank_statement_1.pdf"  # Change this to your PDF file path
output_csv = "extracted_transactions.csv"
extract_transactions(pdf_path, output_csv)



