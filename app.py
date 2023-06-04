import argparse
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import pandas as pd
from configparser import ConfigParser
from helper.handleJoin import HandleJoin

app = Flask(__name__)

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str)
args = parser.parse_args()

# reading and configuring configurations of flask app from constants.ini file
config = ConfigParser()
config.read(args.config)

# configuring JWT token for access management in flask
app.config['JWT_SECRET_KEY'] = config.get('APP', 'SECRET_KEY')
jwt = JWTManager(app)


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    # Validate the credentials (e.g., check against a database)
    try:
        if username == 'admin' and password == 'PasswordBarrier':
            # Create a new access token
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({'error': 'Invalid username or password'}), 401

    except Exception as e:
        return jsonify({'error': 'contact admin with this error: ' + str(e)}), 401


@app.route('/joinDataframes', methods=['POST'])
@jwt_required()
def join_dataframes():
    left_dataframe_data = request.json.get('leftDataframe')
    right_dataframe_data = request.json.get('rightDataframe')
    join_type = request.json.get('joinType')
    joining_keys = request.json.get('joiningKeys')

    handle_join = HandleJoin(left_dataframe_data, right_dataframe_data, join_type, joining_keys)

    return handle_join.dataframe_join()



if __name__ == '__main__':
    app.run(debug=config.getboolean('APP', 'DEBUG'),
            port=int(config.get('APP', 'PORT')))
