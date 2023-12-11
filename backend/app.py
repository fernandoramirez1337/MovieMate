from flask import Flask, jsonify, redirect, render_template, request, url_for
from neo4j_connect import Neo4jConnection
from neo4j_queries import Neo4jQueries

app = Flask(__name__)
neo4j_conn = Neo4jConnection(
    "bolt://3.215.134.19:7687", "neo4j", "sister-focuses-spills"
)
neo4j_conn.connect()


# APIs
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Users name is required"}), 400

    user_name = data["username"]
    if not neo4j_conn.execute_query(
        Neo4jQueries.get_user_by_name(), {"user_name": user_name}
    ):
        return jsonify({"error": "Invalid username"}), 401

    user = neo4j_conn.execute_query(
        Neo4jQueries.get_user_by_name(), {"user_name": user_name}
    )
    print("User Data:", user[0])
    return user[0]


@app.route("/api/suggest_users", methods=["POST"])
def suggest_users():
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Users name is required"}), 400

    user_name = data["username"]
    if not neo4j_conn.execute_query(
        Neo4jQueries.get_user_by_name(), {"user_name": user_name}
    ):
        return jsonify({"error": "Invalid username"}), 401

    list_sugg_users = neo4j_conn.execute_query(
        Neo4jQueries.get_suggested_users(), {"user_name": user_name, "limit": 3}
    )
    return list_sugg_users


@app.route("/api/popular_movies", methods=["POST"])
def popular_movies():
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Users name is required"}), 400

    user_name = data["username"]
    if not neo4j_conn.execute_query(
        Neo4jQueries.get_user_by_name(), {"user_name": user_name}
    ):
        return jsonify({"error": "Invalid username"}), 401

    list_pop_movies = neo4j_conn.execute_query(
        Neo4jQueries.get_popular_movies(), {"limit": 6}
    )
    return list_pop_movies


@app.route("/api/rated_movies", methods=["POST"])
def rated_movies():
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Users name is required"}), 400

    user_name = data["username"]
    if not neo4j_conn.execute_query(
        Neo4jQueries.get_user_by_name(), {"user_name": user_name}
    ):
        return jsonify({"error": "Invalid username"}), 401

    list_rated_movies = neo4j_conn.execute_query(
        Neo4jQueries.get_movies_rated_by_user(), {"user_name": user_name, "limit": 6}
    )
    return list_rated_movies


def make_search_context_and_query_method(search_type, search_text):
    context = {"limit": 6}
    if search_type == "All":
        context["movie_title"] = search_text
        return [context, Neo4jQueries.get_movie_by_title()]

    if search_type == "Person":
        context["user_name"] = search_text
        return [context, Neo4jQueries.get_user_by_name()]

    # if search_type == "Community":
    #     context["community_name"] = search_text
    #     return [context, 1]

    if search_type == "Titles":
        context["movie_title"] = search_text
        return [context, Neo4jQueries.get_movie_by_title()]

    if search_type == "Celebs":
        context["celebrity_name"] = search_text
        return [context, Neo4jQueries.get_celebrities_by_name()]

    if search_type == "Genre":
        context["genre_name"] = search_text
        return [context, Neo4jQueries.get_movies_by_genre()]


@app.route("/api/search", methods=["POST"])
def search(user_id):
    data = request.get_json()
    search_text = data["search_text"]
    search_type = data["search_type"]

    [context, query] = make_search_context_and_query_method(search_type, search_text)

    query_result = neo4j_conn.execute_query(query, context)
    return query_result


@app.route("/api/home/<int:user_id>")
def home(user_id):
    return jsonify({"message": f"Welcome to the home page, user {user_id}!"})


if __name__ == "__main__":
    app.run(debug=True)
