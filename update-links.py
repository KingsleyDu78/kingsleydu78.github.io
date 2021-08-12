import glob
import re
files = glob.glob("*.html")

f = open("links.txt", "r")
links = f.read()
f.close()
for a_file in files:
    f = open(a_file, "r")
    file_content = f.read()
    to_write = re.sub("<!-- Begin Links -->.*?<!-- End Links -->", "<!-- Begin Links -->\n{}\n<!-- End Links -->".format(links), file_content, flags=re.DOTALL)
    f.close()
    f = open(a_file, "w")
    f.write(to_write)
    f.close()