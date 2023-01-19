import asyncio
import asyncpg
from data import config



class Database:

    def __init__(self):
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(**LOG_PG)
        )

    def __init__(self):
        loop = asyncio.get_event_loop()
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PGUSER,
                database=config.DBNAME,
                password=config.PGPASSWORD,
                host=config.DBPORT,
                loop=loop
        )

#    def __init__(self):
 #       loop = asyncio.get_event_loop()
  #      self.pool: asyncio.pool.Pool = loop.run_until_complete(
     #       asyncpg.create_pool(
      #          user=config.PGUSER,
       #         database=config.DBNAME,
        #        password=config.PGPASSWORD,
         #       host=config.DBPORT,
          #      loop=loop
           # )
        #)





    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters, start=1)
        ])

    async def create_table_users(self):
        await self.pool.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INT NOT NULL,
        phone_number VARCHAR (255) NOT NULL,
        CONSTRAINT "user_pk" PRIMARY KEY ("id"))
        WITH (
        OIDS=FALSE
        ); """)
    async def add_user(self, id, phone_number):

        sql = "INSERT INTO users (id, phone_number) VALUES ($1, $2)"
        try:
            await self.pool.execute(sql, id, phone_number)
        except asyncpg.exceptions.UniqueViolationError:
            pass

    async def get_users(self):
        sql="SELECT id, phone_number FROM users"
        try:
            async with self.pool.acquire() as conn:
                all=await conn.fetch(sql)
                answer=[]
                for i in all:
                    answer.append([i[0], i[1]])
                return answer
        except asyncpg.exceptions.UniqueViolationError:
            pass