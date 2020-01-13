# Global variables. Feel free to play around with these
# but please return them to their original values before you submit.
a0_weight = 5
a1_weight = 7
a2_weight = 8
term_tests_weight = 20
exam_weight = 45
exercises_weight = 10
quizzes_weight = 5
a0_max_mark = 25
a1_max_mark = 50
a2_max_mark = 100
term_tests_max_mark = 50
exam_max_mark = 100
exercises_max_mark = 10
quizzes_max_mark = 5
exam_pass_mark = 40
overall_pass_mark = 50


def get_max(component_name):
    '''(str) -> float
    Given the name of a course component (component_name),
    return the maximum mark for that component. This is used to allow the GUI
    to display the "out of" text beside each input field.
    REQ: component_name must be one of: a0,a1,a2,exerises,midterm,exam
    >>> get_max('a0')
    25
    >>> get_max('exam')
    100
    REQ: component_name in {'a0', 'a1', 'a2', 'exercises', 'term tests',
    'quizzes', 'exam'}
    '''
    # DO NOT EDIT THIS FUNCTION. This function exists to allow the GUI access
    # to some of the global variables. You can safely ignore this function
    # for the purposes of E2.
    if(component_name == 'a0'):
        result = a0_max_mark
    elif(component_name == 'a1'):
        result = a1_max_mark
    elif(component_name == 'a2'):
        result = a2_max_mark
    elif(component_name == 'exercises'):
        result = exercises_max_mark
    elif(component_name == 'term tests'):
        result = term_tests_max_mark
    elif(component_name == 'quizzes'):
        result = quizzes_max_mark
    else:
        result = exam_max_mark

    return result

def percentage(raw_mark, max_mark):
    ''' (float, float) -> float
    Return the percentage mark on a piece of work that received a mark of
    raw_mark where the maximum possible mark of max_mark.
    
    >>> percentage(15, 20)
    75.0
    >>> percentage(4.5, 4.5)
    100.0
  
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: raw_max <= max_mark
    '''
    
    #Returns the mark into a percentage
    return raw_mark / max_mark * 100


def contribution(raw_mark, max_mark, weight):
    ''' (float, float, float) -> float
    
    Given a piece of work where the student earned raw_mark marks out of a
    maximum of max_marks marks possible, return the number of marks it
    contributes to the final course mark if this piece of work is worth weight
    marks in the course marking scheme.
    
    >>> raw_contribution(13.5, 15, 10)
    9.0
    REQ: raw_mark >=0
    REQ: max_mark > 0
    REQ: weight >= 0
    '''
    # start your own code here
def term_work_mark(a0,a1,a2,excercises,quizzes,termtests): 
    ''' (float, float,float, float,float, float) -> float
        
        Takes in the marks recived on assignment 0,assignment 1,assignment 2,
        excercises,quizzes and term tests. Then returns the term work mark by 
        dividing each of the grades by the appropriate maximum results and 
        multiplying it by the appropriate weighing.
       
        REQ: a0 >=0 and a0<=25
        REQ: a1 >=0 and a1<=50
        REQ: a2 >=0 and a2<=100
        REQ: excercises >=0 and excercises<=10
        REQ: quizzes >=0 and quizzes<=5
        REQ: termtests >=0 and termtests<=50
        
        >>> term_work_mark(25, 50, 100, 10, 5, 50)
        55.0
        >>> term_work_mark(20, 45, 70, 8, 4, 40)
        43.9
       
    '''
    #Calculations to find the term mark of each category weighting.
    #Convert to float inorder to get deimcals
    a0=float(a0/a0_max_mark)*a0_weight
    a1=float(a1/a1_max_mark)*a1_weight
    a2=float(a2/a2_max_mark)*a2_weight
    excercises=float(excercises/exercises_max_mark)*exercises_weight
    quizzes=float(quizzes/quizzes_max_mark)*quizzes_weight
    termtests=float(termtests/term_tests_max_mark)*term_tests_weight
    
    #Add each catergory for the termwork up
    term_mark= float((a0+a1+a2+excercises+quizzes+termtests))
    return term_mark

