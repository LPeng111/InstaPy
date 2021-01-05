from schedule.Amrzs import Amrzs

ig_name = 'zhejiang20'
ig_passwd = 'xxx.'
ip = '172.15.104.201'
port = '33001'

Amrzs(ig_name=ig_name, ig_passwd=ig_passwd, proxy_ip=ip, proxy_port=port,
      workspace=r'C:\Users\Administrator\InstaPy1', headless=True).daily_maintenance()
