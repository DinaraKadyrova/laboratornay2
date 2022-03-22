f=open("text.txt" , 'r')
macs = [line.split(" - ")[0] for line in f.readlines()]
print(macs)