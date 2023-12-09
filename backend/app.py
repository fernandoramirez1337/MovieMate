from flask import Flask, jsonify, request, redirect, url_for
from neo4j_connect import Neo4jConnection
from neo4j_queries import Neo4jQueries

app = Flask(__name__)
neo4j_conn = Neo4jConnection("neo4j://localhost:7687", "neo4j", "4jneo")
neo4j_conn.connect()


#APIs
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'username' not in data:
        return jsonify({'error': 'Users name is required'}), 400
    
    user_name = data['username']
    if not neo4j_conn.execute_query(Neo4jQueries.get_user_by_name(),{"user_name":user_name}):
        return jsonify({'error': 'Invalid username'}), 401

    user = neo4j_conn.execute_query(Neo4jQueries.get_user_by_name(),{"user_name":user_name})
    print('User Data:', user[0])
    return user[0]

@app.route('/api/suggest_users', methods=['POST'])
def suggest_users():
    data = request.get_json()
    if 'username' not in data:
        return jsonify({'error': 'Users name is required'}), 400
    
    user_name = data['username']
    if not neo4j_conn.execute_query(Neo4jQueries.get_user_by_name(),{"user_name":user_name}):
        return jsonify({'error': 'Invalid username'}), 401
    
    list_sugg_users = neo4j_conn.execute_query(Neo4jQueries.get_suggested_users(),{"user_name":user_name,"limit": 8})
    return list_sugg_users

@app.route('/api/home/<int:user_id>')
def home(user_id):
    return jsonify({'message': f'Welcome to the home page, user {user_id}!'})

if __name__ == '__main__':
    app.run(debug=True)
