def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {object.__class__}")
    elif object.__class__ is float and object != 0.0:
        print(f"Cheese: {object} {object.__class__}")
    elif object.__class__ is int and object == 0:
        print(f"Zero: {object} {object.__class__}")
    elif object.__class__ is str and object == '':
        print(f"Empty: {object}{object.__class__}")
    elif object.__class__.__name__ == 'bool':
        print(f"Fake: {object} {object.__class__}")
    else:
        print("Type not found")

    return 1