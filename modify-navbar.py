import glob
import re
files = glob.glob("*.html")

print("------------------------------\nMODIFY PAGE NAVBARS\n------------------------------")
page_name = input("Name of page? ")
file_name = input("File name of page? ")
f = open("links.txt", "r")
links = f.read()
f.close()
links += '\n<li class="nav-item">\n<a class="nav-link" href="{}.html">{}</a>\n</li>'.format(file_name, page_name)
f = open("links.txt", "w")
f.write(links)
f.close()
for a_file in files:
    new_links = []
    for link in links.strip().split("\n"):
        if a_file in link:
            new_links.append(link.replace("nav-link", "nav-link active"))
        else:
            new_links.append(link)
    new_links = "\n".join(new_links)
    f = open(a_file, "r")
    file_content = f.read()
    to_write = re.sub("<!-- Begin Links -->.*?<!-- End Links -->", "<!-- Begin Links -->\n{}\n<!-- End Links -->".format(new_links), file_content, flags=re.DOTALL)
    f.close()
    f = open(a_file, "w")
    f.write(to_write)
    f.close()