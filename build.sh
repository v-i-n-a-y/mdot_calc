set -e

pyinstaller --noconsole --onefile -i "bernoulli.ico" --name "Mass Flow Calc" main.py
