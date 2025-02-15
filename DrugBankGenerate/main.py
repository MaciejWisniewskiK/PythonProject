from Parse import parse
from Generate import generate_new_drugs
from Save import save
import xml.etree.ElementTree as ET

og_xml = "data/drugbank_partial.xml"
out_xml = "data/drugbank_partial_and_generated.xml"
num_new_drugs = 10#19900

original_drugs, max_id, root = parse(og_xml)
new_drugs = generate_new_drugs(original_drugs, max_id + 1, max_id + num_new_drugs)
save(root, new_drugs, out_xml)

