"""
Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.

Examples
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"

"""

def to_underscore(string):
    string = str(string)
    result = string[0].lower()
    for i in string[1:]:
        if i.isupper() == True:
            result = result + '_' + i.lower()
        else:
            result = result + i
    return result

