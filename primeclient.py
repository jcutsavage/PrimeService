import rpyc

#Connect to the server
server = raw_input("Please enter the server you would like to connect to")
conn = rpyc.connect(server, 12345)

#Get a number from user
n = int(raw_input("Please enter an integer: "))
#Find the primes of the user's input
conn.root.primesLessThanEqualTo(n)
