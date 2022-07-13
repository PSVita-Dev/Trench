import requests, base64

class Instagram:
    def __init__(self, url: str, choice: str):
        self.url = url
        self.choice = "instagram_likes" if choice == 1 else "followers"

    def xuserid(self, session: requests.Session):
        userid = session.get(
            "https://instatrench.com/v5/followforfollow/cpa",
            params = {
                "action":"info"
            },
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"
            }
        ).json()["userId"]
        
        return userid

    def main(self):
        while True:
            session = requests.Session()
            
            session.get(
                url = "https://instatrench.com/v5/followforfollow/cpa",
                params = {
                    "token":base64.b64encode(self.url.encode()),
                    "action": self.choice,
                    "st": "service"
                }
            )

            session.get(
                url = "https://instatrench.com/v5/followforfollow/cpa-user/",
                params = {
                    "token":base64.b64encode(self.url.encode()),
                    "survey":"2333222",
                    "email":"no_email"
                    }
            )

            userid = self.xuserid(session)
            
            session.post("https://instatrench.com/v5/followforfollow/Magic/surveyApp",data = 'mood=mid&data={"userId":"'+userid+'","answerOp":"D","questionId":"8"}',headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"})
            session.post("https://instatrench.com/v5/followforfollow/Magic/surveyApp",data = 'mood=mid&data={"userId":"'+userid+'","answerOp":"A","questionId":"9"}',headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"})
            session.post("https://instatrench.com/v5/followforfollow/Magic/surveyApp",data = 'mood=mid&data={"userId":"'+userid+'","answerOp":"B","questionId":"10"}',headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"})
            session.post("https://instatrench.com/v5/followforfollow/Magic/surveyApp",data = 'mood=mid&data={"userId":"'+userid+'","answerOp":"A","questionId":"11"}',headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"})
            session.post("https://instatrench.com/v5/followforfollow/Magic/surveyApp",data = 'mood=mid&data={"userId":"'+userid+'","answerOp":"A","questionId":"12"}',headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"})
            session.post("https://instatrench.com/v5/followforfollow/Magic/surveyApp",data = 'mood=mid&data={"userId":"'+userid+'","answerOp":"A","questionId":"12"}',headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"})
            req = session.post("https://instatrench.com/v5/followforfollow/Magic/surveyApp",data = 'mood=fin&data={"userId":"'+userid+'"}',headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36"}).text
            
            print(f"Sucess  | Sent 20 likes: {req}")

if __name__ == "__main__":
    link = input('[?] post link: ')
    choice = int(input('[?] 1) likes \n 2) Follows (slow asf 1 day +)\n choice: '))

    Instagram(link, choice).main()
