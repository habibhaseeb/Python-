int_list = [3, 2, 1];

string_list = ["def" , "Kotlin", "Java"];
empty_list = [];


Mixed_list = [9 , 'abc', None , bool , 1.345, "Sting"];
nested_list = [['1','2','3'],[1 , True & 2 , False & 3 , False & 4 , True]];

nested_list1 = [['1','2','3'],[1 , True + 2 , False + 3 , False + 4 , True]];

print(nested_list)

names = ["Alice","John" ,"Habib" ,"Enrich"];

print(names[0])
print(names[-0]) # Alice
print(names[-1])

names[1] = "John Wick"
names.insert(1 , "john wick")  # add new element to a list at specific index you want

           # Remove

foods = ["Chicken" , "beef" , "Qorma" , "Rice"];
foods.remove("Chicken");
print(foods);

  # Append object at the end of the line OR list 

names.append("Hello!")
print(names)

# Length function in python -->   len()
# if you verify the length of that array OR list in python 

Length = len(names)
print(Length)

# To check index of the elements

foods = foods.index("beef");
print(foods)


# To confirm the repeated elements in the array

array = [ 2 , 2 , 2 , 8 , 1 , 1, 1 , 1 , 1 , 1 , 1];
array = array.count(2) , array.count(1);
print(array);

