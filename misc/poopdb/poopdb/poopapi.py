import os

path = '/opt/poopdb/'

# funcs
def db_path(db):
    return path + db

def df_path(db, df):
    return path + db + '/' + df

def db_exist(db):
    return db in [d for d in os.listdir(path)
        if os.path.isdir(os.path.join(path, d))]

def df_exist(db, df):
    return df in [f for f in os.listdir(db_path(db))
        if os.path.isfile(os.path.join(db_path(db), f))]

def is_data(df):
    return df.endswith('.data')

def process(data_line):
    try:
        li = a, b = data_line.split(':')
        return True, a.strip() + ':' + b.strip()
    except:
        return False, ''

# api
# query available databases (show dbs)
def db_avail():
    return [d for d in os.listdir(path)
        if os.path.isdir(os.path.join(path, d))]

# query selected database (show datas)
def db_query(db):
    if db_exist(db):
        database_path = db_path(db)
        return os.listdir(database_path)

# query data file (read foo.data)
def df_query(db, df):
    if df_exist(db, df):
        data_path = df_path(db, df)
        with open(data_path, 'r') as f:
            return f.read()

# create database (use foo.data, if dont exist)
def db_create(db):
    if not db_exist(db):
        os.mkdir(db)

# insert data (add foo.data & write foo.data) ?
def insert(db, df, k, v):
    if db_exist(db) and is_data(df):
        data_path = df_path(db, df)
        valid, data_line = process(str(k) + ':' + str(v))
        if valid:
            with open(data_path, 'a') as f:
                f.write(data_line + '\n')

# delete data file (delete foo.data) ??
def delete(db, df):
    if df_exist(db, df):
        data_path = df_path(db, df)
        os.remove(data_path)
