from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from infrastructure.config.settings import settings

engine = create_engine(settings.DATABASE_URI, echo=True, pool_size=20)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()