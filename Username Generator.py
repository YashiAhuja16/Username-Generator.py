import random   
while True : 
    x = input ("Enter your full name (type 'exit' to stop) : " )
    if x == "exit" : 
        break 
    else : 
        p = x.split (" ")
        p1 = p [0]
        p2 = p [1] 
        y = ["@", "_", "+", ",", "&", "%"]
        z = random.randint (1,10)

        # different combinations to generate usernames 
        comb1 = p1[:3] + random.choice (y) + p2 [-3:]
        comb2 = str (z) + random.choice (p) + random.choice (y)
        comb3 = p2[:2]  + random.choice (y) + p1 [2:]
        comb4 = random.choice (p) + random.choice (y) + str (z)
        comb5 = p2[::3] + p1[::-2] + str (z) 

        # final output 
        final_com = [comb1, comb2, comb3, comb4, comb5]
        print (random.choice(final_com))
