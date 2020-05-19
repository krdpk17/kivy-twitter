from neo4jintf.docker.features import fetcher_query
import os
import pdb
def test_query_insert(filepath):
    print("filepath is {}".format(filepath))
    print("DLLLLLL1") 
    os.environ["ENV_FILEPATH"]=filepath
    status = fetcher_query.test_query_insert()
    print("DLLLLLL1_")
    return status
    
