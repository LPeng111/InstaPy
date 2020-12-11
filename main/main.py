from dbutils.dbutils import MysqlUtils
from schedule.Amrzs import Amrzs

# class myThread(threading.Thread):
#     def __init__(self, thread_id, ig_name, ig_passwd, ip, port):
#         threading.Thread.__init__(self)
#         self.thread_id = thread_id
#         self.ig_name = ig_name
#         self.ig_passwd = ig_passwd
#         self.ip = ip
#         self.port = port
#
#     def run(self):
#         do_action(self.ig_name, self.ig_passwd, self.ip, self.port)
#
#
# def do_action(ig_name, ig_passwd, ip, port):
#     amrzs = Amrzs(ig_name, ig_passwd, ip, port)
#     amrzs.daily_maintenance()


conn = MysqlUtils()
results = conn.get_all_ins_accounts()
i = 0
threads = []
for row in results:
    i += 1
    ig_name = row[0]
    if ig_name == 'keyontearameeu':
        continue
    ig_passwd = row[1]
    ip = row[2]
    port = row[3]

    amrzs = Amrzs(ig_name, ig_passwd, ip, port)
    amrzs.daily_maintenance()
    # amrzs.follow_and_like()

#     thread = myThread(i, ig_name, ig_passwd, ip, port)
#     threads.append(thread)
#
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
