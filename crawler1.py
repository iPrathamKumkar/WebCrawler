# Importing the libraries
import requests
from bs4 import BeautifulSoup

# Step 1: Sending a HTTP request to a URL
result = requests.get("http://www.wikicfp.com/cfp/call?conference=big%20data%20&page=1")
src = result.text

# Step 2: Parse the HTML content
soup = BeautifulSoup(src, "html5lib")

# Step 3: Analyze the HTML tag, where your content lives
# Extract the rows containing the data
rows = soup.select("body > div.contsec > center > form > table > tbody > tr:nth-child(3) > td > table > tbody > tr")

# Step 4: Write the details of each conference in a file
# Each element is separated by a tab space
with open("data.txt", "w") as file:
    newConf = True
    for row in rows:
        newConf = not newConf
        tdTags = row.find_all("td", {"align" : "left"})
        string = ""
        for data in tdTags:
            string += data.text + "\t"
        if newConf:
            file.write("\n" + string.strip())
        else:
            file.write("\t" + string.strip())
    file.close()
