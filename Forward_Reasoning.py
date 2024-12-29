def unify(x, y, subst=None):
    if subst is None:
        subst = {}
    # Step 1: If x and y are the same, return the current substitutions
    if x == y:
        return subst
    # If x is a variable
    if is_variable(x):
        return unify_var(x, y, subst)
    # If y is a variable
    if is_variable(y):
        return unify_var(y, x, subst)
    # If x and y are compound expressions
    if is_compound(x) and is_compound(y):
        if get_predicate(x) != get_predicate(y):
            return "FAILURE"
        return unify(get_args(x), get_args(y), subst)

    # If x and y are lists
    if isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return "FAILURE"
        if not x and not y:
            return subst
        return unify(x[1:], y[1:], unify(x[0], y[0], subst))

    # If x and y are constants or cannot be unified
    return "FAILURE"

def unify_var(var, x, subst):
    if var in subst:
        return unify(subst[var], x, subst)
    if x in subst:
        return unify(var, subst[x], subst)
    if occurs_check(var, x):
        return "FAILURE"
    subst[var] = x
    return subst

def occurs_check(var, x):
    if var == x:
        return True
    if isinstance(x, list):
        return any(occurs_check(var, arg) for arg in x)
    return False

def is_variable(x):
    return isinstance(x, str) and x.islower()  # Variables are lowercase strings

def is_compound(x):
    return isinstance(x, str) and '(' in x and ')' in x

def get_predicate(x):
    return x.split('(')[0]

def get_args(x):
    return x[x.index('(') + 1:x.index(')')].split(',')

# Test cases
x1 = "f(x, y)"
x2 = "f(a, b)"
print(unify(x1, x2))  # Expected: {'x': 'a', 'y': 'b'}

x3 = "p(x, g(y))"
x4 = "p(f(a), g(b))"
print(unify(x3, x4))  # Expected: {'x': 'f(a)', 'y': 'b'}

expression_a = "Eats(x, Apple)"
expression_b = "Eats(Riya, y)"

substitution = unify(expression_a, expression_b)

# Print the result
if substitution == "FAILURE":
    print("Unification failed.")
else:
    print("Unification successful:")
    print(substitution)
# Define the Knowledge Base (KB)
kb = []
# Facts
kb.append(("fact", "American", ["Robert"]))
kb.append(("fact", "Enemy", ["A", "America"]))
kb.append(("fact", "Missile", ["T1"]))
# Rules
kb.append(("rule", ["Missile(x)"], "Weapon(x)"))  # All missiles are weapons
kb.append(("rule", ["Weapon(x)", "Sells(Robert, x, A)", "Hostile(A)"], "Criminal(Robert)"))  # Selling weapons to hostiles implies criminality
kb.append(("rule", ["Enemy(x, America)"], "Hostile(x)"))  # Enemies of America are hostile
kb.append(("fact", "Sells", ["Robert", "T1", "A"]))  # Robert sells T1 to A

# Forward Reasoning Function
def forward_reasoning(kb, query):
    inferred = set()  # Already inferred facts
    while True:
        new_inferred = set()
        for entry in kb:
            if entry[0] == "fact":
                # Add atomic facts to inferred
                fact_name = entry[1]
                fact_args = tuple(entry[2])
                new_inferred.add((fact_name, fact_args))

            elif entry[0] == "rule":
                # Check if the rule's premise is satisfied
                premises = entry[1]
                conclusion = entry[2]

                # Evaluate premises
                premises_satisfied = True
                substitutions = {}
                for premise in premises:
                    satisfied = False
                    for fact in inferred:
                        fact_name, fact_args = fact
                        if match(premise, fact_name, fact_args, substitutions):
                            satisfied = True
                            break
                    if not satisfied:
                        premises_satisfied = False
                        break

                # If all premises are satisfied, infer the conclusion
                if premises_satisfied:
                    conclusion_name, conclusion_args = parse_predicate(conclusion)
                    conclusion_args = [
                        substitutions.get(arg, arg) for arg in conclusion_args
                    ]
                    new_inferred.add((conclusion_name, tuple(conclusion_args)))

        # If no new facts are inferred, stop
        if not new_inferred.difference(inferred):
            break
        inferred.update(new_inferred)

        # Check if the query is inferred
        query_name, query_args = parse_predicate(query)
        if (query_name, tuple(query_args)) in inferred:
            return True

    return False

# Helper functions for matching and parsing
def match(premise, fact_name, fact_args, substitutions):
    premise_name, premise_args = parse_predicate(premise)
    if premise_name != fact_name or len(premise_args) != len(fact_args):
        return False
    for p_arg, f_arg in zip(premise_args, fact_args):
        if p_arg.islower():  # Variable
            substitutions[p_arg] = f_arg
        elif p_arg != f_arg:  # Constant mismatch
            return False
    return True

def parse_predicate(predicate):
    name, args = predicate.split("(")
    args = args[:-1].split(",")  # Remove closing ")"
    return name, args

# Query
query = "Criminal(Robert)"

# Check if the query can be proved
if forward_reasoning(kb, query):
    print(f"The query {query} can be proved.")
else:
    print(f"The query {query} cannot be proved.")

