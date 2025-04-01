'''
Given a String, split it into major parts separated by special char '/'. For each major part that’s split by '/',
we can further split it into minor parts separated by '.'.

### Example 1
str = stripe.com/payments/checkout/customer.john.doe
minor_parts = 2
after Part 1 compression
=>
s4e.c1m/p6s/c6t/c6r.j2n.d1e
after Part 2 compression
=>
s4e.c1m/p6s/c6t/c6r.j5e
### Example 2
Given:
str = www.api.stripe.com/checkout
minor_parts = 3
(after Part 1 compression)
=>
w1w.a1i.s4e.c1m/c6t
(then after Part 2 compression)
=>
w1w.a1i.s7m/c6t

The question is to compress the string. The rule is that, for each major part,
 it contains at most <minor_parts> minor parts. And for each minor parts,
 you need to compress it in the format of <heading_letter><letter_count_in_betwee><tailing_letter>.
The edge case is, what if the minor part contains less than 3 letters?
Like the first minor part of m.stripe.com/checkout.
'''


"stripe.com/payments/checkout/customer.john.doe"
class SplitAndCompress:

    def __init__(self, st, minor_parts):
        self.st = st
        self.minor_parts = minor_parts
        self.IsGeneralCompressionDone = False
        self.compressionRequired = False


    def compressInternal(self):
        self.compressionRequired = False
        stlist = self.st.split('/')
        newlist = []
        for item in stlist:
            itemlist = item.split('.')
            if len(itemlist) <= self.minor_parts or len(itemlist) <= 1:
                newlist.append(item)
                continue
            self.compressionRequired = True
            seclast, last = itemlist[-2], itemlist[-1]
            seclastint = int(seclast[1:-1])
            lastint = int(last[1:-1])
            newitem = seclast[0] + str(seclastint+lastint + 2) + last[-1]
            itemlist.pop(-1)
            itemlist.pop(-1)
            itemlist.append(newitem)
            newlist.append('.'.join(itemlist))
        self.st = '/'.join(newlist)

        return self.st
    def generalCompression(self):
        if self.IsGeneralCompressionDone:
            return
        stlist = self.st.split('/')
        newlist = []
        for item in stlist:
            itemlist = item.split('.')
            newitlist = []
            for it in itemlist:
                it = it[0] + str(len(it[1:-1]))+it[-1]
                newitlist.append(it)
            newitem = '.'.join(newitlist)
            newlist.append(newitem)
        self.st = '/'.join(newlist)
        self.IsGeneralCompressionDone = True

    def compress(self):
        stlist = self.st.split('/')
        for item in stlist:
            itemlist = item.split('.')
            if len(itemlist) > self.minor_parts:
                self.generalCompression()
                self.compressionRequired = True
                break
        while(self.compressionRequired):
            # print(self.st)
            self.compressInternal()
        return self.st

    def print(self):
        print(self.st)


splitAndCompress = SplitAndCompress("stripe.com/payments/checkout/customer.john.doe", 2) # s4e.c1m/p6s/c6t/c6r.j5e
res = splitAndCompress.compress()
print(res == "s4e.c1m/p6s/c6t/c6r.j5e")

splitAndCompress2 = SplitAndCompress("www.api.stripe.com/checkout", 3) # w1w.a1i.s7m/c6t
res = splitAndCompress2.compress()
print(res == "w1w.a1i.s7m/c6t")