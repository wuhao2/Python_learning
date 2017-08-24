from xml.etree.ElementTree import parse, Element
doc = parse('demo.xml')
root = doc.getroot()
print(root)

# Remove a few elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))
# Insert a new element after <nm>...</nm>
root.getchildren().index(root.find('nm'))

e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)

# Write back to a file
doc.write('newpred.xml', xml_declaration=True)

####################################################################
from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Download the RSS feed and parse it
# u = urlopen('http://planet.python.org/rss20.xml')
# doc = parse(u)
# e = doc.find('channel/title')
# print(e)
# print(e.tag)
# print(e.text)
# print(e.get('some_attribute'))
# print(list(doc.iter('title')))

# # Extract and output tags of interest
# for item in doc.iterfind('channel/item'):
#     title = item.findtext('title')
#     date = item.findtext('pubDate')
#     link = item.findtext('link')
#
#     print(title)
#     print(date)
#     print(link)
#     print()
################################################################################
from xml.etree.ElementTree import Element


def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)

    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
e = dict_to_xml('stock', s)
print(e)
from xml.etree.ElementTree import tostring
print(tostring(e))