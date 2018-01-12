class Phonebook(object):


    def __init__(self):
        self.pb = {}

    def entry(self):
        times = int(input().strip())
        while times > 0:
            wrk = input().strip()
            wrkl = wrk.split(' ')
            #print(wrkl)
            self.pb[wrkl[0]] = wrkl[1]
            #print(self.pb)
            times -= 1

    def lookup(self):
        while True:
            query = input().strip()
            if query == '': break
            if query in self.pb:
                print(query, '=',self.pb[query],sep='')
            else:
                print("Not found")
        exit(0)


P = Phonebook()
P.entry()
P.lookup()