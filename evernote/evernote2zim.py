import re
import sys

__author__ = 'hiqhan'
html_filename = 'Evernote.html'
links_filename = 'SharedLinks.txt'
output_filename = 'evernote.txt'

if __name__ == "__main__":
	# read from exported html
    with open(html_filename) as html_file:
        s = html_file.read()
	# get shared links from file
    with open(links_filename, 'r') as link_file:
        links = link_file.readlines()

	# get title
    start = '<h1>'
    end = '</h1>'
    title = re.findall(re.escape(start)+"(.*)"+re.escape(end), s)

	# the number of titles should be equal to links'
    if len(title) != len(links):
        print "title lines are not equal to links"
        sys.exit(0)

    else:
        res = ["* [[" + links[i].strip() + "|" + title[i] + "]]" for i in range(len(title))]

	# output the zim style
    with open(output_filename, 'w') as output:
        output.writelines('\n'.join(res))





