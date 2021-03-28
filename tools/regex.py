# hht, regex
import base64
import csv
from io import StringIO


data = base64.b64decode(self.upload_file).decode('latin-1')
data = StringIO(data)
reader = csv.DictReader(data)
