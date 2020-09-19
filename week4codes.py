str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars = []
for s in str1:
    chars.append(s)
    
    
    
###### 


ael = "python!"

app = []

for ele in ael:
    app.append(ele)



 #######
 
 
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]

past_wrds = []

for str in wrds:
    new_word = str+"ed"
    past_wrds.append(new_word)

##########

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']


sports.insert(2,"horseback riding")


#########

trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']

pos_london = trav_dest.index("London")
trav_dest.pop(pos_london)


#################

trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']


trav_dest.append("Guadalajara")


###############

winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']


winners.sort()



##################






#############

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

split_scores = scores.split()

a_scores = 0 

for score in split_scores:
    score = int(score)
    if score >= 90:
        a_scores +=1
        
        
###################      
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

org_split = org.split()

acro = ""

for word in org_split:
    if word not in stopwords:
        caps = word[0].upper()
        acro = acro + caps
        print(acro)
        
        
        
#####################        
        
        
        
        
