def generate_concept(title, description):
	html1 = '''
<div class="concept">
	
	<h3>
		''' + title
	html2 = '''
	<h3>
	
	<p>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
		''' + description
	html3 = '''
	<p>

</div>
		
		<a href="#beginning">Back to Top</a>
		'''
	
	all_html = html1 + html2 + html3
	return all_html
	
def make_concept(concept):
	title = concept[0]
	description = concept[1]
	return generate_concept(title, description)
	
def make_all_html(concepts):
	HTML = ""
	for concept in concepts:
		concept_HTML = make_concept(concept)
		HTML = HTML + concept_HTML
	return HTML

# This list doesn't work. Python picks up every single in, for, while, etc. and highlights it blue despite it all
# being strings. As far as I can tell it's because they're long strings with other punctuation in them. This 
# makes using my actual notes with this HTML generator practically impossible, and so I've put in a simple test 
# list below. I can no longer count the number of problems with lists I've come across that aren't explained even 
# slightly in the course material. More frustratingly, I did a great deal of work on a more complicated version
# of all of this code, only to have issues with lists which have forced me to use this project as a fall back.
#content = [
#	['Python Variables', 'Variables are a way to name certain values in Python. This is helpful because it 
#	improves code readability, but also functionally, as it allows values to change.'],
#	['Equals Symbol (=)', 'Equals symbols have a different meaning in Python than in math. In Python they mean
#	['Strings', 'In Python, strings are enclosed within single or double quotations. Either work, but the 
#	closing and ending type must match. Things within a string will not be recognized as numbers.'],
#	['Functions', 'Functions take some input and do something to it, producing an output. 
#	A function could, for example, add two numbers no matter what those numbers are.'],
#	['Parts of a Function', 'Functions are started by the keyword def followed by the name of the 
#	function. This is then followed by the functions parameters in 
#	parenthesis immediately following the functions name, separated by commas and ended 
#	with a colon. Next is the body of the function, which is what the function is going 
#	to do to the parameters. When printing the result of a function you print the 
#	name of the function, followed by the values which are to take the place of the parameters
#	in the function.'],
#	['Functions and Repetition', 'Functions help to avoid repetition because it only needs to be defined once. A 
#	function which adds two numbers can be called upon any time that two numbers need adding within the code 
#	without redefining it.'],
#	['Return Statements', 'Return statements tell Python exactly what a function should produce as output. 
#	For example, if the body of a function was that a + b = c then the return statement should either be 
#	"return c", or simply put all of it in the return statement like "return a + b".'],
#	['If', 'If statements are statements used in Python to make code do something different depending
#	upon the result of a comparison. Indented within an if statement is a block which contains what the 
#	code will do if the if statement evaluates to true.'],
#	['Else', 'Else statements are used in addition to if statements to tell code what to do if the if statement 
#	evaluates to false. Else statements are along the same indentation as the same if statement and also have
#	an indented block within them.'],
#	['While Loops', 'While loops are another Python statement which do something multiple times. You set a condition 
#	under which it will continue, and it will continue until the input no longer meets that condition.'],
#	['Debugging Tips, If code is causing an error, it's best to start by examining the error message. The last line 
#	usually gives the best information to help you figure out the problem. It's also helpful to 
#	compare your code to working examples of similar code, and to check that whatever code you
#	may have based yours upon works also. It's most difficult to figure out an issue when the code
#	doesn't produce any error, but doesn't do what you want it to. In many cases it's helpful when
#	debugging something like this to print individual parts of your code to see what isn't working 
#	exactly.']
#]

content = [
	['Python', 'Python is a Programming language'],
	['For Loop', 'For Loops allow you to iterate over lists'],
	['Lists', 'Lists are sequences of data']
]
	
all_content = make_all_html(content)

print (all_content)
