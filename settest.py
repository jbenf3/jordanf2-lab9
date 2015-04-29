#!/usr/bin/python

import sets

def main():

    s = sets.Set([4,5,6,7])
    print "Declare s:"
    print s
    
    t = sets.Set([1,2,3,4,5])
    print "Declare t: "
    print t

    print "s&t:"
    print s&t
    print "Print s again:"
    print s
    print "s-t:"
    print s-t
    print "Print s again:"
    print s
    print "s|t:"
    print s|t
    print "Print s again:"
    print s
    s.add(5)
    print "Add 5 to s:"
    print s
    s.delete(5)
    print "Remove 5 from s:"
    print s

main()
