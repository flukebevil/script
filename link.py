import subprocess
bash = "wget --spider -r https://www.20scoops.com 2>&1 | grep '^--' | awk '{ print $3 }' | grep -v '\.\(css\|js\|png\|gif\|jpg\|JPG\)$' > urls.txt"
process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
output, error = process.communicate
