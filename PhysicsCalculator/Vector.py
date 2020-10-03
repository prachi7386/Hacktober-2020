"""This program is for finding the sum,difference or multiplication of two vectors"""
def vector():
    vect1=eval(raw_input("Enter the coefficients of the vector in list form:"))            #Input of two vectors in the form of i,j and k.
    vect2=eval(raw_input("Enter the coefficients of the vector in list form:"))
    choice=raw_input(" Addition,Subtraction,Dot product or cross product?:")              #Choice for the user from the given operations
    if(choice=="Dot" or choice=="Dot product" or choice=="dot product" or choice=="dot"):
        print vect1[0]*vect2[0]+vect1[1]*vect2[1]+vect1[2]*vect2[2],"Is the magnitude of the dot produchoicet"
    elif(choice=="Cross" or choice=="Cross product" or choice=="cross product" or choice=="cross"):
        print vect1[1]*vect2[2]-vect1[2]*vect2[1],"i",-1*(vect1[0]*vect2[2]-vect2[0]*vect1[2]),"j",(vect1[0]*vect2[1]-vect2[0]*vect2[1]),"k"
    elif(choice=="Add" or choice=="Addition" or choice=="Sum" or choice=="addition"):
        print vect1[0]+vect2[0],"i",+vect1[1]+vect2[1],"j",+vect1[2]+vect2[2],"k"
    elif(choice=="Subtract" or choice=="difference" or choice=="subtract" or choice=="sub" or choice=="Subtraction"):
         print vect1[0]-vect2[0],"i",+vect1[1]-vect2[1],"j",+vect1[2]-vect2[2],"k"
    else:
        print "Wrong choice,Exiting....."                                                                                  #if entered a wrong choice then program exits



