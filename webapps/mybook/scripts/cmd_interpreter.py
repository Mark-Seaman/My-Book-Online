#!/usr/bin/python
from os         import system, chdir, getcwd
from sys        import argv

# Encapsulate a reusable command intepreter
class CommandInterpreter():
    def __init__ (self, command_dictionary, help_text):
        self.command_dictionary = command_dictionary
        self.help_text = help_text
    
    # List help for this script
    def show_help (self):
       print self.help_text 
       for c in sorted(self.command_dictionary):
            print "       ", self.command_dictionary[c]['label']

    # Print an error message and exit
    def error_exit(self, reason):
        print "Error: "+reason
        self.show_help()
        exit(1)  

    # Check to make sure that at least one argument is supplied
    def check_has_arguments(self):
        if len(argv) < 2 : 
            self.error_exit('no command given')

    # Check to make sure that at least one argument is supplied
    def check_argument_number(self, parms, details):
        if len(argv)-2 != parms: 
            self.error_exit('wrong number of arguments'+details)

    # Return the usage label
    def usage(self, command):
        return "\n   usage: "+self.command_dictionary[command]['label']
       
    # Create the proper text for the arguments given
    def check_arguments (self, argv):
        self.check_has_arguments()
        command = argv[1]
        if self.command_dictionary.has_key(command):
            parms = self.command_dictionary[command]['parms']
        else:
            self.error_exit('bad command, '+command)
        self.check_argument_number(parms, self.usage(command))
     

# Helper function to access the database contents for a model
def support_center_list (command):
    system ("manage.py "+command)
    exit (0)

# Invoke the command interpreter with the command line arguments
def command_interpreter(command_dictionary, help_text):
    CommandInterpreter(command_dictionary, help_text).check_arguments (argv)
    support_center_list (' '.join(argv[1:]))

