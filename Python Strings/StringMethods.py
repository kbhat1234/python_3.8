course = 'Python for Beginners '
course1 = '22312312'
cast = int(course1)
course2 = '   Raaga apartments   '

''' len(course) -> 20 '''
print(f'length of course is {len(course)}')

''' title() -> "Python For Beginners" '''
print(f'title of course is {course.title()}')

''' casefold() -> "python for beginners" '''
print(f'casefold is {course.casefold()}')

''' upper() -> "PYTHON FOR BEGINNERS" '''
print(f'course upper is {course.upper()}')

''' lower() -> "python for beginners" '''
print(f'course lower is {course.lower()}')

''' isdigit() -> False '''
print(f'course isdigit is {course.isdigit()}')

''' isdigit() -> True '''
print(f'course isdigit is {course1.isdigit()}')

''' index("P") -> 2 '''
print(f'course index for given character/substring is {course.index("P")}')

''' capitalize() -> "python for beginners" '''
print(f'course is capitalize {course.capitalize()}')

''' count("P") -> 1 '''
print(f'course given character count is {course.count("P")}')

''' isalnum() -> False '''
print(course.isalnum())

''' isalnum() -> True '''
print(course1.isalnum())

''' swapcase() -> "pYTHON FOR bEGINNERS" '''
print(course.swapcase())

''' find("z") -> -1 '''
print(f'{course.find("z")}')

''' find("Beginners") -> 12 '''
print(f'{course.find("Beginners")}')

''' replace('Python', 'Python3) -> "Python3 for Beginners" '''
print(course.replace('Python', 'Python3'))

''' print() course string value '''
print(f'{course}')

''' in operator with False condition '''
print(f'{"python" in course}')

''' in operator with True condition '''
print(f'{"Python" in course}')

print(f'original course2 is {course2}')
print(f'stripped off course2 string {course2.strip()}')

print(course + course1)
print(course * 8)
