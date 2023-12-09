# neo4j_queries.py

class Neo4jQueries:
    #SIMPLE GET NODE TYPE QUERIES 
    @staticmethod
    def get_user_by_name():
        return (
            "MATCH (u:User {name: $user_name}) "
            "RETURN { name: u.name, userId: u.userId } AS user"
        )
    @staticmethod
    def get_movie_by_title():
        return (
            "MATCH (m:Movie {title: $movie_title}) "
            "RETURN { title: m.title, imdbId: m.imdbId, plot: m.plot } AS movie"
        )
    #SIMPLE GET RELATIONSHIP TYPE QUERIES
    @staticmethod
    def get_R_rated():
        return (
            "MATCH (m:Movie {title: $movie_title})-[r:RATED]-(u:User {name: $user_name}) "
            "RETURN { movie: m.title, user: u.name, rating: r.rating} AS rating"
        )
    #COMPLEX GET NODE TYPE QUERIES
    @staticmethod
    def get_suggested_users():
        return (
            "MATCH (me:User {name: $user_name})-[my:RATED]->(m:Movie) "
            "MATCH (other:User)-[their:RATED]->(m) "
            "WHERE me <> other "
            "AND abs(my.rating - their.rating) < 0.5 "
            "WITH other, COUNT(m) AS n, COLLECT(m.title) as Movies_in_common "
            "RETURN other.name AS Friend_suggestion,n , Movies_in_common "
            "ORDER BY n DESC "
            "LIMIT $limit "
        )
    @staticmethod
    def get_suggested_movies():
        return ()   
    #CREATE NODE TYPE QUERIES
    @staticmethod
    def create_node_user():
        return ()
    #CREATE RELATIONSHIP TYPE QUERIES
    def create_relation_rating():
        return ()