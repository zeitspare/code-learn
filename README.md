# code-learn
codes, Frameworks, basic definition, Cheets sheats, short Tricks.
---
![class](CLASS.PNG "Class - Objects, Attributes and Functionalities")   ![class types](CLASSTYPES.PNG "Different types of Classes") 
![derived class](CLASSTYPES1.PNG "Derived Classes")   ![super class](SUPERCLASS.PNG "Super and Sub Classes")
---
OOPS CONCEPT

### Class
 A class contains the blueprints or the prototype from which the objects are being created. It is a logical entity that contains some attributes and methods

### Object
The object is an entity that has a functionality and property associated with it.

### Methods
A method in python is somewhat similar to a function, except it is associated with object/classes

### Functions
A function is a block of code to carry out a specific task, will contain its own scope and is called by name. 

### Inheritance 
Inheritance is the capability of one class to derive or inherit the properties from another class. The class that derives properties is called the derived class or child class and the class from which the properties are being derived is called the base class or parent class.

|Single-Inheritance|Multilevel-Inheritance|Hierachical-Intheritance|Multile-Inheritance|
|-----------|:-----------:|-----------:|-----------:|
enables a derived class to inherit characteristics from a single-parent class.|enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class.|enables more than one derived class to inherit properties from a parent class.| enables one derived class to inherit properties from more than one base class.|

### Polymorphism
Polymorphism simply means having many forms.

### Encapsulation
wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. 

### Data Abstraction
hides the unnecessary code details from the user. To hide sensitive parts of our code implementation.
Data Abstraction in Python can be achieved through creating abstract classes

### self
The word 'self' is used to represent the instance of a class. By using the "self" keyword we access the attributes and methods of the class in python.

### _ _ init _ _ method
"_ _ init _ _" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.

### _ _ superprivate
variable name with double underscore prefix. will keep the Variable superprivate can be accessed only in the base class and not even in Derived class

### _ semiprivate
variable name with single underscore prefix. will keep the Variable semiprivate can only be accessed or changed  if this is a absolutely must.
