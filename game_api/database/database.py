from sqlmodel import SQLModel,create_engine #import cac thanh phan can thiet tu thu vien SQLModel de lam viec voi csdl va tao doi tuong du lieu

sqlite_file_name = "database.db" #ten tep csdl SQLite
sqlite_url = f"sqlite:///{sqlite_file_name}" #tao URL ket noi SQLite  sqlite:/// va duong dan

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)#tao ket noi thao tac voi csdl va thuc thi lenh DB(echo =true)


def create_db_and_tables(): #tao bang csdl
    SQLModel.metadata.create_all(engine)