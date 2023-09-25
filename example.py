from bs4 import BeautifulSoup

f = open("index.html", "r")
data = f.read()

soup = BeautifulSoup(data, 'html.parser')
# print(soup)


#  Count and print divs
divs = soup.select("div")

print(len(divs), "divs found")

for d in divs:
    print(d)

print("Content of div[0]", divs[0].get_text())

# Drill down through div
div2 = divs[1]

print("\nParagraph texts\n")

pps = div2.select("p")

for p in pps:
    print(p.get_text())

print("\n daily classes \n")

dailies = soup.select(".daily")
for d in dailies:
    print(d.get_text())

print("\n Dictionary attributes, and single key selection\n")

print(dailies[1].attrs)
print(dailies[1].attrs['data-value'])
