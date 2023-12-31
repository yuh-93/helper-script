import json, os, requests
from dotenv import load_dotenv

load_dotenv()
WEB_HOOK_URL = os.getenv("WEB_HOOK_URL")

# 記録されたIP読み込み
f = open("ip.txt", "r")
ip_data = f.readline().replace("\n", "")
print("記録IP: " + ip_data)
f.close()

# 現在のIP取得
ip_res = requests.get("http://httpbin.org/ip").json()
print("現在IP: " + ip_res["origin"])

if ip_res["origin"] == ip_data:
    print(True)
else:
    print(False)
    requests.post(
        WEB_HOOK_URL,
        data=json.dumps(
            {
                "text": f"現在のIPが{ip_data}から{ip_res['origin']}に変わったよ",  # 通知内容
                "username": "ip notification",
                "icon_emoji": ":smile_cat:",
                "link_names": 1,
            }
        ),
    )

    f = open("ip.txt", "w")
    f.write(ip_res["origin"])
    f.close()
