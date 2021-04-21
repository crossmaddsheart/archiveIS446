#
#

import xml.etree.cElementTree as ET

def main():
    tree = ET.ElementTree(file='mca_cat.xml')
    root = tree.getroot()

    for recordid in root:
        recordid = recordid.text

#    for recordid in root('recordid'):
#        print(recordid.text)


main()

