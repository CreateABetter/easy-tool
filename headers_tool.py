'''
Main for orderly format，from software Fidder to copy headers, and transfer it to orderliness format of Python

headers is important for web crawler.

maybe this Python script can easy your work.



author:Forrest Gump

'''



type_four_text = '''
GET https://mp.weixin.qq.com/s?__biz=MjM5MjA1NTM2MA==&mid=2652958868&idx=2&sn=70bfaa9b69707f25e5c99c3f4f3dbd15&chksm=bd7879bb8a0ff0ad8fc3d04a260f944decbf06d4e4b1bcb8f30d6723bf14fca9fe22c5d0d038&scene=0&xtrack=1&from=singlemessage&ascene=1&devicetype=android-19&version=26060736&nettype=WIFI&abtest_cookie=BAABAAoACwANABQABAAjlx4AWZkeAIqZHgCMmR4AAAA%3D&lang=zh_CN&pass_ticket=qJfxOFvti%2FxBqBBifpQJ8%2B8Z2kob%2BoyZQBisJN%2BO4TVP8oaTetWt3iIJJc3ht30l&wx_header=1 HTTP/1.1
Host: mp.weixin.qq.com
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
x-wechat-uin: NTMwOTA3ODQ0
x-wechat-key: bc1f43870fefa3ad5fbee26ad8e4137601281a71dd7a3f497f512101542cfb0a3d4bf8f083420c14cc4244ce8d35c9f3490dcd0c126de116831832eb193f9feffd7f4f6f399649af553766c65ae9e75e
User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; MI 6  Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 MicroMessenger/6.6.7.1321(0x26060736) NetType/WIFI Language/zh_CN
Accept-Encoding: gzip,deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: rewardsn=; wxuin=530907844; devicetype=android-19; version=26060736; lang=zh_CN; pass_ticket=qJfxOFvti/xBqBBifpQJ8+8Z2kob+oyZQBisJN+O4TVP8oaTetWt3iIJJc3ht30l; wap_sid2=CMSFlP0BElxEUW1OaWlfMG5Rb2lMOFItWG0tVEI0Z1YwTGQ2U1d5c2czM2NUTm13cTRzTVlqLVQ3eXFoeHdCUjVvckRYUGw1czZhdHBSdmxHT0NFdEtXbU13Y1MwdFlEQUFBfjCC8I/fBTgNQAE=; wxtokenkey=777
X-Requested-With: com.tencent.mm


HTTP/1.1 200 OK
Last-Modified: Thu, 8 Nov 2018 17:03:05 +0800
Expires: Thu, 8 Nov 2018 17:11:25 +0800
Content-Security-Policy: script-src 'self' 'unsafe-inline' 'unsafe-eval' http://*.qq.com https://*.qq.com http://*.weishi.com https://*.weishi.com 'nonce-176462304';style-src 'self' 'unsafe-inline' http://*.qq.com https://*.qq.com;object-src 'self' http://*.qq.com https://*.qq.com;font-src 'self' data: http://*.qq.com https://*.qq.com http://fonts.gstatic.com https://fonts.gstatic.com;frame-ancestors 'self' http://wx.qq.com https://wx.qq.com http://wx2.qq.com https://wx2.qq.com  http://wx8.qq.com https://wx8.qq.com http://web.wechat.com https://web.wechat.com http://web1.wechat.com https://web1.wechat.com http://web2.wechat.com https://web2.wechat.com http://sticker.weixin.qq.com https://sticker.weixin.qq.com http://bang.qq.com https://bang.qq.com http://app.work.weixin.qq.com https://app.work.weixin.qq.com http://work.weixin.qq.com https://work.weixin.qq.com;report-uri https://mp.weixin.qq.com/mp/fereport?action=csp_report
Content-Type: text/html; charset=UTF-8
Cache-Control: public, max-age=500
RetKey: 14
LogicRet: 0
Content-Type: text/html; charset=UTF-8
Strict-Transport-Security: max-age=0
Set-Cookie: malluin=NTMwOTA3ODQ0; Path=/bizmall/; HttpOnly
Set-Cookie: mallkey=bc1f43870fefa3ad5fbee26ad8e4137601281a71dd7a3f497f512101542cfb0a3d4bf8f083420c14cc4244ce8d35c9f3490dcd0c126de116831832eb193f9feffd7f4f6f399649af553766c65ae9e75e; Path=/bizmall/; HttpOnly
Set-Cookie: malluin=EXPIRED; Path=/; Expires=Wed, 07-Nov-2018 09:03:05 GMT; HttpOnly
Set-Cookie: mallkey=EXPIRED; Path=/; Expires=Wed, 07-Nov-2018 09:03:05 GMT; HttpOnly
Set-Cookie: rewardsn=; Path=/
Set-Cookie: payforreadsn=EXPIRED; Path=/; Expires=Wed, 07-Nov-2018 09:03:05 GMT; HttpOnly
Set-Cookie: wxtokenkey=777; Path=/; HttpOnly
Set-Cookie: wxuin=530907844; Path=/; HttpOnly
Set-Cookie: devicetype=android-19; Path=/
Set-Cookie: version=26060736; Path=/
Set-Cookie: lang=zh_CN; Path=/
Set-Cookie: pass_ticket=qJfxOFvti/xBqBBifpQJ8+8Z2kob+oyZQBisJN+O4TVP8oaTetWt3iIJJc3ht30l; Path=/; HttpOnly
Set-Cookie: wap_sid2=CMSFlP0BElxYdmhDdGRVdHhvNHFMUmVhRXQ2UzJsdXdqZWRmbzI3OEo5OEFKR0JJLXVLT2ptM2NQV0hjREJaREYxTUZvbGdoM0lEdGszWWVZVUpqOWRKa1dKRktaTllEQUFBfjDJ94/fBTgNQAE=; Path=/; HttpOnly
MMLAS-VERIFYRESULT: CAE=
Connection: keep-alive
Content-Length: 119440



------------------------------------------------------------------

POST https://mp.weixin.qq.com/mp/getappmsgad?f=json&mock=&uin=777&key=777&pass_ticket=qJfxOFvti%25252FxBqBBifpQJ8%25252B8Z2kob%25252BoyZQBisJN%25252BO4TVP8oaTetWt3iIJJc3ht30l&wxtoken=777&devicetype=android-19&clientversion=26060736&appmsg_token=982_OwZrr5v402zk9ltCt78JiT5Py9dG0_BWnCksDvM9_htrvODRzUSjpCBK2zVMY4ZzbqkE_anuZn6OM18F&x5=0&f=json HTTP/1.1
Host: mp.weixin.qq.com
Connection: keep-alive
Content-Length: 851
Origin: https://mp.weixin.qq.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; MI 6  Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 MicroMessenger/6.6.7.1321(0x26060736) NetType/WIFI Language/zh_CN
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept: */*
Referer: https://mp.weixin.qq.com/s?__biz=MjM5MjA1NTM2MA==&mid=2652958868&idx=2&sn=70bfaa9b69707f25e5c99c3f4f3dbd15&chksm=bd7879bb8a0ff0ad8fc3d04a260f944decbf06d4e4b1bcb8f30d6723bf14fca9fe22c5d0d038&scene=0&xtrack=1&from=singlemessage&ascene=1&devicetype=android-19&version=26060736&nettype=WIFI&abtest_cookie=BAABAAoACwANABQABAAjlx4AWZkeAIqZHgCMmR4AAAA%3D&lang=zh_CN&pass_ticket=qJfxOFvti%2FxBqBBifpQJ8%2B8Z2kob%2BoyZQBisJN%2BO4TVP8oaTetWt3iIJJc3ht30l&wx_header=1
Accept-Encoding: gzip,deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: rewardsn=; wxtokenkey=777; wxuin=530907844; devicetype=android-19; version=26060736; lang=zh_CN; pass_ticket=qJfxOFvti/xBqBBifpQJ8+8Z2kob+oyZQBisJN+O4TVP8oaTetWt3iIJJc3ht30l; wap_sid2=CMSFlP0BElxYdmhDdGRVdHhvNHFMUmVhRXQ2UzJsdXdqZWRmbzI3OEo5OEFKR0JJLXVLT2ptM2NQV0hjREJaREYxTUZvbGdoM0lEdGszWWVZVUpqOWRKa1dKRktaTllEQUFBfjDJ94/fBTgNQAE=


HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Cache-Control: no-cache, must-revalidate
RetKey: 14
LogicRet: 0
Strict-Transport-Security: max-age=0
Content-Encoding: deflate
Set-Cookie: wxtokenkey=777; Path=/; HttpOnly
Connection: keep-alive
Content-Length: 2187



------------------------------------------------------------------



'''


