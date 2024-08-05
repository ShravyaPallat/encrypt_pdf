import pikepdf
import maskpass
try:
    pdf = input("Enter the address of pdf: ")
    new_name = input("Enter the name of the new pdf: ")
    user_password = maskpass.askpass(prompt="Enter the user password for the pdf: ", mask="*")
    owner_password = maskpass.askpass(prompt="Enter the owner password for the pdf: ", mask="*")

    # Open the existing PDF
    old_pdf = pikepdf.Pdf.open(pdf)

    # Define permissions
    permissions = pikepdf.Permissions(extract=False)

    # Save the new PDF with encryption and specified permissions
    old_pdf.save(new_name+".pdf", encryption=pikepdf.Encryption(user=user_password, owner=owner_password, allow=permissions))

    print("PDF saved and encrypted successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
