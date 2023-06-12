def noteEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "title": item["title"],
        "desc":item["desc"],
        "important":item["important"]
    }
    
def notesEntity(ITEMS) -> list:
    return [noteEntity(item) for item in ITEMS] 