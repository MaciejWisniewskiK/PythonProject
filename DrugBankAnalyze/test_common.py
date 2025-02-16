def is_valid_drugbank_id(id : str) -> bool:
    return len(id) == 7 and id[:2] == "DB" and id[2:].isdigit()