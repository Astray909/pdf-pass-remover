import pikepdf
import os

import supportingModule.progressBar as pgB

def find_ext(dir):
    files = []
    for file in os.listdir(dir):
        if file.endswith(".pdf"):
            # print(os.path.join(dir, file))
            files.append((os.path.join(dir, file),file))
    return files

def pdf_unlock(dir, pdf_pass):
    os_name = os.name
    if os_name == 'Windows':
        div_sym = "\\"
    else:
        div_sym = "/"

    all_pdf = find_ext(dir)

    isExist = os.path.exists(dir + div_sym + "unlocked")
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(dir + div_sym + "unlocked")

    pgB.printProgressBar(0, len(all_pdf), prefix =  'Unlocking Progress:', suffix = 'Complete', length = 50)
    for i in range(len(all_pdf)):
        pdf = pikepdf.open(all_pdf[i][0], password=pdf_pass)
        # print("\nProcessing...\n")
        pdf_save = all_pdf[i][1].replace(".pdf", "_unlocked.pdf")
        pdf_loc2 = dir + div_sym + "unlocked"
        pdf.save(pdf_loc2 + div_sym + pdf_save)
        # print("The password successfully removed from the PDF")
        # print("\aLocation: " + dir + div_sym + pdf_save)
        pgB.printProgressBar(i+1, len(all_pdf), prefix =  'Unlocking Progress:', suffix = 'Complete', length = 50)

if __name__ == "__main__":
    dir = input("PDF location: ")
    pdf_pass = input("PDF password: ")
    pdf_unlock(dir, pdf_pass)
