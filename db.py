import os
from tortoise import Tortoise


# DB_PATH = os.path.abspath(f"user.db")

# print("SQLite file path:", DB_PATH)

# DATABASE_URL = f"sqlite:///{DB_PATH}"


DB_URL = "postgresql://neondb_owner:npg_7t0mlTwduAis@ep-winter-meadow-a18p3t4g-pooler.ap-southeast-1.aws.neon.tech/neondb"

DB_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "user": "neondb_owner",
                "password": "npg_7t0mlTwduAis",
                "host": "ep-winter-meadow-a18p3t4g-pooler.ap-southeast-1.aws.neon.tech",
                "port": 5432,
                "database": "neondb",
                "ssl": True,  # Explicitly enabling SSL
            }
        }
    },
    "apps": {
        "models": {
            "models": ["models.user", "aerich.models"],
            "default_connection": "default",
        }
    }
}

# Asynchronous database initialization
async def init_db():
    await Tortoise.init(config=DB_CONFIG)
    await Tortoise.generate_schemas()  # Optional: Create schema for the models