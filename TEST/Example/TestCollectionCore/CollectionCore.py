def get_all_subclasses(cls):
    """
    Return all subclasses of the given class, including subclasses of subclasses.
    
    Args:
        cls: The class to find subclasses for
        
    Returns:
        A list of all subclasses
    """
    all_subclasses = []
    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))
    return all_subclasses


def get_subclasses_excluding(cls1, cls2):
    """
    Return all subclasses of cls1, excluding all subclasses of cls2.
    
    Args:
        cls1: The class to find subclasses for
        cls2: The class whose subclasses should be excluded
        
    Returns:
        A list of subclasses of cls1 that are not subclasses of cls2
    """
    all_subclasses = get_all_subclasses(cls1)
    excluded_subclasses = [cls2] + get_all_subclasses(cls2)
    
    return [cls for cls in all_subclasses if cls not in excluded_subclasses] 