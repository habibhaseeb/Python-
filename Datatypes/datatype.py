from typing import Tuple

n = issubclass(bool , int)
print("Result:" , n );
        #     // Numbers

number1 = 10;
number2 = 34545550135450;  # Arbitary sizes of int


_Res = number1
_Res1 = number2

print(type(_Res));
print(type(_Res1));  # // integers


        #     // Floating point numbers 

number1 = 0.5324;
number2 = 8.56;

others = 10.e2

Result1 = type(number1);
Result2 = type(number2);

print(Result1 , Result2 , others);  # // <float>

#                     //   Strings  //

let = "This is String Datatype in python";

suppose = 'This is single quote String'

# Note: Backticks not available in python ``


                   #  Tuples 

a = (10 , 11 , 'Python' , (1 , 2));
# a[2] = 12   # TypeError

# tuples are immutable not change any reference.

print(a);

person : Tuple[str , str , str] = ("habib" , "ABC" , "Habib@gmail.ai");

name , address , email = person;

print (f"Name: {name}");
print (f"Address is: {address}");
print (f"Email is: {email}");


# person[0] = "Habib"
# person[1] = "ABC"
# person[2] = "Habib@gmail.ai"

