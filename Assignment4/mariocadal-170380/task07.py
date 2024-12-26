# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yPniC8cCIRK0ofpUQK_h0bcNOa4CroCF

**Task 07: Querying RDF(s)**
"""

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

"""First let's read the RDF file"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**"""

# TO DO
query_subclasses_livingthing = """
    SELECT ?subclass WHERE {
        ?subclass rdfs:subClassOf ns:LivingThing.
    }
"""

print("Subclases de LivingThing:")
for r in g.query(query_subclasses_livingthing):
    print(r.subclass)


"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
query_individuals_person = """
    SELECT ?person WHERE {
        { ?person a ns:Person. } UNION {
            ?person a ?subclass.
            ?subclass rdfs:subClassOf ns:Person.
        }
    }
"""

print("Individuos de Person:")
for r in g.query(query_individuals_person):
    print(r.person)

"""**TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**

"""

query_individuals_person_animal = """
    SELECT ?individual WHERE {
        { ?individual a ns:Person. } UNION { 
            ?individual a ns:Animal.
        }
    }
"""

print("Individuos de Person o Animal:")
for r in g.query(query_individuals_person_animal):
    print(r.individual)


"""**TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**"""

# TO DO
query_persons_who_know_rocky = """
    SELECT ?name WHERE {
        ?person ns:knows ns:Rocky.
        ?person ns:name ?name.
    }
"""

print("Personas que conocen a Rocky:")
for r in g.query(query_persons_who_know_rocky):
    print(r.name)



"""**Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**"""

# TO DO
query_animals_know_another_animal = """
    SELECT ?animalName WHERE {
        ?animal ns:knows ?otherAnimal.
        ?animal a ns:Animal.
        ?otherAnimal a ns:Animal.
        ?animal ns:name ?animalName.
    }
"""

print("Animales que conocen al menos a otro animal:")
for r in g.query(query_animals_know_another_animal):
    print(r.animalName)

"""**Task 7.6: List the age of all living things in descending order (in SPARQL only)**"""

# TO DO
query_ages_of_living_things = """
    SELECT ?livingThing ?age WHERE {
        ?livingThing a ns:LivingThing.
        ?livingThing ns:age ?age.
    } ORDER BY DESC(?age)
"""

print("Edad de todos los seres vivos en orden descendente:")
for r in g.query(query_ages_of_living_things):
    print(r.livingThing, r.age)
