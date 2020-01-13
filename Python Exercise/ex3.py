def percent_to_gpv (percent):
    ''' (int) -> float
        
        Takes in the percent of a course as an integer and returns a GPA value
        in terms of a float.
        
        REQ: percent >=0 and percent<=100
        REQ: Must be entered as an integer
    
        >>> percent_to_gpv(87)
        4.0
        >>> percent_to_gpv(54)
        1.0
    
    '''   
    #If the percent given is between 85-100
    if (int((percent>=85))):
        GPV=float(4.0) #GPA is a 4.0       
    
    #If the percent given is between 80-84  
    elif(int((percent>=80))):
        GPV=float(3.7)#GPA is a 3.7 
    
    #If the percent given is between 77-79
    elif(int((percent>=77))):
        GPV=float(3.3)#GPA is a 3.3         
    
    #If the percent given is between 73-76
    elif(int((percent>=73))):
        GPV=float(3.0)#GPA is a 3.0  
    
    #If the percent given is between 70-72
    elif(int((percent>=70))):
        GPV=float(2.7)#GPA is a 2.7          
    
    #If the percent given is between 67-69
    elif(int((percent>=67))):
        GPV=float(2.3)#GPA is a 2.3 
   
   #If the percent given is between 63-66
    elif(int((percent>=63))):
        GPV=float(2.0)#GPA is a 2.0    
  
   #If the percent given is between 60-62 
    elif(int((percent>=60))):
        GPV=float(1.7)#GPA is a 1.7  
   
   #If the percent given is between 57-59
    elif(int((percent>=57))):
        GPV=float(1.3)#GPA is a 1.3  
   
   #If the percent given is between 53-56
    elif(int((percent>=53))):
        GPV=float(1.0)#GPA is a 1.0  
   
   #If the percent given is between 50-52 
    elif(int((percent>=50))):
        GPV=float(0.7)#GPA is a 0.7      
  
   #If the percent given is between 0-49 
    else:
        GPV=float(0.0)#GPA is a 0.0  
    
    #Return the GPA Value
    return GPV    
 
 
 
        
def card_namer(Value,Suits): 
    ''' (str,str) -> str
           
        Takes in the Value and Suit of a card in the form of a string and return
        the name of the card (i.e Queen of Diamonds) in the form of a string.
        If the parameters take in the wrong Values it will say CHEATER!
           
        REQ: The values entered in the prarameters must be a string
        
        >>> card_namer('K','S')
        'King of Spades'
        >>> card_namer('8','C')
        '8 of Clubs'
        >>> card_namer('8','T')
        'CHEATER!'
    '''
    #VALUE OF CARDS
    #If the Value of a Card is entered as an "A"
    if(str(Value)==str("A")):
        result=str("Ace")#Result is Ace
    
    #If the Value of a Card is entered as a "K"    
    elif(str(Value)==str("K")):
        result=str("King")#Result is King
  
    #If the Value of a Card is entered as a "Q"    
    elif(str(Value)==str("Q")):
        result=str("Queen") #Result is Queen       
    
    #If the Value of a Card is entered as a "J"
    elif(str(Value)==str("J")):
        result=str("Jack")#Result is Jack        
    
    #If the Value of a Card is entered as a "T" 
    elif(str(Value)==str("T")):
        result=str(10)#Result is 10
    
    #If the Value of a Card is entered as a "2-9"
    elif((str(Value)>=str("2")) and (str(Value)<=str("9"))):
        result=str(Value)#Result is between 2-9
    
    #If any other value is entered other than the required 
    else:    
        result=str("CHEATER!")#Result is "CHEATER!"   
   
   
    #SUITS OF CARDS
    #If the Suit of Card is entered as "D" 
    if(str(Suits)==str("D")):
        suit=str("Diamonds")#Suit is Diamonds
    
    #If the Suit of Card is entered as "C"
    elif(str(Suits)==str("C")):
        suit=str("Clubs")#Suit is Clubs
    
    #If the Suit of Card is entered as "H"
    elif(str(Suits)==str("H")):
        suit=str("Hearts")#Suit is Hearts        
    
    #If the Suit of Card is entered as "S"
    elif(str(Suits)==str("S")):
        suit =str("Spades")#Suit is Spades
   
    #If any other value is entered other than the required Suit
    else:
        suit=str("CHEATER!")#The outcome is "CHEATER!"
     
    
    #If the outcome of either the Value or Suit is "CHEATER!"    
    if((str(suit)==str("CHEATER!")) or (str(result)==str("CHEATER!"))):
        Final=str("CHEATER!") #The Final outcome will be "CHEATER!" 
    
    #If anything else is entered
    else:
        Final=(str(result) + " of " + str(suit))#The Final outcome is the card  
    #Return the appropriate Final outcome of the card
    return Final    