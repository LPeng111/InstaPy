import pymysql


class MysqlUtils():
    def __init__(self):
        self.host = 'xxx'
        self.user = 'xxx'
        self.password = 'xxx.'
        self.port = 3306
        self.database = 'CrawlerDBStore'

    def get_all_ins_accounts(self):
        sql = "SELECT username, password, ip, port, proxy_username, proxy_password FROM SS_INS_ACCOUNTS WHERE is_locked = 0"
        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port,
                                     database=self.database, charset='utf8')
        cursor = connection.cursor()

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        except:
            print("Error: unable to fetch data")
        finally:
            cursor.close()
            connection.close()

    def update_cookie(self, cookie):
        sql = "UPDATE SS_INS_ACCOUTNS SET cookie = '{}'".format(cookie)

        connection = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port,
                                     database=self.database, charset='utf8')
        cursor = connection.cursor()
        try:
            cursor.execute(sql)
            connection.commit()
        except:
            connection.rollback()
        finally:
            cursor.close()
            connection.close()

# conn = MysqlUtils()
# conn.get_all_ins_accounts()
