import subprocess
import json
import os
from pprint import pprint
base_path = os.path.abspath('.')

with open(base_path+'/totalOfficeURL.json') as f:
    data = json.load(f)

for url in data:
    bash = "wget --spider -r "+data['link']+" 2>&1 | grep '^--' | awk '{ print $3 }' | grep -v '\.\(css\|js\|png\|gif\|jpg\|JPG\)$' > "+data.link+".txt"
    process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
    output, error = process.communicate
