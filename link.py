import subprocess
import json
import os
from pprint import pprint
base_path = os.path.abspath('.')
script_command = []

with open(base_path+'/totalOfficeURL.json') as f:
    data = json.load(f)

for url in data:
    bash = "wget --spider -r " + \
        url['link'] + \
        " 2>&1 | grep '^--' | awk '{ print $3 }' | grep -v '\.\(css\|js\|png\|gif\|jpg\|JPG\)$' > " + \
        url['link']+".txt"
    script_command.append(bash.split())

procs = [subprocess.Popen(i) for i in script_command]
for pc in procs:
    pc.wait()
# process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
# output, error = process.communicate
