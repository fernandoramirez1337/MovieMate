from neo4j import GraphDatabase, basic_auth
from neo4j.exceptions import Neo4jError
import json

class Neo4jConnection:

    def __init__(self, uri, username, password):
        self.id_global = 1000
        self._uri = uri
        self._username = username
        self._password = password
        self._driver = None

    def close(self):
        if self._driver is not None:
            self._driver.close()

    def connect(self):
        self._driver = GraphDatabase.driver(self._uri, auth=basic_auth(self._username, self._password))

    def find_node_user(self, user_name):
        query = (
            "MATCH (u:User {name: $user}) "
            "RETURN { name: u.name, userId: u.userId } AS user"
        )
        try:
            with self._driver.session() as session:
                result = session.run(query,{"user": user_name})
                records = [dict(record) for record in result]
            return records
        except Neo4jError as e:
            print(f"Neo4jError: {e}")
            return None
        
    def find_node_movie(self, movie_title):
        query = (
            "MATCH (m:Movie {title: $title}) "
            "RETURN { title: m.title, imdbId: m.imdbId, plot: m.plot } AS movie"
        )
        try:
            with self._driver.session() as session:
                result = session.run(query,{"title": movie_title})
                records = [dict(record) for record in result]
            return records
        except Neo4jError as e:
            print(f"Neo4jError: {e}")
            return None
        
    def find_relationship_rated(self, user_name, movie_title):
        query = (
            "MATCH (m:Movie {title: $title})-[r:RATED]-(u:User {name: $name}) "
            "return { movie: m.title, user: u.name, rating: r.rating} AS rating "
        )
        try:
            with self._driver.session() as session:
                result = session.run(query,{"title": movie_title, "name": user_name})
                records = [dict(record) for record in result]
            return records
        except Neo4jError as e:
            print(f"Neo4jError: {e}")
            return None
        
    def create_node_user(self, node_json):
        name = node_json.get("nodeProperties", {}).get("name")

        if self.find_node_user(name):
            print(f'Node with value "{name}" already exists.')
            return
        print(f'Node with value "{name}" not exists.')

        labels = node_json.get("nodeType", [])
        properties = node_json.get("nodeProperties", {})
        query = (
        f"CREATE (n:{':'.join(labels)}) SET n = $properties "
        )
        with self._driver.session() as session:
            session.run(query, properties = properties)

        if self.find_node_user(name):
            print(f'Node with value "{name}" already exists.')
        else: 
            print(f'Node with value "{name}" not exists.')
        return
    
    def execute_query_and_save_to_file(self, output_file_path, query, parameters=None):
        try:
            with self._driver.session() as session:
                result = session.run(query,parameters)
                records = [dict(record) for record in result]
            with open(output_file_path, "w") as output_file:
                json.dump(records, output_file, indent=2)
            print(f"Result saved to {output_file_path}")
        except Exception as e:
            print(f"Error: {e}")

    def generate_user_json(self, name):
        self.id_global += 1
        node_json = {
            "nodeProperties": {
                "name": f"{name}",
                "userId": self.id_global
            },
            "nodeType": [
                "User"
            ]
        }
        return node_json

        

def main():
    # SANDBOX
    # neo4j_conn = Neo4jConnection("bolt://44.197.239.196:7687", "neo4j", "recruit-presence-captain")
    # LOCAL SANDBOX
    neo4j_conn = Neo4jConnection("bolt://34.203.189.174:7687", "neo4j", "resolution-terminations-duration")

    neo4j_conn.connect()

    test03_query = neo4j_conn.find_node_user("Margaret Allen")
    if not test03_query:
        print("No")
    else:
        print(json.dumps(test03_query, indent=2))
    test03_query = neo4j_conn.find_node_user("Yessenia")
    if not test03_query:
        print("No")
    else:
        print(json.dumps(test03_query, indent=2))
    test03_query = neo4j_conn.find_node_user("Fernando")
    if not test03_query:
        print("No")
    else:
        print(json.dumps(test03_query, indent=2))
    test03_query = neo4j_conn.find_node_movie("Toy Story")
    if not test03_query:
        print("No")
    else:
        print(json.dumps(test03_query, indent=2))
    test03_query = neo4j_conn.find_relationship_rated("Glenn Mitchell", "Toy Story")
    if not test03_query:
        print("No")
    else:
        print(json.dumps(test03_query, indent=2))


    neo4j_conn.close()

if __name__ == "__main__":
    main()