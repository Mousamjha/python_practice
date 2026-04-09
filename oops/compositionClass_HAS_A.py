
class InternationalNews:

    def __init__(self):
        self.newsHeading = "Top 4 NEWS from International"
        self.newsNos = 4

    def displayInternationalNews(self):
        print(f"*****{self.newsHeading}*****")
        for news in range(self.newsNos):
            print(f"This is news no {news}")


class SportsNews:

    def __init__(self):
        self.newsHeading = "Top 4 NEWS from Sports"
        self.newsNos = 4

    def displaySportsNews(self):
        print(f"*****{self.newsHeading}*****")
        for news in range(self.newsNos):
            print(f"This is news no {news}")


class NationalNews:

    def __init__(self):
        self.newsHeading = "Top 4 NEWS from Nation"
        self.newsNos = 4

    def displayNationalNews(self):
        print(f"*****{self.newsHeading}*****")
        for news in range(self.newsNos):
            print(f"This is news no {news}")



class MyNewsChannel:

    channelName = "| !!!!! Siddhant News !!!!! |"

    def displayAllNews(self):
        n1 = InternationalNews()
        n2 = SportsNews()
        n3 = NationalNews()
        print("-----------------------------")
        print(MyNewsChannel.channelName)
        print("-----------------------------")
        print()
        print(n1.newsHeading)
        print("* ----------------------------- *")
        print(n1.displayInternationalNews())
        print()
        print(n2.newsHeading)
        print("* ----------------------------- *")
        print(n2.displaySportsNews())
        print()
        print(n3.newsHeading)
        print("* ----------------------------- *")
        print(n3.displayNationalNews())


myNews = MyNewsChannel()
myNews.displayAllNews()