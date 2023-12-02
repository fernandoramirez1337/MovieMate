from neo4j import GraphDatabase, basic_auth
import json

class Neo4jConnection:
    def __init__(self, uri, username, password):
        self._uri = uri
        self._username = username
        self._password = password
        self._driver = None
    
    def close(self):
        if self._driver is not None:
            self._driver.close()
    
    def connect(self):
        self._driver = GraphDatabase.driver(self._uri, auth=basic_auth(self._username, self._password))
    
    def user_exists(self, user):
        query = (
        "MATCH (u:User {name: $user}) "
        "RETURN u.name IS NOT NULL AS nodeExists"
        )
        with self._driver.session() as session:
            result = session.run(query,user=user).single()
            if result:  
                return result["nodeExists"]
            return False
    
    def execute_query(self, query, parameters=None):
        with self._driver.session() as session:
            result = session.run(query, parameters)
            return result
        
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
    
    def create_node_from_json(self, node_json):
        name = node_json.get("nodeProperties", {}).get("name")

        if name is not None and self.user_exists(name):
            print(f'Node with value "{name}" already exists.')
            return
        
        labels = node_json.get("nodeType", [])
        properties = node_json.get("nodeProperties", {})
        query = (
            F"CREATE (n:{':'.join(labels)} $properties)"
        )
        with self._driver.session() as session:
            session.run(query, properties = properties)
    
    def get_node_relations(self, node_json):
        return
 

#LOCAL TEST
# neo4j_conn = Neo4jConnection("neo4j://44.200.3.71:7687", "neo4j", "site-evidence-barriers")
# CONNECTED
neo4j_conn = Neo4jConnection("bolt://44.197.239.196:7687", "neo4j", "recruit-presence-captain")

neo4j_conn.connect()

query_01 = neo4j_conn.user_exists("Fernando")
query_02 = neo4j_conn.user_exists("Yessenia")
query_get_labels = (
    "MATCH (n) "
    "RETURN labels(n) AS nodeType, COUNT(n) AS count "
    "ORDER BY count DESC "
    )
query_get_n_user = (
    "MATCH (u:User) "
    "RETURN properties(u) AS nodeProperties, labels(u) AS nodeType "
    "LIMIT 100 "
    )
query_get_n_movie = (
    "MATCH (m:Movie) "
    "RETURN properties(m) AS nodeProperties, labels(m) AS nodeType "
    "LIMIT 100 "
    )
query_get_n_actor = (
    "MATCH (a:Actor) "
    "RETURN properties(a) AS nodeProperties, labels(a) AS nodeType "
    "LIMIT 100 "
    )
query_get_n_director = (
    "MATCH (d:Director) "
    "RETURN properties(d) AS nodeProperties, labels(d) AS nodeType "
    "LIMIT 100 "
    )
query_get_n_genre = (
    "MATCH (g:Genre) "
    "RETURN properties(g) AS nodeProperties, labels(g) AS nodeType "
    "LIMIT 100 "
    )
query_get_movie_relations = (
    "MATCH (m:Movie {title: 'Toy Story'})-[:IN_GENRE]-(g:Genre)" 
    "RETURN g.name"
    )
get_n_movies_by_genre = (
    "MATCH (g:Genre {name: 'Comedy'})-[:IN_GENRE]-(m:Movie) " 
    "RETURN m.title as Movie "
    "LIMIT 10 "
)
def get_n_movies_by_genre(genre_name, limit = 10):
    query = (
        "MATCH (g:Genre {name: $genre_name})-[:IN_GENRE]-(m:Movie) "
        "RETURN m.title as Movie "
        f"LIMIT {limit}"
    )
    return query, {"genre_name" : genre_name}


tmp = ("    MATCH (me:User {name:'Omar Huffman'})-[my:RATED]->(m:Movie {name: 'Toy Story'}) MATCH (other:User)-[their:RATED]->(m) WHERE me <> other AND abs(my.rating - their.rating) < 1 RETURN other.name, their:RATED")

#neo4j_conn.execute_query_and_save_to_file(query_get_n_user,"user_list.txt")
#neo4j_conn.execute_query_and_save_to_file(query_get_n_movie,"movie_list.txt")
#neo4j_conn.execute_query_and_save_to_file(query_get_n_actor,"actor_list.txt")
#neo4j_conn.execute_query_and_save_to_file(query_get_n_director,"director_list.txt")
#neo4j_conn.execute_query_and_save_to_file(query_get_n_genre,"genre_list.txt")
#neo4j_conn.execute_query_and_save_to_file(query_get_movie_relations,"test03.txt",'Toy Story')

genre_name = "Comedy"
limit = 10
cypher_query, cypher_params = get_n_movies_by_genre(genre_name, limit)
neo4j_conn.execute_query_and_save_to_file("get_movies_by_genre.txt",cypher_query, cypher_params)


# neo4j_conn.execute_cypher_query_and_save_to_file(query_get_movie_relations,"movie_test01.txt")

node_json = {
    "nodeProperties": {
        "name": "Yessenia",
        "userId": "1002"
    },
    "nodeType": [
        "User"
    ]
}
neo4j_conn.create_node_from_json(node_json)

neo4j_conn.close()