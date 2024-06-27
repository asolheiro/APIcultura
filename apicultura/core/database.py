from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

<<<<<<< HEAD
DATABASE_URL = ''

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
=======
from apicultura.core.settings import Settings

settings = Settings()

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
>>>>>>> a694a75 (Primeira migração com alembic. Adicionando a tabela users)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
