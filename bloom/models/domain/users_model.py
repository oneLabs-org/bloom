from sqlalchemy import Column, BIGINT, VARCHAR
from ...db.repositories.database_setup import Base


class Test(Base):
    __tablename__ = "tests"
    test_id = Column(BIGINT, primary_key=True)
    test_name = Column(VARCHAR(40), nullable=False)
    test_email = Column(VARCHAR(30), nullable=False)


class Test2(Base):
    __tablename__ = "nontests"
    test_id_one = Column(BIGINT, primary_key=True)
    test_name_one = Column(VARCHAR(40), nullable=False)
    test_email_one = Column(VARCHAR(30), nullable=False)
