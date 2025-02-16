import pywikibot as pw

site = pw.Site('commons')
cat = pw.page.Category(site, 'Images from Wiki Loves Folklore 2025 in Bangladesh')
names = ""

for page in cat.newest_pages(total=40):
    file = pw.page.FilePage(site, page.title())
    name = file.get_file_history()[list(file.get_file_history())[-1]]['user']
    if name not in names: names+=name+"\n"

with open("wlfbd usernames.txt", "w") as file:
    file.write(names)
