def all_thing_is_obj(object: any) -> int:
    if (object.__class__ == str):
        print(object, "is in the kitchen :", object.__class__)
    elif (object.__class__ == int):
        print ("Type not found")
    else :
        print(object.__class__.__name__.capitalize(), ":", object.__class__)
    return 42