def final_mark(a0,a1,a2,excercises,quizzes,termtests,exam):
    ''' (float, float,float, float,float, float, float) -> float
            
        Takes in the marks recived on assignment 0,assignment 1,assignment 2,
        excercises,quizzes,term tests and exam. Then returns the final mark  
        by dividing each of the grades by the appropriate maximum results and 
        multiplying it by the appropriate weighing.
           
        REQ: a0 >=0 and a0<=25
        REQ: a1 >=0 and a1<=50
        REQ: a2 >=0 and a2<=100
        REQ: excercises >=0 and excercises<=10
        REQ: quizzes >=0 and quizzes<=5
        REQ: termtests >=0 and termtests<=50
        REQ: exam >=0 and exam<=100
           
        >>> final_mark(25, 50, 100, 10, 5, 50,100)
        100.0
        >>> final_mark(20, 45, 70, 8, 4, 40, 73)
        76.75
           
    '''    
    
    #Exam mark is now included 
    #Calculations to find the term mark of each category weighting.
    #Convert to float inorder to get deimcals, and not rounded values     
    a0=float(a0/a0_max_mark)*a0_weight
    a1=float(a1/a1_max_mark)*a1_weight
    a2=float(a2/a2_max_mark)*a2_weight
    excercises=float(excercises/exercises_max_mark)*exercises_weight
    quizzes=float(quizzes/quizzes_max_mark)*quizzes_weight
    termtests=float(termtests/term_tests_max_mark)*term_tests_weight 
    exam=float(exam/exam_max_mark )*exam_weight 
    
    #Add up all the marks and return the final mark
    final=float((a0+a1+a2+excercises+quizzes+termtests+exam))
    return final    

def is_pass(a0,a1,a2,excercises,quizzes,termtests,exam):
    ''' (float, float,float, float,float, float, float) -> float
             
         Takes in the marks recived on assignment 0,assignment 1,assignment 2,
         excercises,quizzes,term tests and exam. Then returns the term work mark  
         by dividing each of the grades by the appropriate maximum results and 
         multiplying it by the appropriate weighing. Later it determines with a
         boolean wether or not you pass the course. If you grade is above 50 and
         exam mark is also above 40 you pass and the boolean will return true.
         However if you dont meet the passing requirement of 50 and above nor an
         exam grade of 40 and above you fail. The boolean will then return false
            
         REQ: a0 >=0 and a0<=25
         REQ: a1 >=0 and a1<=50
         REQ: a2 >=0 and a2<=100
         REQ: excercises >=0 and excercises<=10
         REQ: quizzes >=0 and quizzes<=5
         REQ: termtests >=0 and termtests<=50
         REQ: exam >=0 and exam<=100
            
        >>> is_pass(20, 45, 70, 8, 4, 40, 41)
        True
        >>> is_pass(20, 45, 70, 8, 4, 40, 39)
        False
        >>> is_pass(10, 21, 12, 2, 1, 15, 23)
        False
            
     '''    
    
    #Calculations to find the term mark of each category weighting.
    #Convert to float inorder to get deimcals, and not rounded values         
    a0=float(a0/a0_max_mark)*a0_weight
    a1=float(a1/a1_max_mark)*a1_weight
    a2=float(a2/a2_max_mark)*a2_weight
    excercises=float(excercises/exercises_max_mark)*exercises_weight
    quizzes=float(quizzes/quizzes_max_mark)*quizzes_weight
    termtests=float(termtests/term_tests_max_mark)*term_tests_weight 
    exam=float(exam/exam_max_mark )*exam_weight  
    
    #Final mark
    final=float((a0+a1+a2+excercises+quizzes+termtests+exam))
    
    #Calculation to get the exam mark to the orginal mark that was given and
    #Not the mark exam number after bring weighted
    exam=float((exam/exam_weight)*exam_max_mark)
    
    #Returs the boolean True if the final mark is greater than or equal to 50
    #And if the Exam mark is greater than or equal to 40
    #Else if, it returns False
    return bool((final>=overall_pass_mark) and (exam>=exam_pass_mark))

