num=int(input("you want odd and even numbers under the value?: "))
odd_list=[i for i in range(num) if i%2 !=0]
print("List of odd numbers:",odd_list,"\n")
fruits=['apple','bannana','mango','papaya','grapes']
fruits=[x[0].upper()+x[1:] for x in fruits]
print(("Fruits as proper nouns:",fruits))