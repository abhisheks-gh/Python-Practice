class Parent:
     def func1(self):
         print("this is function 1")
class Child(Parent):
     def func2(self):
          Super().func1()
          print("this is function 2")
 
ob = Child()
ob.func2()