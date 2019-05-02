from py2neo import Graph , Node, Relationship, Database

user="neo4j"
pwd="pass"

graph = Graph(auth=(user, pwd))
person = graph.run("MATCH (n:Person {name:'Bob'}) RETURN n.name").data()
relationships = graph.run("""
MATCH (a:Person {name:'Alice'}) - [:KNOWS] - (b:Person)
UNWIND [a.name] AS list_a
UNWIND [b.name] AS list_b
RETURN list_a, list_b
""").data()

for rel in relationships:
    print(rel)

#delete_once = graph.run("MATCH (a:Person {name:'Bob'}) - [r] - (b) DELETE r,a")
#delete_all = graph.run("MATCH (n) OPTIONAL MATCH (n) - [r] -() DELETE n,r")

#print(relationships)



 