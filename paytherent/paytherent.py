import itertools

outcome = None
def paytherent(a,b,c,d,e,f):
    perms = list(itertools.permutations([a,b,c,d,e,f]))
    final = []            
    for i in perms:
        if i[0] < (i[1] + i[2]) < (i[3] + i[4]) < i[5]:
            final.append(i)
    for i in final:
        for n in final:
            if (([i[1], i[2]] == [n[1], n[2]]) and ([i[3], i[4]] == [n[4], n[3]])):
                final.remove(n)
        for n in final:
            if (([i[3], i[4]] == [n[3], n[4]]) and ([i[1], i[2]] == [n[2], n[1]])):
                final.remove(n)
        for n in final:
            if (([i[3], i[4]] == [n[4], n[3]]) and ([i[1], i[2]] == [n[2], n[1]])):
                final.remove(n)
    global outcome
    if len(final) == 1:
        outcome = "1 winning combination."
    else:
        outcome = str(len(final)) + " winning combinations."
    for i in final:
        print "[" + str(i[0]) + ", (" + str(i[1]) + " & " + str(i[2]) + "), (" + str(i[3]) + " & " + str(i[4]) + "), " + str(i[5]) + "]"

#paytherent(1.49, 2.98, 3.49, 5.49, 5.99, 7.30)
#print "SEPTEMBER 20, 2010: " + outcome
#paytherent(3.99, 0.79, 4.99, 3.39, 2.99, 6.79)
#print "NOVEMBER 11, 2010: " + outcome
#paytherent(2.99, 0.25, 1.99, 1.69, 2.49, 3.99)
#print "NOVEMBER 11, 2011: " + outcome
#paytherent(2.89, 0.35, 2.99, 4.49, 6.49, 4.99)
#print "JANUARY 6, 2012: " + outcome
#paytherent(2.29, 1.99, 1.49, 2.99, 2.09, 4.22)
#print "APRIL 30, 2012: " + outcome
#paytherent(5.29, 7.69, 9.99, 13.99,6.99, 6.82)
#print "MAY 16, 2012: " + outcome
#paytherent(5.99, 3.49, 4.60, 2.29, 3.99, 8.00)
#print "AUGUST 17, 2012: " + outcome
#paytherent(2.49, 3.19, 1.29, 3.99, 3.69, 5.99)
#print "DECEMBER 21, 2012: " + outcome
#paytherent(0.59, 1.09, 3.39, 2.29, 5.79, 9.99)
#print "MARCH 27, 2013: " + outcome
paytherent(2.49, 1.59, 4.99, 2.79, 5.79, 12.99)
print "APRIL 24, 2013: " + outcome