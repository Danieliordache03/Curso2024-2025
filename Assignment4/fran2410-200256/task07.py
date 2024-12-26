# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/121Gq_pFbL2pptY3eyx_vhwV_PrToIZJd

**Task 07: Querying RDF(s)**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

"""First let's read the RDF file"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, FOAF
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**"""

from rdflib.plugins.sparql import prepareQuery

NS = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")

q1 = prepareQuery('''
    SELECT ?subclass WHERE {
      ?subclass rdfs:subClassOf ns:LivingThing .
    }
''', initNs={"rdfs": RDFS, "ns": NS})

# Visualize the results
for r in g.query(q1):
    print(r.subclass)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

q2 = prepareQuery('''
    SELECT ?individual WHERE {
      ?individual rdf:type/rdfs:subClassOf* ns:Person .
    }
''', initNs={"rdf": RDF, "rdfs": RDFS, "ns": NS})

# Visualize the results
for r in g.query(q2):
    print(r.individual)

"""**TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**

"""

q3 = prepareQuery("""
    SELECT ?individual WHERE {
      { ?individual rdf:type ns:Person . }
      UNION
      { ?individual rdf:type ns:Animal . }
    }
""", initNs={"rdf": RDF, "ns": NS})

# Visualize the results
for r in g.query(q3):
    print(r.individual)

"""**TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**"""

q4 = prepareQuery('''
    SELECT ?individual ?Given WHERE {
      ?individual rdf:type/rdfs:subClassOf* ns:Person .
      ?individual foaf:knows ns:RockySmith .
      ?individual vcard:Given ?Given.
    }
''', initNs={"rdf": RDF, "foaf": FOAF, "vcard": VCARD, "ns": NS})

# Visualize the results
for r in g.query(q4):
    print( r.Given)

"""**Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**"""

q5 = prepareQuery('''
    SELECT ?individual ?Given WHERE {
      ?individual rdf:type/rdfs:subClassOf* ns:Animal .
      ?otro rdf:type ns:Animal .
      ?individual foaf:knows ?otro .
      ?individual vcard:Given ?Given.
    }
''', initNs={"rdf": RDF, "foaf": FOAF, "vcard": VCARD, "ns": NS})

# Visualize the results
for r in g.query(q5):
    print( r.Given)

"""**Task 7.6: List the age of all living things in descending order (in SPARQL only)**"""

q6 = prepareQuery("""
    SELECT ?livingThing ?age WHERE {
      ?livingThing rdf:type/rdfs:subClassOf* ns:LivingThing .
      ?livingThing foaf:age ?age .
    }
    ORDER BY DESC(?age)
""", initNs={"rdf": RDF,"foaf": FOAF, "ns": NS})

# Visualize the results
for r in g.query(q6):
    print(r.livingThing, r.age)