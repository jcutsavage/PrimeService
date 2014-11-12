#!/usr/bin/env python3

import rpyc

#Server capable of returning primes <= a number
class PrimeService(rpyc.Service):
    def on_connect(self):
        #initialize
        pass

    def on_disconnect(self):
        #finalize
        pass

#check if prime
    def isprime(self,n):
        if n < 2: #not prime
            return False
        elif n == 2: #2 is prime
            return True
        for x in range(2,n-1):
            if not n % x: return False
        return True

#check for primes <= a number n.
#return array
    def exposed_primesLessThanEqualTo(self,n):
        primes = []
        x=2
        for x in range(2,n):
            if self.isprime(x):
                primes.append(x)
        return primes

#start server
from rpyc.utils.server import ThreadedServer
t = ThreadedServer(PrimeService, port = 12345)
t.start()
