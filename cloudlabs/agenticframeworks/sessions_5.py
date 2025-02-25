
# This program demonstrates a simple knowledge representation and reasoning system using a rule-based approach.
# We represent knowledge using facts and rules.  Facts are simple assertions, and rules are implications of the form IF condition THEN conclusion.
# The system uses forward chaining to deduce new facts from existing ones and rules.

# Define facts as a dictionary.  Keys are fact names, values are booleans indicating truth.
facts = {
    "bird": True,
    "flies": False,  # Initially unknown
    "penguin": False,
}

# Define rules as a list of dictionaries. Each dictionary represents a rule with "condition" and "conclusion" keys.
# Conditions are lists of facts that must be true for the conclusion to be drawn.
rules = [
    {"condition": ["bird"], "conclusion": "flies"},  # Rule 1: If it's a bird, it flies.
    {"condition": ["bird", "penguin"], "conclusion": "flies", "negate": True}, #Rule 2: If it's a bird and a penguin, it doesn't fly (negation example)

]


def forward_chaining(facts, rules):
    # This function performs forward chaining inference.
    inferred_facts = {} #Keep track of newly inferred facts to avoid infinite loops.
    while True:
        changed = False
        for rule in rules:
            condition_met = True
            for fact in rule["condition"]:
                #Check for negation using an optional "negate" key in the rule
                negate = rule.get("negate",False)
                if (fact not in facts or facts[fact] != (not negate)):
                    condition_met = False
                    break

            if condition_met:
                conclusion = rule["conclusion"]
                if conclusion not in facts and conclusion not in inferred_facts:
                    facts[conclusion] = True
                    inferred_facts[conclusion] = True
                    changed = True
                    print(f"Inferred: {conclusion} is True")

        if not changed:
            break  # No new facts inferred, stop the loop.

    return facts


# Run the forward chaining inference engine
updated_facts = forward_chaining(facts, rules)


# Print the final set of facts.
print("\nFinal Facts:")
for fact, value in updated_facts.items():
    print(f"{fact}: {value}")

# Example of adding a new fact and re-running inference (demonstrates dynamic knowledge update).
facts["penguin"] = True
updated_facts = forward_chaining(facts, rules)
print("\nFinal Facts after adding penguin fact:")
for fact, value in updated_facts.items():
    print(f"{fact}: {value}")


