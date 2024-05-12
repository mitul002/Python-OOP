
#Create class
class student:
    '''id_no=""
    section=""
    ''' #If we use method or constructor we don't need to use this part

   #Constructor
    def __init__(self, id,sec):
        self.id_no = id
        self.section=sec

    # Method/Function
    def display(self):
        print(f"ID : {self.id_no}  Section: {self.section}")

#Create object
Rahim=student(9899,"D") #Constructor don't need to call seperately
Rahim.display()

Karim=student(9786,"K")
Karim.display()
