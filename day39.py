question=[
["Q1.What is the capital of India","a.Mumbai","b.Kolkata","c.New Delhi","d.Jaipur",3 ],
["Q2.Which among this is not a fruit", "a.Banana", "b.Carrot", "c.Watermelon", "d.Apple",2], 
["Q3.Who is the Prime Minister of India", "a.Indra Gandhi", "b.Rahul Gandhi", "c.Narendra Modi", "d.None",3],
["Q4.What is India's national bird", "a.Parrot", "b.Owl", "c.Peacock", "d.Crow",3],
["Q5.What is India's national animal", "a.Lion", "b.Dog", "c.Elephant", "d.Tiger",4]
]

levels=[1000,2000,3000,5000,10000,20000,50000,80000,160000,320000,640000,10000000]


for i in range(0,len(question)):
    print(f"\n\nQuestion for Rs.{levels[i]}:")
    questions= question[i]   
    print(f"{questions[0]}") 
    print(f"{questions[1]}     {questions[2]}")
    print(f"{questions[3]}     {questions[4]}")
    reply=int(input("Enter the correct option(1-4):"))
    if (reply==questions[-1]):
        print(f"Correct answer, you have won Rs.{levels[i]}")
    else:
        print("Wrong Answer, better luck next time")
        break
print(f"\nYou have won Rs.{levels[i]}")


        
    
            

    