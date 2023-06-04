nickname = input("Enter nickname: ")
profession = input("Enter profession: ")

url = "http://example.com/{}/desirable/{}/profile".format(nickname, profession)

print("User-specific URL: {}".format(url))
