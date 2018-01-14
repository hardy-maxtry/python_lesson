import asyncio
import aiomysql

loop = asyncio.get_event_loop()


async def test_example(sql):
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                       user='root', password='root', db='mysql',
                                       loop=loop)

    cur = await conn.cursor(aiomysql.DictCursor)
    # await cur.execute("SELECT Host,User FROM user")
    # await cur.execute("SELECT * FROM new_schema.user")
    await cur.execute(sql)
    # await cur.execute("insert Into  new_schema.user (iduser,username,userpassword) values (3,'user3','pass3')")
    await conn.commit()
    # print(cur.description)
    r = await cur.fetchall()
    # print(r)
    await cur.close()
    conn.close()
    return r
    # 'select iduser, username, userpassword from new_schema.user where iduser = 1'

async def execute_sql():
    sql = 'select iduser, username, userpassword from new_schema.user where iduser = 1'
    r = await test_example(sql)
    print('query end')
    print(r)

loop.run_until_complete(execute_sql())

