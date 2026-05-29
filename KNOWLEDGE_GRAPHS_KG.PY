# ==========================================
# KNOWLEDGE GRAPHS AND TOOLS TO BUILD KG
# Complete Single File Implementation
# ==========================================

# ------------------------------------------
# IMPORTING LIBRARIES
# ------------------------------------------

from rdflib import Graph, Literal, RDF, URIRef, Namespace
from neo4j import GraphDatabase


# ==========================================
# PART 1 : KNOWLEDGE GRAPH THEORY
# ==========================================

print("\n==========================================")
print("KNOWLEDGE GRAPHS")
print("==========================================")

print("""
A Knowledge Graph (KG) is a graph-based data structure
used to represent entities and relationships.

Main Components:
1. Nodes       -> Entities
2. Edges       -> Relationships
3. Properties  -> Attributes

Applications:
- Google Search
- Recommendation Systems
- Chatbots
- Semantic Search
""")


# ==========================================
# PART 2 : RDF KNOWLEDGE GRAPH USING RDFLIB
# ==========================================

print("\n==========================================")
print("CREATING RDF KNOWLEDGE GRAPH")
print("==========================================")

# Creating Graph
g = Graph()

# Creating Namespace
EX = Namespace("http://example.org/")

# Creating Entities
alice = URIRef(EX.Alice)
bob = URIRef(EX.Bob)

# Adding Relationships
g.add((alice, RDF.type, Literal("Person")))
g.add((bob, RDF.type, Literal("Person")))

g.add((alice, EX.knows, bob))

g.add((alice, EX.age, Literal(25)))
g.add((bob, EX.age, Literal(30)))

# Displaying Graph Triples
print("\nKnowledge Graph Triples:\n")

for subj, pred, obj in g:
    print(subj, pred, obj)

# Saving RDF File
g.serialize(destination="knowledge_graph.rdf")

print("\nRDF Graph saved as knowledge_graph.rdf")


# ==========================================
# PART 3 : EXPLORING KNOWLEDGE GRAPH TOOLS
# ==========================================

print("\n==========================================")
print("TOOLS USED FOR BUILDING KNOWLEDGE GRAPHS")
print("==========================================")

tools = {
    "Neo4j": "Graph Database",
    "Protégé": "Ontology Editor",
    "RDFLib": "Python RDF Processing Library",
    "Apache Jena": "Semantic Web Framework",
    "GraphDB": "RDF Triple Store"
}

for tool, desc in tools.items():
    print(f"{tool} --> {desc}")


# ==========================================
# PART 4 : NEO4J IMPLEMENTATION
# ==========================================

print("\n==========================================")
print("NEO4J KNOWLEDGE GRAPH EXAMPLE")
print("==========================================")

print("""
NOTE:
To run this section:
1. Install Neo4j Desktop
2. Start Neo4j Database
3. Change username/password below
""")


# Neo4j Connection Details
URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "password"

try:

    # Connecting to Neo4j
    driver = GraphDatabase.driver(
        URI,
        auth=(USERNAME, PASSWORD)
    )

    # Function to Add Person Node
    def add_person(tx, name):
        query = "CREATE (:Person {name: $name})"
        tx.run(query, name=name)

    # Creating Session
    with driver.session() as session:

        session.write_transaction(add_person, "Alice")
        session.write_transaction(add_person, "Bob")

    print("Nodes added successfully in Neo4j")

except Exception as e:
    print("Neo4j Connection Failed")
    print("Reason:", e)


# ==========================================
# PART 5 : SIMPLE KNOWLEDGE GRAPH QUERY
# ==========================================

print("\n==========================================")
print("QUERYING KNOWLEDGE GRAPH")
print("==========================================")

print("\nPeople in Knowledge Graph:\n")

for subj, pred, obj in g.triples((None, RDF.type, None)):
    print(subj)

print("\nRelationships:\n")

for subj, pred, obj in g.triples((None, EX.knows, None)):
    print(f"{subj} knows {obj}")


# ==========================================
# PART 6 : APPLICATIONS OF KNOWLEDGE GRAPHS
# ==========================================

print("\n==========================================")
print("APPLICATIONS OF KNOWLEDGE GRAPHS")
print("==========================================")

applications = [
    "Search Engines",
    "Recommendation Systems",
    "Healthcare Systems",
    "Chatbots",
    "Fraud Detection",
    "Social Networks"
]

for app in applications:
    print("-", app)


# ==========================================
# PART 7 : ADVANTAGES
# ==========================================

print("\n==========================================")
print("ADVANTAGES OF KNOWLEDGE GRAPHS")
print("==========================================")

advantages = [
    "Better data representation",
    "Efficient relationship modelling",
    "Semantic understanding",
    "Easy querying of connected data",
    "Supports AI applications"
]

for adv in advantages:
    print("-", adv)


# ==========================================
# PART 8 : TEST CASES
# ==========================================

print("\n==========================================")
print("TEST CASES")
print("==========================================")

print("""
Test Case 1:
Input  : Add Alice and Bob
Output : Nodes created successfully

Test Case 2:
Input  : Alice knows Bob
Output : Relationship stored in RDF graph

Test Case 3:
Input  : Query all persons
Output : Alice, Bob
""")


# ==========================================
# PART 9 : VIVA QUESTIONS
# ==========================================

print("\n==========================================")
print("VIVA QUESTIONS")
print("==========================================")

viva = {
    "What is a Knowledge Graph?":
        "A graph-based structure used to represent entities and relationships.",

    "What is RDF?":
        "Resource Description Framework used for representing web data.",

    "What is Neo4j?":
        "A graph database used for storing and querying graph data.",

    "What are Triples in RDF?":
        "Subject, Predicate, Object.",

    "What is an Ontology?":
        "A formal representation of concepts and relationships."
}

for q, ans in viva.items():
    print(f"\nQ: {q}")
    print(f"A: {ans}")


# ==========================================
# END OF PROGRAM
# ==========================================

print("\n==========================================")
print("KNOWLEDGE GRAPH IMPLEMENTATION COMPLETED")
print("==========================================")
