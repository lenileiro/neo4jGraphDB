from py2neo import Graph , Node, Relationship

user="neo4j"
pwd="pass"

class App:
    @staticmethod
    def graph():
        graph = Graph(auth=(user, pwd))
        return graph