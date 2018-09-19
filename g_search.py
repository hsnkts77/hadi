from google import google

class Srch:
    def __init__(self,data,answer1,answer2,answer3,page=1):
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.data    = data
        self.page    = page
    def ask(self):
        c1, c2, c3 = 0, 0, 0
        self.negative = False
        if 'değildir' in self.data.lower() or 'degildir' in self.data.lower():
            self.data = self.data.replace('degildir','').replace('değildir','')
            self.negative = True

        self.result = google.search(self.data,self.page,lang='tr')
        self.answers = {self.answer1.lower():c1,self.answer2.lower():c2,self.answer3.lower():c3}

        for i in self.result: #Find possible answers and count
            for j in self.answers:
                if j in i.description.lower() or j in i.name.lower():
                    self.answers[j] += 1

        if self.negative == False: #Check whether sentence is negative and act on it
            if max(self.answers.values()) == 0:
                print('\n\n***B***U***L***U***N***A***M***A***D***I***\n\n')
            else:
                best = list(self.answers.keys())[list(self.answers.values()).index(max(self.answers.values()))]
                print('\n\n',best.upper(), max(self.answers.values()))
        elif self.negative == True:
            best = list(self.answers.keys())[list(self.answers.values()).index(min(self.answers.values()))]
            print('\n\n\n',best.upper().strip(),'\n\n\n', min(self.answers.values()))

#EXAPMLE
if __name__ == '__main__':
    srch = Srch('"dumanlı koy" nedir', 'reykjavik', 'dublin', 'stockholm ',1)
    srch.ask()
    input()
