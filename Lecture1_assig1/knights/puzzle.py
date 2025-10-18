from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

same = Or(And(AKnight, BKnight), And(AKnave, BKnave))
different = Or(And(AKnight, BKnave), And(AKnave, BKnight))

# Additional symbols 
AsaidKnight = Symbol("A said 'I am a Knight'")
AsaidKnave  = Symbol("A said 'I am a Knave'")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    
    # TODO

    # Rule: A is either a Knight or a Knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # A says: "I am both a knight and a knave"
    # If A were a knight, the statement would be true (so A would be both)
    # If A were a knave, the statement would be false (so A would not be both)
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

knowledge2 = And(
    # TODO
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Implication(AKnight, same),
    Implication(AKnave, Not(same)),

    Implication(BKnight, different),
    Implication(BKnave, Not(different))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Each person is either knight or knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # A said either "I am a Knight" OR "I am a Knave", and not both
    Or(AsaidKnight, AsaidKnave),
    Not(And(AsaidKnight, AsaidKnave)),

    # If A actually said "I am a Knight":
    #    - If A is a knight, that statement must be true (AKnight)
    #    - If A is a knave, that statement must be false (Not(AKnight))
    Implication(AsaidKnight, Implication(AKnight, AKnight)),
    Implication(AsaidKnight, Implication(AKnave, Not(AKnight))),

    # If A actually said "I am a Knave":
    #    - If A is a knight, that statement must be true (AKnave)  <-- contradiction then
    #    - If A is a knave, that statement must be false (Not(AKnave)) <-- implies AKnight
    Implication(AsaidKnave, Implication(AKnight, AKnave)),
    Implication(AsaidKnave, Implication(AKnave, Not(AKnave))),

    # B says "A said 'I am a knave'."  => if B is knight then AsaidKnave is true;
    # if B is knave then AsaidKnave is false (he lies).
    Implication(BKnight, AsaidKnave),
    Implication(BKnave, Not(AsaidKnave)),

    # B also says "C is a knave."
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # C says "A is a knight."
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
