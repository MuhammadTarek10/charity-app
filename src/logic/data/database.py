import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Query


class Database:
    def __init__(self, db_url):
        self.engine = sa.create_engine(db_url)
        self.connection = self.engine.connect()

    def get_connection(self) -> sa.engine.Connection:
        return self.connection

    def get_engine(self) -> sa.engine.Engine:
        return self.engine

    def get_metadata(self) -> sa.MetaData:
        return sa.MetaData(bind=self.engine)

    def get_session(self) -> sessionmaker:
        return sessionmaker(bind=self.engine)()

    def create_tables(self, metadata: sa.MetaData) -> None:
        metadata.create_all(self.engine)

    def drop_tables(self, metadata) -> None:
        metadata.drop_all(self.engine)

    def get_by_id(self, table_name: str, id: int) -> Query:
        return self.get_session().query(table_name).filter_by(id=id).first()

    def get_all(self, table_name: str):
        return self.get_session().query(table_name).all()

    def update(self, table_name: str, id: int, data: dict) -> None:
        session = self.get_session()
        session.query(table_name).filter_by(id=id).update(data)
        session.commit()

    def insert(self, table_name: str, data: dict) -> None:
        session = self.get_session()
        session.add(table_name(**data))
        session.commit()

    def delete(self, table_name: str, id: int) -> None:
        session = self.get_session()
        session.query(table_name).filter_by(id=id).delete()
        session.commit()

    def close(self) -> None:
        self.connection.close()
        self.engine.dispose()

    def __enter__(self) -> "Database":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
