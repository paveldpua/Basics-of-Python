"""Brute-Force PDF Password Breaker."""
import os

import PyPDF2


def break_pdf_password(pdf_file, pass_dict_file):
    """Brute-Force PDF Password Breaker."""
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_file, 'rb'))
    with open(pass_dict_file, 'r') as pwd_file:
        for word in pwd_file:
            upper = pdf_reader.decrypt(word.upper())
            lower = pdf_reader.decrypt(word.lower())
            if upper or lower:
                print(word.upper() if upper else word.lower())
                break


if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    break_pdf_password('encrypted.pdf', 'dictionary.txt')
