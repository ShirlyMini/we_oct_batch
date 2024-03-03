# oops- object oriented programming language
# blue print(class) - house1, house2(obj)

# resume template(class) - stud1(obj1), stud2(obj2)
# name- stud1
# age -
# qual -
# project -
# attributes are function or variable inside class

# class
# blue print. logical entity
# no mem allocation happen on class creation
# attributes are all defined in class

# obj
# physical entity, you can create n number of obj
# mem allocation happen when obj creation
# attributes are all accessed by object

class resume_template:
    name=""
    age=""
    def education(self):
        print("BE Information tech")

    def project(self):
        print("Mini project")

# create a obj
# print(resume_template())#<__main__.resume_template object at 0x000001B2ABF84410>
stud1=resume_template()
print(stud1)#<__main__.resume_template object at 0x00000285C5408710>
print("Before changing")
print(stud1.name)
print(stud1.age)
print("After changing")
stud1.name="ram"
stud1.age="19"
print(stud1.name)
print(stud1.age)

stud1.education()
stud1.project()

stud2=resume_template()
print(stud2)#<__main__.resume_template object at 0x00000285C5408790>
print("Before changing")
print(stud2.name)
print(stud2.age)
print("After changing")
stud2.name="sam"
stud2.age="20"
print(stud2.name)
print(stud2.age)

stud2.education()
stud2.project()




