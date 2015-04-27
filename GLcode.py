def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="topic">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="text">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TOPIC:')
    end_location = concept.find('TEXT:')
    topic = concept[start_location+7 : end_location-1]
    return topic

def get_description(concept):
    start_location = concept.find('TEXT:')
    description = concept[start_location+5 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TOPIC:')
        next_concept_end   = text.find('TOPIC:', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept

TEST_TEXT = """TOPIC: Computer Science
TEXT: Computer science is a scientific and practical approach to both problem solving and programming.
Thinking in a mechanical way, by breaking down problems into smaller pieces or steps that can be solved as you go.
A computer scientist specializes in the theory of computation and design.
TOPIC: Programming languages.
TEXT: A computer program is simply a list of instructions that direct a computer on what to do and how to do it.
Because computers don't think, these instructions have to be very specific and in a specific language that the computer can understand.
These languages are programming languages, like C++ or Python. While it would be nice to use a language like english to program
a computer, our native languages are too ambigious for a computer to completely understand, until we achieve AI.
TOPIC: Python
TEXT: Python is a "programming language." It is an easy way to write computer code that has established data structures and definitions.
Python is a common and accepted computer language that I'm only just beginning to understand completely.
TOPIC: Print function
TEXT: The Print funciont within Python is the simpliest expression I know. It tells Python to print out the result or number that results 
from the program as written. Spaces between the print funcion and the item printed on the line don't matter.
TOPIC: Variables
TEXT:  Names can be used to keep track of many things, from numbers to text. When creating a variable, you
give the variable a name and then assign it some expression. The = sign is used to assign a named variable it's expression.
For example, the Speed of Light = 29979245. Variables can be altered by what the program tells it the new variable is. 
This is a powerful tool in making programs that can do many complicated things.
Other signs can be used to change the variables as well. The + sign will add something to the variable (ie: hours = hours + 1).
The * sign will do multiplication.
TOPIC: Strings
TEXT: Strings are a sequence of characters between single or double quotes. The quote types much match.
The + sign can add things to strings as well. Python can locate parts of a string by using the [] function.
It is important to remember that Python starts counting from 0 and not 1 when it looks at a string.
So when trying to find the first letter in a string, it is going to be stringname[0] and not [1]. The : will allow
us to find parts of a string from the starting position, to the stopping position, [0:5] for example.
TOPIC: Find operation
TEXT: The Find method can find any or all instances of what you are looking for in a string. The output of the find
is the position of the first occurance in the string. This is done with string.find(string). The find function can use
one or more parameters in it's find function, which greatly expands its use. Passing in a number can tell the find function
where in the string to start the search. 
TOPIC: Functions and Inputs
TEXT: The def funtion allows us to define a string using an input as entered by the user. Def string(n): allows us to define
a string by what we input into the program, which is n in this case, and since there is only one input, only one input will be accepted.
Def string(a,b,c) would be looking for 3 inputs when defining that string. 
With these inputs, we can use programming to alter that string and print out or return new results.
When making functions, PRINT gives the value to the users as an output string and the program loses the value. Whereas,
RETURN will give the value back to the program, so that internal functions can still work.
TOPIC: Flows and Loops
TEXT: If, While and For can make loops when programming in Python. This allows a function to occure over and over again
until some end function or endstate is met. If statements are like IF/THEN in basic. If a certain condition is met,
then return or print the outcome. If it is not met, then move to the next line of code. The While statement creates a loop
that will keep running, until the condition is shown to be false (while n < 0, for example). The For statement
will move through a collection of ready made inputs or lists and then completes."""


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(TEST_TEXT)

    