import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Class.calculator import Calculator  

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
