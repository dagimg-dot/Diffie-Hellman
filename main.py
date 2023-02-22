prime = int(input("Enter the prime number: "))

list = []
for i in range(0,prime-1):
    list.append(i+1)

gen_list = []

possible_gen = []

for i in range(2,prime):
    for j in range(1, len(list)+1):
        ins = i**j % prime
        gen_list.append(ins)
    if sorted(gen_list) == list:
        print("The generator" , i ,"produces all the elements of the main list")
        possible_gen.append(i)
        print(gen_list)
        gen_list.clear()
    else:
        gen_list.clear()
        continue

print("\n\nThe possible generators are: ", possible_gen)
