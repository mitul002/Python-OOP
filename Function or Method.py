
#Create class
class student:
    id_no=""
    section=""

   #Method/Function
    def input(self,id,sec):
        self.id_no = id
        self.section=sec

    def display(self):
        print(f"ID : {self.id_no}  Section: {self.section}")

#Create object
Rahim=student()
Rahim.input(9899,"D")
Rahim.display()

Karim=student()
Karim.input(9786,"K")
Karim.display()
