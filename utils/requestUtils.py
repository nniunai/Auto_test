import requests




def request_get(url,headers):
    r = requests.get(url=url,headers=headers)

    code =r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text

    res = dict()
    res["code"] = code
    res["body"] = body

    return res


class Requsts():


    def requests_api(self,url,method="get",data=None,json=None,headers=None,cookies=None):

        if method == "get":
            r= requests.get(url=url,data=data,json=json,headers=headers,cookies=cookies)
        elif method== "post":
            r =requests.post(url=url,data=data,json=json,headers=headers,cookies=cookies)

        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        res = dict()
        res["code"] = code
        res["body"] = body

        return res

    def get(self,url,**kwargs):
        return self.requests_api(url=url,method="get",**kwargs)



    def post(self,url,**kwargs):
        return self.requests_api(url=url,method="post",**kwargs)




if __name__ == '__main__':

    re = Requsts()
    data= {"password": "hd.123456","username": "huang123456"}
    #rp=re.post("http://106.14.225.213:8000/xc/login",data=data)
    rp = re.get("http://106.14.225.213")
    print(rp)

    pass