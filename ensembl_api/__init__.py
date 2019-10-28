# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

from sqlalchemy import create_engine
from flask_jsonpify import jsonify

# connection to db
db_connect = create_engine('mysql+mysqlconnector://anonymous@ensembldb.ensembl.org:3306/ensembl_website_97')

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)


class Genes(Resource):
    def get(self):
        conn = db_connect.connect()

        # argument parsing
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('species')
        args = parser.parse_args()

        gene_name = args['name']
        species = args['species']

        if len(gene_name) < 3:
            return {'message': 'too short gene name (minimum 3 characters)'}, 400

#        query_string = 'SELECT stable_id, display_label, species FROM gene_autocomplete WHERE locate({}, display_label) '.format(gene_name)


        if species:
            query = conn.execute('SELECT stable_id, display_label, species FROM gene_autocomplete WHERE locate(%s, display_label) AND species =%s',
                                 gene_name, species)
        else:
            query = conn.execute('SELECT stable_id, display_label, species FROM gene_autocomplete WHERE locate(%s, display_label) ',
                                 gene_name)

#        query = conn.execute(query_string)

        result = {'genes': [dict(zip(tuple(query.keys()),i)) for i in query.cursor]}
        return jsonify(result)

    def post(self):
        return {'message': 'POST request not permitted'}, 405
    
    def put(self):
        return {'message': 'PUT request not permitted'}, 405
    
    def patch(self):
        return {'message': 'PATCH request not permitted'}, 405



api.add_resource(Genes, '/genes')

#if __name__=='__main__':
#    app.run(port='5000')


