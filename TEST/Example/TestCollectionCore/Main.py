from PyClass import A, B, C, D, E, F
from CollectionCore import get_all_subclasses, get_subclasses_excluding


def main():
    # Demo for get_all_subclasses
    print("All subclasses of A:")
    for cls in get_all_subclasses(A):
        print(f" - {cls.__name__}")
    
    print("\nAll subclasses of B:")
    for cls in get_all_subclasses(B):
        print(f" - {cls.__name__}")
    
    # Demo for get_subclasses_excluding
    print("\nSubclasses of A excluding B and its subclasses:")
    for cls in get_subclasses_excluding(A, B):
        print(f" - {cls.__name__}")


if __name__ == "__main__":
    main() 