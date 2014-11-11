import rpyc

class PrimeService(rpyc.Service):
    def on_connect(self):
        #initialize
        pass

    def on_disconnect(self):
        #finalize
        pass

    def isprime(n):
        if n < 2:
            return False
        elif n == 2: 
            return True
        for x in range(2,n-1):
            if not n % x: return False
        return True

    def exposed_primesLessThanEqualTo(self,n):
        primes = []
        x=2
        for x in range(2,n):
            if isprime(x):
                primes.append(x)
        return primes

if __name__== "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(PrimeService, port = 12345)

