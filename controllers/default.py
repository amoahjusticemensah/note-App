def addnote():
    return dict()

def store():
    submitted_topic = request.vars.topic,
    submitted_typenote = request.vars.typenote

    result = db.notes.insert(
        db_topic=submitted_topic,
        db_typenote =submitted_typenote
    )

    if result:
            return "Note Added Successfully"
    else:
            return "Connectivity Problem"    

def seenotes():
    notes =db().select(db.notes.ALL)
    return dict(notes=notes)   
    