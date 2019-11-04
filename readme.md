### Instructions for running flask and API exmaples:

1. Make a new folder that will be your workspace (pref within your existing codefirst folder).
2. Open up your terminal and type <br><code>$ git init</code>
3. Clone the repository containing the code example using the command:
<code>$ git clone https://github.com/Expan75/codefirst_examples.git</code> 
<br><br>This will create a new folder ('codefirst' underscore 'examples') in your working directory that contains all the code in the repository.

--
### To run the examples, follow the steps below:

1. Make sure you have all the code that is visible in the repo.

2. Make sure you have all the required packages & modules. To ensure that you do, open a terminal and type <code>$ pip install -r requirements.txt </code>

3. Type pip list to check that it worked (inspect the requirements.txt file to double if the right versions were downloaded).

4. make sure you standing in <code>/codefirst_examples/</code> directory.

5. Start the flask application using: <code>$ flask run</code>

6. Navigate to the address given in the terminal (mine was http://127.0.0.1:5000/, but it might differ) using your favourite browser.
7. Assuming hello world showed up, now try a the <code>/scootero</code> path
8. Enter a location in the form and press locate :)

--
# Learning Outcomes

<p> Try to understand what the script is doing. If you want to purely have a look at the api part (the part that uses requests) you can try running the api1.py script. Play around with it until you're confident about what happens. Then try going back to the <code>app.py</code> code and go step by step, alternatively adding pring statements to check what happens and <i>when it happens. </p></i>

### Toubleshooting


While there could be many issues while runnning the examples, probably it has to do with your Python version.

This sample is written with the intention of running python 3.7

If you run 2.+ you might need to edit some code in order to get everything running. That being said, 
the concepts, structure, and libraries, are fairly similar regardless of python version.

Another issue that you might run into is a "module not found error", this simply means that Python can locate the neccessary packages (that Python tries to import because you told it to, i.e. import statements). 

Luckily there's an easy fix! Open your terminal (make sure you are in the write directory), and simple type

<code>$ pip install -r requirements.txt </code>

This will install the libraries/modules specified in the requirements.txt file! Make you sure you have a look at the file. This is generally how people ensure that other entities (people or systems), have the right dependencies (the stuff necceccary to run the other stuff). You can generate your own requirements.txt file using the command:

<code>$ pip freeze > requirements.txt</code>

This will pull down all the modules (and their exact version) into a format that other peoples' pip:s can utilise!

--

### If it comes to the worst, make sure you message the instructors or talk to them in classs. Good luck!