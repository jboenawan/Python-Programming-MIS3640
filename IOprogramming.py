#synchronous and asynchronous type of io programming.

# fout = open('output.txt','w') #w means to write on files
# line1 = "How many roads must a man walk down\n"
# fout.write(line1)
# line2 = "Before you call him a man?\n"
# fout.write(line2)
# fout.close()

import os 
cwd = os.getcwd()
# print(cwd)
print(os.path.abspath('output.txt')) #absolute path 
print(os.path.exists('output.txt')) #does it exist 

try:
    fin = open('bad_file') #if this doesnt work, do 'except' function
except:
    print("something went wrong.")

print("now we are here.")

import pickle 
t1 = [1,2,3]
s = pickle.dumps(t1)

t2 = pickle.loads(s)
print(t2)

print(t2==t1)