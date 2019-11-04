###

It might be that running this exact will not work on machine. 

While there could be many casuses of this, probably it has to do with your Python version.

This sample is written with the intention of running python 3.7

If you run 2.+ you might need to edit some code in order to get everything running. That being said, 
the concepts, structure, and libraries, are fairly similar regardless of python version.

Another issue that you might run into is a "module not found error", this simply means that Python can
locate the neccessary packages (that Python tries to import because you told it to, i.e. import statements). 

Luckily there's an easy fix! Open your terminal (make sure you are in the write directory), and simple type

$ pip install -r requirements.txt

This will install the libraries/modules specified in the requirements.txt file! Make you sure you have a look at the file. This is generally how people ensure that other entities (people or systems), have the right dependencies (the stuff necceccary to run the other stuff). You can generate your own requirements.txt file using the command:

$ pip freeze > requirements.txt

This will pull down all the modules (and their exact version) into a format that other peoples' pip:s can utilise!