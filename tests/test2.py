from schedule.Amrzs import Amrzs

ig_name = 'keyontearameeu'
ig_passwd = 'xxx.'
ip = '172.15.104.201'
port = '33003'

Amrzs(ig_name=ig_name, ig_passwd=ig_passwd, proxy_ip=ip, proxy_port=port,
      workspace=r'C:\Users\Administrator\InstaPy', headless=False).daily_maintenance()
