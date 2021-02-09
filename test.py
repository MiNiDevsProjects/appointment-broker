from datetime import datetime
import pytz

ist = pytz.timezone('Asia/Kolkata')
currentTime = datetime.now(ist)

filename = "time.txt"
try:
    f = open(filename, "w+")
    f.write(str(currentTime))
    f.close
except:
    print("Error Writing to the file")

try:
    f = open(filename, "r")
    print("\nPrinting from file:")
    print(f.read())
except:
    print("Error reading from the file")

