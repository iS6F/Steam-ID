import requests, random, string, bs4
len = 3
webhook = ""
while True:
    id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=len))
    request = requests.get(f'https://steamcommunity.com/id/{id}')
    lxml = bs4.BeautifulSoup(request.content, 'lxml')
    title = lxml.find('title')
    list = title.text.split()
    if list[-1] == "Error":
        print(f'{id} is Available')
        requests.post(webhook, data={"content" : f'{id} is Available'})
    else:
        print(f'{id} is Taken')