class work():

    def __init__(self):
        configue = 3
        #if configue = 1 It will campare different from self.headers_a and  self.headers b
        #if configue = 2  It will tranisfer code from format of HTML or Fiddler to dictionary format code of Python
        #if configue = 3 It will compare parameter from self.url_a and self.url_b
        #if configue = 4 It will compare Fiddler text that inculde url、headers 、response of request twice or more. output format code and print(relationship with the time_request and next request ) ,ease for web crawler.



        self.headers_a = """


Host: api.amemv.com
Connection: keep-alive
Cookie: qh[360]=1; install_id=48599881817; ttreq=1$078e3a30aa611cb95d6de56ee1f5ad4ca8ff979f; odin_tt=8fee6b9384befff1bab978d2f776fb93e42f7d1f63ddd9c3753e0a25d4721e8abec0c761ad67d8aa39405e5367fe9012; sid_guard=49bd141d50aac7b9eb8f71fde2688b70%7C1541645242%7C5184000%7CMon%2C+07-Jan-2019+02%3A47%3A22+GMT; uid_tt=d121483b945d48b8aabd0e1e3a503c18; sid_tt=49bd141d50aac7b9eb8f71fde2688b70; sessionid=49bd141d50aac7b9eb8f71fde2688b70
Accept-Encoding: gzip
X-SS-REQ-TICKET: 1541645294703
X-Tt-Token: 0049bd141d50aac7b9eb8f71fde2688b703e0ef8c6ca84b31956aa9ad4f9bf73417b58c8a0bd4eb91ae9c9187753307a802c
sdk-version: 1
X-SS-TC: 0
User-Agent: com.ss.android.ugc.aweme/310 (Linux; U; Android 4.4.2; zh_CN; HUAWEI MLA-AL10; Build/HUAWEIMLA-AL10; Cronet/58.0.2991.0)














              
                    """

        self.headers_b = '''

Host: mp.weixin.qq.com
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
x-wechat-uin: NTMwOTA3ODQ0
x-wechat-key: a2364b934e76f3a766b260d34ac6701005a438e3ec9b2b39d18b691c3e963890c4e49c48456d6a3695391abc83e66c6126f2634bedd125dcfee6d941f2d95e20a56fba48c4a624627311d0e26ef031eb
User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 MicroMessenger/6.6.7.1321(0x26060736) NetType/WIFI Language/zh_CN
Accept-Encoding: gzip,deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: rewardsn=; wxuin=530907844; devicetype=android-19; version=26060736; lang=zh_CN; pass_ticket=f1SgB82buiYbhtINO62qxMVokr3B/nwTTFXwbxFv0V95htTNLv4j2h97S6VUyTfC; wap_sid2=CMSFlP0BElxhSU9ZVm5hLU9lekNRdFVmTVFDSEdEWjVlOXliSlNKRi1xSGoycXpEOFZxckFXQ1dUd0xfN1BHNy1la0JYSG15ZUlLNHRBTzRxTEx5ZnJjNk5nTGpEdFFEQUFBfjCMteTeBTgNQAE=; wxtokenkey=777
X-Requested-With: com.tencent.mm









               '''

        self.url_a = '''
http://mp.weixin.qq.com/s?__biz=MjM5MjA1NTM2MA==&mid=2652958868&idx=4&sn=82d12b14273c836358cbd92d1a7b8ed5&chksm=bd7879bb8a0ff0ad0674bb6bd6a0339708e2b58eab288546dea70b019ffe8b418fd54469b459&scene=0&xtrack=1#rd
        '''

        self.url_b = '''
https://mp.weixin.qq.com/s?__biz=MjM5MjA1NTM2MA==&mid=2652958868&idx=2&sn=70bfaa9b69707f25e5c99c3f4f3dbd15&chksm=bd7879bb8a0ff0ad8fc3d04a260f944decbf06d4e4b1bcb8f30d6723bf14fca9fe22c5d0d038&scene=0&xtrack=1&from=singlemessage&ascene=1&devicetype=android-19&version=26060736&nettype=WIFI&abtest_cookie=BAABAAoACwANABQABAAjlx4AWZkeAIqZHgCMmR4AAAA%3D&lang=zh_CN&pass_ticket=qJfxOFvti%2FxBqBBifpQJ8%2B8Z2kob%2BoyZQBisJN%2BO4TVP8oaTetWt3iIJJc3ht30l&wx_header=1
        '''

        if configue == 1:

            self.transform()
            self.comparision()
            self.output()
        elif configue ==2:
            self.write_python_form()

        elif configue ==3:
            self.get_parameter_comparision()
        elif configue == 4:
            self.four_type_compose()
        else:
            self.cookie_analyze()


    def get_parameter_comparision(self):
        _a_list = self.url_a.replace(' ','').split('&')
        _b_list = self.url_b.replace(' ','').split('&')
        print('a not in b:')
        for a in _a_list:

            if a not in _b_list:
                print(a)
        print('b not in a:')
        for b in _b_list:

            if b not in _a_list:
                print(b)



    def transform(self):
        try:
            self.headers_a_Cookie = [a for a in self.headers_a.replace(' ','').split("\n") if a != 0 if "Cookie" in a if a !=''][0].split(';')
        except:
            self.headers_a_Cookie = ''
        self.headers_a = [a.replace('','') for a in self.headers_a.replace("	","").replace(' ','').split("\n") if a != 0 if "Cookie" not in a]


        try:
            self.headers_b_Cookie = [a for a in self.headers_b.replace(' ','').split("\n") if a != 0 if "Cookie" in a if a != ''][0].split(';')
        except:
            self.headers_b_Cookie = ''
        self.headers_b = [a for a in self.headers_b.replace("	","").replace(' ','').split("\n") if a != 0 if "Cookie" not in a]

    def comparision(self):

        self.different_headers_onlya = set(self.headers_a).difference(set(self.headers_b))#在a中但不在b中
        self.different_headers_onlyb = set(self.headers_b).difference(set(self.headers_a))#在b中但不在a中

        self.different_headers_Cookie_onlya = set(self.headers_a_Cookie).difference(set(self.headers_b_Cookie))#在a中但不在b中
        self.different_headers_Cookie_onlyb = set(self.headers_b_Cookie).difference(set(self.headers_a_Cookie))#在b中但不在a中


    def write_python_form(self):
        """将headers文档，转化成python字典的那种录入格式"""
        self.headers_a = [a for a in self.headers_a.replace(" ","").split("\n") if a != ""]
        print("headers_a","\n")
        for a in self.headers_a:
            if self.headers_a.index(a) == len(self.headers_a)-1:
                #如果是最后一个，最后输出不加 逗号
                a_find = a.find(":")
                print("'"+ a[0:a_find]+ "':'"+ a[a_find+1:]+"'")
            else:
                a_find = a.find(":")
                print("'" + a[0:a_find] + "':'" + a[a_find + 1:] + "',")

    def cookie_analyze(self):
        cookie = [a for a in self.headers_a.replace(" ", "").split("\n") if  "Cookie" in a][0]
        cookie = cookie.split(';')
        for a in cookie:
            print('\n')
            print(a)


    def output(self):
        print("different_headers_onlya:","\n")
        for a in self.different_headers_onlya:
            print("                         ",a,"\n")

        print("different_headers_onlyb:","\n")
        for a in self.different_headers_onlyb:
            print("                         ",a,"\n")

        print("different_headers_Cookie_onlya:","\n")
        for a in self.different_headers_Cookie_onlya:
            print("                         ",a, "\n")

        print("different_headers_Cookie_onlyb:","\n")
        for a in self.different_headers_Cookie_onlyb:
            print("                         ",a, "\n")

    def four_type_compose(self):
        global type_four_text
        data = [a for a in type_four_text.split('------------------------------------------------------------------') if'GET' in a or 'POST' in a]
        def compose(first_request_text,second_request_text,whats_the_ranking):
            first_request,first_request_response = [a for a in first_request_text.split('\n\n') if len(a)>0]
            second_request,second_request_response = [a for a in second_request_text.split('\n\n') if len(a)>0]
            first_request_url = [a for a in first_request.split('\n') if 'GET'in a or 'POST' in a or 'https' in a or 'http' in a ][0].split(' ')[:2]
            first_request_headers_str = [a for a in first_request.split('\n') if first_request_url[1] not in a and len(a)>0]
            first_request_headers = {}
            for a in [a.split(":") for a in first_request_headers_str]:
                if a[0] == "Cookie":
                    first_request_headers_cookie = "\nCookie:\n       " + a[1].replace(';', '\n     ')
                else:
                    first_request_headers_cookie = ""
                first_request_headers[a[0]] = a[1].replace(" ","").replace(' ','')


            second_request_url = [a for a in second_request.split('\n') if 'GET' in a or 'POST' in a or 'https' in a or 'http' in a][0].split(' ')[:2]
            second_request_url_variate_list = [a.split('=') for a in second_request_url[1].split("&") if a.split('=')[1] in first_request_response]
            second_request_headers_str = [a for a in second_request.split('\n') if second_request_url[1] not in a and len(a) > 0]
            second_request_headers_str = [a for a in second_request.split('\n') if second_request_url[1] not in a and len(a) > 0]
            second_request_headers = {}
            for a in [a.split(":") for a in second_request_headers_str]:
                if a[1] in first_request_response:
                    second_request_headers[a[0]] = a[1].replace(" ","").replace(' ','')+"——变量——————————————————————————————————————"

                else:
                    if a[0] == "Cookie":
                        second_request_headers_cookie = "\nCookie:\n    " + ";".join([a + "——变量————————————" for a in a[1].split(';') if a in first_request_response]).replace(';', '\n     ')
                        cookie = a[1]
                        for b in a[1].split(';'):
                            if b in first_request_response:
                                cookie = cookie.replace(b,b.split("=")[0].replace(" ","")+"={"+b.split("=")[0].replace(' ','')+"}")
                        second_request_headers[a[0]] = cookie
                    else:
                        second_request_headers[a[0]] = a[1].replace(" ","").replace(' ','')
                
            print(" \nurl:{}\n     ".format(first_request_url[0]),first_request_url[1],"\n","\nheader:\n    ",str(first_request_headers).replace('\',',"\',\n    "),"\n",first_request_headers_cookie,"\n","\nfirst_request_response:\n",first_request_response.replace('\n','\n      '))

            print('第{}个请求:'.format(whats_the_ranking+1),"="*100)
            print(" \nurl:{}\n     ".format(second_request_url[0]),second_request_url[1],"\n      url variate aready exist in the response that of the first request \n    ",str(second_request_url_variate_list).replace('],',']\n    '),"\n","\nheader:\n    ",str(second_request_headers).replace('\',',"\',\n    "),"\n",second_request_headers_cookie,"\n","\nresponse:\n",second_request_response.replace('\n','\n      '))



        for a in range(len(data)-1):
            compose(data[a],data[a+1],a+1)





work()