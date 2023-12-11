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
    @staticmethod
    def get_movies_rated_by_user():
        return (
            "MATCH (me:User {name: $user_name})-[my:RATED]->(m:Movie) "
            "RETURN m.title AS movie, my.rating AS rating "
            "ORDER BY rating DESC "
            "LIMIT $limit "
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
    def get_popular_movies():
        return (
            "MATCH (m:Movie)<-[r:RATED]-() "
            "MATCH (m:Movie)-[IN_GENRE]->(g:Genre) "
            "RETURN COUNT(r) AS N_of_reviews, m.title as Movie, m.year as Year ,COLLECT(DISTINCT g.name) as Genre "
            "ORDER BY N_of_reviews DESC "
            "LIMIT $limit"
        )   
    def get_suggested_movies_based_on_actors():
        return (
            "MATCH (u:User {name: $user_name})-[r:RATED]->(m:Movie) "
            "MATCH (m)-[:ACTED_IN]-(a:Actor) "
            "MATCH (a)-[:ACTED_IN]-(mm:Movie) "
            "MATCH (mm)-[rr:RATED]-() "
            "WHERE m <> mm "
            "RETURN u.name AS User, m.title AS MyRatedMovie, r.rating AS Rating, a.name AS Actor, mm.title AS RecommendedMovie, COUNT(rr) AS n_ratings "
            "ORDER BY Rating DESC, n_ratings DESC "
            "LIMIT $limit"
        )
    def get_suggested_movies_based_on_actor_in_movie():
        return (
            "MATCH (u:User {name: 'Margaret Allen'})-[r:RATED]->(m:Movie) "
            "MATCH (m)-[:ACTED_IN]-(a:Actor) "
            "MATCH (a)-[:ACTED_IN]-(mm:Movie) "
            "MATCH (mm)-[rr:RATED]-() "
            "WHERE m <> mm AND r.rating >= 4.0 "
            "WITH u, m.title AS MyRatedMovie, r.rating AS Rating, a.name AS Actor, COLLECT(DISTINCT mm.title) AS RecommendedMovies, COUNT(rr) AS n_ratings "
            "RETURN u.name AS User, MyRatedMovie, Rating, Actor, RecommendedMovies, n_ratings "
            "ORDER BY RAND() "
            "LIMIT 1 "
        )
    #CREATE NODE TYPE QUERIES
    @staticmethod
    def create_node_user():
        return ()
    #CREATE RELATIONSHIP TYPE QUERIES
    def create_relation_rating():
        return ()