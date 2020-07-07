glossary = {
    "Key-value pair": "A key-value pair is a set of values associated with each other.",
    "Tuples": "Lists work well for storing collections of items that can change throughout the life of a program. Sometimes you’ll want to create a list of items that cannot change.",
    "Multiple Assignment": "You can assign values to more than one variable using just a single line. ",
    "Python Enhancement Proposal (PEP)": "Style guide that nstructs Python programmers on how to style their code.",
    "Python;s dictionaries": "Allows you to connect pieces of related information."
}

for words, meaning in glossary.items():
    print(f"\n{words}: {meaning}")