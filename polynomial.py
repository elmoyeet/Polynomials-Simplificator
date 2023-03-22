import os
import sys
import time
import re
import logging
from colorama import Fore

try:
    logging.getLogger().setLevel(logging.ERROR)

    def watermark():
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix/Linux/MacOS
            os.system('clear')
        print(f"""{Fore.RED}     _____     _                   _     _ 
    |  _  |___| |_ _ ___ ___ _____|_|___| |
    |   __| . | | | |   | . |     | | .'| |
    |__|  |___|_|_  |_|_|___|_|_|_|_|__,|_|
                |___|                      
                """)
        print("""By: ELMO!#9999 | Math time! :)""")
        print("(Ctrl + c) to stop the process")
        print("")

    def simplify_polynomial(polynomial):
        terms = re.findall(r"[+-]?\s*\d*\s*x(?:\^\d+)?|[+-]?\s*\d+|[+-]?\s*x", polynomial)
        coefficients = {}
        for term in terms:
            match = re.match(r"([+-]?\s*\d*)(?:\s*x(?:\^(\d+))?)?", term)
            coefficient = int(match.group(1).replace(" ", "")) if match.group(1) else 1
            exponent = int(match.group(2)) if match.group(2) else 1 if "x" in term else 0
            if exponent in coefficients:
                coefficients[exponent] += coefficient
            else:
                coefficients[exponent] = coefficient
        simplified_polynomial = ""
        for exponent in sorted(coefficients.keys(), reverse=True):
            coefficient = coefficients[exponent]
            if coefficient == 0:
                continue
            if exponent == 0:
                simplified_polynomial += f"{'' if simplified_polynomial else ''}{coefficient}"
            elif exponent == 1:
                simplified_polynomial += f" {'+' if coefficient > 0 and simplified_polynomial else ''}{coefficient if abs(coefficient) != 1 else ''}x"
            else:
                simplified_polynomial += f" {'+' if coefficient > 0 and simplified_polynomial else ''}{coefficient if abs(coefficient) != 1 else ''}x^{exponent}"
        simplified_polynomial = simplified_polynomial.lstrip("+").lstrip()
        return simplified_polynomial

    while True:
        watermark()
        logging.getLogger().setLevel(logging.ERROR)

        polynomial = input("Polynomial: ")

        try:
            simplified_polynomial = simplify_polynomial(polynomial)
            print(f"Simplificado: {simplified_polynomial}")
            time.sleep(5)
        except:
            print("Invalid structure. (if you have put \"x\" replace it with \"1x\")")
            time.sleep(2)
            continue
except KeyboardInterrupt:
    print("Exiting polynomial by ELMO#999 in 5 seconds...")
    time.sleep(5)
    sys.exit(0)