import random
import copy
import xml.etree.ElementTree as ET

def generate_new_drugs(original_drugs : list[ET.Element], first_id : int, last_id : int) -> list[ET.Element]:
    """
        Generate new drugs with incrementing IDs and values randomly chosen from original ones.
    """
    ns = {'db': 'http://www.drugbank.ca'}

    new_drugs = []
    for i in range(first_id, last_id + 1):
        new_id = f"DB{i:05d}"
        new_drug = copy.deepcopy(random.choice(original_drugs))
        new_drug.find("db:drugbank-id", ns).text = new_id

        new_drugs.append(new_drug)
    
    return new_drugs