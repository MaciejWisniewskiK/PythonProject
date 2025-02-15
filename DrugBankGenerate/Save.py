import xml.etree.ElementTree as ET

def save(root, new_drugs, out_xml):
    for new_drug in new_drugs:
        root.append(new_drug)
    
    tree = ET.ElementTree(root)
    tree.write(out_xml, encoding="utf-8", xml_declaration=True)