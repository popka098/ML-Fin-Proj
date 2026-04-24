from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./db.sqlite3"

engine = create_async_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False,
    },
)

AsyncSessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)