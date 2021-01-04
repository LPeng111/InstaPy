from dbutils.dbutils import MysqlUtils
from schedule.Amrzs import Amrzs

# class MyThread(threading.Thread):
#     def __init__(self, thread_id, ig_name, ig_passwd, ip, port, workspace):
#         threading.Thread.__init__(self)
#         self.thread_id = thread_id
#         self.ig_name = ig_name
#         self.ig_passwd = ig_passwd
#         self.ip = ip
#         self.port = port
#         self.workspace = workspace
#
#     def run(self):
#         do_action(self.ig_name, self.ig_passwd, self.ip, self.port, self.workspace)
#
#
# lock = threading.Lock()
#
#
# def do_action(ig_name, ig_passwd, ip, port, workspace):
#     amrzs = Amrzs(ig_name=ig_name, ig_passwd=ig_passwd, proxy_ip=ip, proxy_port=port, workspace=workspace,
#                   headless=False)
#     amrzs.daily_maintenance()


conn = MysqlUtils()
results = conn.get_all_ins_accounts()
i = 0
threads = []
workspace = r'C:\Users\Administrator\InstaPy'
for row in results:
    i += 1
    ig_name = row[0]
    # if ig_name == 'keyontearameeu':
    #     continue
    ig_passwd = row[1]
    ip = row[2]
    port = row[3]

    Amrzs(ig_name=ig_name, ig_passwd=ig_passwd, proxy_ip=ip, proxy_port=port, workspace=workspace,
          headless=False).daily_maintenance()
    # amrzs.follow_and_like()

#     thread = MyThread(i, ig_name, ig_passwd, ip, port, workspace + str(i))
#     threads.append(thread)
#
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
