"""
Exercice 3 - Valid Parentheses

Ecrire la fonction is_valid_parentheses(s).

La fonction doit retourner True si les parentheses, crochets et accolades
sont correctement fermes et correctement imbriques.

Caracteres possibles :
- parentheses : ( )
- crochets : [ ]
- accolades : { }

Une chaine vide est consideree comme valide.

Exemple :
s = "{[]}"
resultat attendu : True
"""


def is_valid_parentheses(s: str) -> bool:
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


def check(name: str, result: bool, expected: bool) -> bool:
    if result == expected:
        print(f"[OK] {name}")
        return True

    print(f"[KO] {name}")
    print(f"     obtenu   : {result}")
    print(f"     attendu  : {expected}")
    return False


tests = [
    ("parentheses simples", "()", True),
    ("trois paires", "()[]{}", True),
    ("mauvaise fermeture", "(]", False),
    ("mauvais ordre", "([)]", False),
    ("imbrication correcte", "{[]}", True),
    ("chaine vide", "", True),
]


if __name__ == "__main__":
    passed = 0

    for name, s, expected in tests:
        result = is_valid_parentheses(s)
        if check(name, result, expected):
            passed += 1

    total = len(tests)
    print(f"\nResultat : {passed}/{total} tests reussis")
