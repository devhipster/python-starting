#type hint
""" 
The most fundamental support consits of the types : 
Any, Union,tuple ,Callable , TypeVar, and Generic

"""
#an example of annotation 

def greeting(name: str)-> str: 
    return 'Hello '+name

#type alliases 
#example

""" he's how we can declare an aliases "
Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

new_vector = scale(2.0,[1.0,30.3 , -4.322])

#an complex example of it 

from collections.abs import sequence


ConnectionOptions = dict[str,str]
Address = tuple[str,int]
Server =  tuple[Address,ConnectionOptions]


#challenge create a function declaration to use the above variables 
#challenge create the unchained statement for the above decalration



        """  Comprehension in debunking """




        




