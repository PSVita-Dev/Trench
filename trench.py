import requests
import base64 #their "token" system lmfao

if __name__ == "__main__":
    print("""'########:'########::'########:'##::: ##::'######::'##::::'##:                                                                 
... ##..:: ##.... ##: ##.....:: ###:: ##:'##... ##: ##:::: ##:                                                                 
::: ##:::: ##:::: ##: ##::::::: ####: ##: ##:::..:: ##:::: ##:                                                                 
::: ##:::: ########:: ######::: ## ## ##: ##::::::: #########:                                                                 
::: ##:::: ##.. ##::: ##...:::: ##. ####: ##::::::: ##.... ##:                                                                 
::: ##:::: ##::. ##:: ##::::::: ##:. ###: ##::: ##: ##:::: ##:                                                                 
::: ##:::: ##:::. ##: ########: ##::. ##:. ######:: ##:::: ##:                                                                 
:::..:::::..:::::..::........::..::::..:::......:::..:::::..::                                                                 
'########::'##:::'##:::::::'###::::'########:'##::::'##:'########::'####::'######::'####:'##::: ##:'##::::'##:'####:'########::
 ##.... ##:. ##:'##:::::::'## ##:::..... ##:: ##:::: ##: ##.... ##:. ##::'##... ##:. ##:: ###:: ##: ###::'###:. ##:: ##.... ##:
 ##:::: ##::. ####:::::::'##:. ##:::::: ##::: ##:::: ##: ##:::: ##:: ##:: ##:::..::: ##:: ####: ##: ####'####:: ##:: ##:::: ##:
 ########::::. ##:::::::'##:::. ##:::: ##:::: ##:::: ##: ########::: ##::. ######::: ##:: ## ## ##: ## ### ##:: ##:: ########::
 ##.... ##:::: ##::::::: #########::: ##::::: ##:::: ##: ##.... ##:: ##:::..... ##:: ##:: ##. ####: ##. #: ##:: ##:: ##.. ##:::
 ##:::: ##:::: ##::::::: ##.... ##:: ##:::::: ##:::: ##: ##:::: ##:: ##::'##::: ##:: ##:: ##:. ###: ##:.:: ##:: ##:: ##::. ##::
 ########::::: ##::::::: ##:::: ##: ########:. #######:: ########::'####:. ######::'####: ##::. ##: ##:::: ##:'####: ##:::. ##:
........::::::..::::::::..:::::..::........:::.......:::........:::....:::......:::....::..::::..::..:::::..::....::..:::::..::""")
    r = requests.Session()
    what = input("[+] What do you need? Enter 1=Instagram likes 2=Instagram Follower !VERY SLOW! (can take up to a day until they come): ")
    if(what == "1"):
        action = "instagram_likes"
        link = input("[+] Please enter your IG post link: ")
    elif(what == "2"):
        action = "followers"
        link = input("[+] Please enter your Instagram Username: ")
    else:
        print("[-] Invalid type")
        quit()
        
    while True:
        r.get("https://instatrench.com/v5/followforfollow/cpa",params = {"token":base64.b64encode(link.encode("utf-8")),"action":action,"st":"service"})
        
        r.get("https://instatrench.com/v5/followforfollow/cpa-user/",params = {"token":base64.b64encode(link.encode("utf-8")),"survey":"2333222","email":"no_email"})
        
        userid = r.get("https://instatrench.com/v5/followforfollow/cpa",params = {"action":"info"},headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"}).json()["userId"]
        
        r.post("https://instatrench.com/v5/followforfollow/Magic/surveyApp",data = 'mood=mid&data={"userId":"'+userid+'","answerOp":"D","questionId":"8"}',headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"})
        
        r.post("https://instatrench.com/v5/followforfollow/Magic/surveyApp",data = 'mood=mid&data={"userId":"'+userid+'","answerOp":"A","questionId":"9"}',headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"})
        
        r.post("https://instatrench.com/v5/followforfollow/Magic/surveyApp",data = 'mood=mid&data={"userId":"'+userid+'","answerOp":"B","questionId":"10"}',headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"})
        
        r.post("https://instatrench.com/v5/followforfollow/Magic/surveyApp",data = 'mood=mid&data={"userId":"'+userid+'","answerOp":"A","questionId":"11"}',headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"})
        
        r.post("https://instatrench.com/v5/followforfollow/Magic/surveyApp",data = 'mood=mid&data={"userId":"'+userid+'","answerOp":"A","questionId":"12"}',headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"})
        
        r.post("https://instatrench.com/v5/followforfollow/Magic/surveyApp",data = 'mood=mid&data={"userId":"'+userid+'","answerOp":"A","questionId":"12"}',headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"})#submit "survey"
        
        
        print(r.post("https://instatrench.com/v5/followforfollow/Magic/surveyApp",data = 'mood=fin&data={"userId":"'+userid+'"}',headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"}).text)#submit order
        
        print("[+] Order sent!")
