#企业微信机器人
from hashlib import md5
import requests,base64,random,string

url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d931f4aa-c756-4691-8133-cf64dc83c0d2"

class Robot():
    def __init__(self,url,name,image):
        self.url=url
        self.name=name
        self.image=image
    def introduce(self):
        self.sendmarkdown("# 自我介绍\nHi,我是%s\n我是一个**整天无所事事**的机器人"%self.name)
        self.sendimage(self.image)
        self.sendtext("这就是我，是不是很可爱呢awa？")
    def sendtext(self,msg):
        data={
            "msgtype": "text",
            "text": {
                "content": msg
            }
        }
        r=requests.post(self.url,json=data)
        return r.json()
    def sendmarkdown(self,content):
        data={
            "msgtype": "markdown",
            "markdown": {
                "content": content
            }
        }
        r=requests.post(self.url,json=data)
        return r.json()
    def sendimage(self,image):
        md5_v=md5(open(image,"rb").read()).hexdigest()
        image=base64.b64encode(open(image,"rb").read())
        data={
            "msgtype": "image",
            "image": {
                "base64":image.decode(),
                "md5": md5_v,
            }
        }
        r=requests.post(self.url,json=data)
        return r.json()

def test(robot):
    robot.sendtext("以下内容为测试")
    robot.sendmarkdown("### 测试markdown\n- 测试1\n- 测试2\n- 测试3")
    robot.sendtext("*********** Test Start ***********")
    for i in range(random.randint(1,10)):
        robot.sendtext("".join(random.choices(string.ascii_letters+string.digits,k=random.randint(10,20))))
    robot.sendtext("*********** Test End ***********")

yuki=Robot(url,"yuki","yuki.jpg")
#yuki.introduce()
#test(yuki)
yuki.sendmarkdown("**我生气了！！！**")
