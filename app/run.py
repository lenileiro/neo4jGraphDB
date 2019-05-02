from py2neo import Graph , Node, Relationship

user="neo4j"
pwd="neo4j"

graph = Graph(auth=(user, pwd))
alice = Node("Person", name="Alice")
bob = Node("Person", name="Bob")
alice_knows_bob = Relationship(alice, "KNOWS", bob)
graph.create(alice_knows_bob)