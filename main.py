import pikepdf
import os

def find_ext(dir):
    files = []
    for file in os.listdir(dir):
        if file.endswith(".pdf"):
            # print(os.path.join(dir, file))
            files.append((os.path.join(dir, file),file))
    return files

def pdf_unlock(dir, pdf_pass):
    all_pdf = find_ext(dir)

    isExist = os.path.exists(dir + "\\unlocked")
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(dir + "\\unlocked")

    for one_pdf in all_pdf:
        pdf = pikepdf.open(one_pdf[0], password=pdf_pass)
        print("\nProcessing...\n")
        pdf_save = one_pdf[1].replace(".pdf", "_unlocked.pdf")
        pdf_loc2 = dir + "\\unlocked"
        pdf.save(pdf_loc2 + '\\' + pdf_save)
        print("The password successfully removed from the PDF")
        print("\aLocation: " + dir + '\\' + pdf_save)

if __name__ == "__main__":
    dir = input("PDF location: ")
    pdf_pass = input("PDF password: ")
    pdf_unlock(dir, pdf_pass)
