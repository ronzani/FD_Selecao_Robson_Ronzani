from sqlalchemy import create_engine

# Configurações de conexão
# TODO criar um arquivo .env
db_config = {
    'dbname': 'teste_fd',
    'user': 'postgres',
    'password': 'local123',
    'host': 'localhost',
    'port': 5432
}

# Cria a string de conexão
connection_string = f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"

# Cria a engine do SQLAlchemy
engine = create_engine(connection_string)