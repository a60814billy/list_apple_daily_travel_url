import urllib.request
import lxml.html
import datetime
import sys

def generate_date(before_days):
    today = datetime.date.today()
    dateArray = []
    dateArray.append(today.strftime('%Y%m%d'))
    for i in range(1,before_days):
        delta = datetime.timedelta(days=i)
        dateArray.append((today - delta).strftime('%Y%m%d'))
    return dateArray

def get_article_href(specific_date):
    url = 'http://www.appledaily.com.tw/appledaily/archive/' + specific_date
    req = urllib.request.urlopen(url)
    data = req.read().decode('utf-8')
    page = lxml.html.fromstring(data)
    content = page.xpath('//*[@id="snr-mainSub"]/article[2]/ul/li/a')
    return 'http://www.appledaily.com.tw/' + content[0].get('href')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: python3 " + sys.argv[0] + " how_many_dates_shows")
        print("example: python3 " + sys.argv[0] + ' 5')
        exit()
    
    try:
        count = int(sys.argv[1])
        if count <= 0:
            print("argument must greater than zero.")
    except:
        print("argument must be number.")
        exit()

    result = []
    dateArr = generate_date(count)
    print(dateArr)
    for d in dateArr:
        result.append( get_article_href(d) )

    for art in result:
        print(art)

