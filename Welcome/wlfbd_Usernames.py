import pywikibot as pw
import welcomeparameters

site = pw.Site('commons')
cat = pw.page.Category(site, welcomeparameters.Categorytocheck)
names = ""

for page in cat.newest_pages(total=1000000):
    file = pw.page.FilePage(site, page.title())
    name = file.get_file_history()[list(file.get_file_history())[-1]]['user']
    if name not in names: names+=name+"\n"

with open("wlfbd all uploaders.txt", "w") as file:
    file.write(names)
