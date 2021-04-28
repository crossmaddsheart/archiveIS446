# file read_dict.py
#

from collections import defaultdict

def etree_to_dict(my_tree):
    my_dict = {my_tree.tag: {} if my_tree.attrib else None}
    children = list(my_tree)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        my_dict = {my_tree.tag: {k: v[0] if len(v) == 1 else v
                                 for k, v in dd.items()}}
    if my_tree.attrib:
        my_dict[my_tree.tag].update(('@' + k, v)
                                    for k, v in my_tree.attrib.items())
    if my_tree.text:
        text = my_tree.text.strip()
        if children or my_tree.attrib:
            if text:
                my_dict[my_tree.tag]['#text'] = text
        else:
            my_dict[my_tree.tag] = text
    return my_dict

if __name__ == "__main__":
    from pprint import pprint
    import xml.etree.ElementTree as ET

    dbt_xml = ET.parse('2468.xml')

    tree = dbt_xml.getroot()
    my_dict = etree_to_dict(record)

    print(type(my_dict))

    pprint(my_dict)
    print(my_dict)