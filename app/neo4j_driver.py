import os
from neo4j import GraphDatabase
from langchain_community.graphs import Neo4jGraph

#host = "bolt://172.17.0.2:7687"
host = "bolt://host.docker.internal:7687"
user = 'neo4j'
password = 'password'
driver = GraphDatabase.driver(host, auth=(user, password))


def get_schema():
    graph = Neo4jGraph(url="bolt://host.docker.internal:7687", username="neo4j", password="password")
    graph.refresh_schema()
    return graph.schema
    

def run_query(query, params={}):
    with driver.session() as session:
        result = session.run(query, params)
        response = [r.values()[0] for r in result]
        return response


if __name__ == '__main__':
    print(run_query("""
    MATCH (c:comment) RETURN n LIMIT 1
    RETURN {sample_comment: c.comment} AS result;
    """))
