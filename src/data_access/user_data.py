from data_config import simple_conn_pool
from models.users import User 
def get_user_by_id(id):
    ps_connection = simple_conn_pool.getconn()
    if (ps_connection):
        ps_cursor = ps_connection.cursor()
        query = "SELECT * FROM users WHERE id= %s;"
        ps_cursor.execute(query,(id, ))
        user_tuple = ps_cursor.fetchone()
        ps_cursor.close()
        # release the connection to pool after completion of this method 
        simple_conn_pool.putconn(ps_connection)
        return user_tuple

