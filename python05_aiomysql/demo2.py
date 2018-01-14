import asyncio
import aiomysql

pool = None
loop = asyncio.get_event_loop()

async def create_pool():
    sql = 'select iduser, username, userpassword from new_schema.user where iduser = 1'
    global pool 
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                           user='root', password='root',
                                           db='mysql', loop=loop,
                                           charset='utf8',)

async def close_pool():
    pool.close()
    await pool.wait_closed()

async def execute_sql():
    await create_pool()
    sql = 'select iduser, username, userpassword from new_schema.user where iduser = %s'
    for x in range(1,4):
        with (await pool) as conn:
            print('query start')
            # cur = await conn.cursor()
            cur = await conn.cursor(aiomysql.DictCursor)
            
            await cur.execute(sql % str(x))
            # print(cur.description)
            r = await cur.fetchall()
            print(r)
            print('query end')
    await close_pool()
    


loop.run_until_complete(execute_sql())