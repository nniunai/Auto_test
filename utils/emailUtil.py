from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from config.conf import ConfigYaml

data = ConfigYaml().get_email_info()




class Email():

    def __init__(self,smtp_addr,username,password,recv,title,content=None,file=None):

        self.smtp_addr = smtp_addr
        self.username = username
        self.password = password
        self.recv =recv
        self.title =title
        self.content = content
        self.file = file



    def send_mail(self):

        msg = MIMEMultipart()

        msg.attach(MIMEText(self.content,_charset="utf-8"))
        # 标题
        msg["Subject"] = self.title
        # 发送者账户
        msg["From"] = self.username
        # 接受者
        msg["To"] = self.recv


        # 附件
        if self.file:
            att = MIMEText(open(self.file).read())
            # 设置内容类型
            att["Content-Type"]="application/octet-stream"
            # 设置附件头
            att["Content-Disposition"] = "attachment;filename='%s'" %self.file
            # 将内容加到邮件里面
            msg.attach(att)

        # 登录服务器
        self.smtp = smtplib.SMTP(host=self.smtp_addr,port=25)
        self.smtp.login(self.username,self.password)

        # 发送邮件
        self.smtp.sendmail(self.username,self.recv,msg.as_string())

if __name__ == '__main__':
    smtp_addr= data["smtpserver"]
    username = data["username"]
    password = data["password"]
    recv= data["receiver"]
    print(smtp_addr,username,password,recv)

    email = Email(smtp_addr,username,password,recv,"test")
    email.send_mail()