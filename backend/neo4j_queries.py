# neo4j_queries.py


class Neo4jQueries:
    # SIMPLE GET NODE TYPE QUERIES
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

    # SIMPLE GET RELATIONSHIP TYPE QUERIES
    @staticmethod
    def get_R_rated():
        return (
            "MATCH (m:Movie {title: $movie_title})-[r:RATED]-(u:User {name: $user_name}) "
            "RETURN { movie: m.title, user: u.name, rating: r.rating} AS rating"
        )

    # COMPLEX GET NODE TYPE QUERIES
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

    # SEARCH QUERIES
    @staticmethod
    def get_celebrities_by_name():
        return (
            "MATCH (m:Person) "
            "WHERE toLower(m.name) CONTAINS toLower($celebrity_name) "
            "RETURN m.name, m.poster"
            "LIMIT $limit"
        )

    # @staticmethod
    # def get_community_by_name():

    @staticmethod
    def get_movies_by_genre():
        return (
            "MATCH (g:Genre)<-[:IN_GENRE]-(m:Movie) "
            "WHERE toLower(g.name) STARTS WITH toLower($genre_name) "
            "RETURN m.title, m.poster"
            "LIMIT $limit"
        )

    # CREATE NODE TYPE QUERIES
    @staticmethod
    def create_node_user():
        return ()

    # CREATE RELATIONSHIP TYPE QUERIES
    def create_relation_rating():
        return ()
