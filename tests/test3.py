from schedule.Amrzs import Amrzs

ig_name = 'wixjsuttles23017'
ig_passwd = 'xxx.'
ip = '172.15.104.201'
port = '33002'

Amrzs(ig_name=ig_name, ig_passwd=ig_passwd, proxy_ip=ip, proxy_port=port,
      workspace=r'C:\Users\Administrator\InstaPy2', headless=True).daily_maintenance()
