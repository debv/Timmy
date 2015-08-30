#/-------------------------------------------------------------------------/
# Timmy - A UNIX terminal personal assistant for note-taking.
# Version: 1.0.0
#     Copyright (C) 2015,  Deborah Venuti
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#/-------------------------------------------------------------------------/

#!/usr/bin/env python
import getpass
import os
import sys
import shutil
import subprocess
from colorama import Fore, init

#/--------Help Function--------/#
def Help():
	print("\nTimmy - A UNIX terminal personal assistant for note-taking")
	print("\t-h \t Display this help Menu")
	print("\t-q \t Quit Timmy\n")
	print("\t-l \t List all notebooks | List notes in a notebook")
	print("\t-o \t Open a notebook | Open a note")
	print("\t-c \t Close a notebook")
	print("\t-n \t New notebook or note") 	#Notes can be any file type (.txt, .py etc...)
	print("\t-d \t Delete a notebook | Delete a note")
#/------------------------------/#

#/------Directory Function------/#
def directories(user):
	#Check if Timmy/notes exists, if it doesn't then create it
	#add error message if trying to create dirs but they already exist
	#at the time of installation (they shouldn't?)
	if not os.path.isdir('/Users/%s/Dropbox/Timmy/notes' % user):
		#print("DOESN'T EXIST") #TEST
		os.makedirs('/Users/%s/Dropbox/Timmy/notes' % user)
		#print("DIRECTORY CREATED") #TEST
		nDir = '/Users/%s/Dropbox/Timmy/notes' % user
		#print(nDir)
#/------------------------------/#

#/------Notebook Functions------/#
def listNotes(user, notebook):
	for notes in os.listdir('/Users/%s/Dropbox/Timmy/notes/%s' % (user, notebook)):
		if not notes.startswith('.'):
			print(notes)

def openNote(user, args, notebook):
	notes = os.listdir('/Users/%s/Dropbox/Timmy/notes/%s' % (user, notebook))
	if args[1] in notes:
		subprocess.call(['vim', '/Users/%s/Dropbox/Timmy/notes/%s/%s' % (user, notebook, args[1])])
	elif args[1] not in notes:
		print("This note does not exist.")

def newNote(user, args, notebook):
	for dirpath, dirname, files in os.walk('/Users/%s/Dropbox/Timmy/notes/%s' % (user, notebook)):
		if not files:
			subprocess.call(['vim', '/Users/%s/Dropbox/Timmy/notes/%s/%s' % (user, notebook, args[1])])
		else:
			notes = os.listdir('/Users/%s/Dropbox/Timmy/notes/%s' % (user, notebook))
			if args[1] not in notes:
				subprocess.call(['vi', '/Users/%s/Dropbox/Timmy/notes/%s/%s' % (user, notebook, args[1])])
			elif args[1] in notes:
				print("This note already exists.")

def deleteNote(user, args, notebook):
	notes = os.listdir('/Users/%s/Dropbox/Timmy/notes/%s' % (user, notebook))
	if args[1] in notes:
		init(autoreset = True)
		print(Fore.RED + "WARNING: You are about to delete the following note: %s" % args[1])
		confirm = raw_input("Are you sure you want to delete this note? Y/n ")
		if confirm == 'y':
			os.remove('/Users/%s/Dropbox/Timmy/notes/%s/%s' % (user, notebook, args[1]))
	elif args[1] not in notes:
		print("This note does not exist")

def modifyNotes(user, args, notebook):
	if args[0] == '-l':
		listNotes(user, notebook)
	elif args[0] == '-o':
		openNote(user, args, notebook)
	elif args[0] == '-n':
		newNote(user, args, notebook)
	elif args[0] == '-d':
		deleteNote(user, args, notebook)

def listNotebooks(user):
	for notebooks in os.listdir('/Users/%s/Dropbox/Timmy/notes' % user):
		if not notebooks.startswith('.'):
			print(notebooks)

def openNotebook(user, args, notebook):
	while args[0] != '-c':
		arg = raw_input("Timmy(Notebook %s): " % notebook)
		args = arg.split()
		modifyNotes(user, args, notebook)

def newNotebook(user, args):
	if not os.path.isdir('/Users/%s/Dropbox/Timmy/notes/%s' % (user, args[1])):
		os.makedirs('/Users/%s/Dropbox/Timmy/notes/%s' % (user, args[1]))
	else:
		print("This notebook already exists")

def deleteNotebook(user, args):
	for dirpath, dirname, files in os.walk('/Users/%s/Dropbox/Timmy/notes/%s' % (user, args[1])):
		if files:
			init(autoreset = True)
			print(Fore.RED + "WARNING: This notebook contains notes.")
			print(Fore.RED + "Deleting this notebook will also delete ALL notes inside.")
			confirm = raw_input("Are you sure you want to delete this notebook? Y/n ")
			if confirm == 'y':
				shutil.rmtree('/Users/%s/Dropbox/Timmy/notes/%s' % (user, args[1]))

		elif not files:
			confirm = raw_input("Are you sure you want to delete this empty notebook? Y/n ")

			if confirm == 'y':
				shutil.rmtree('/Users/%s/Dropbox/Timmy/notes/%s' % (user, args[1]))

def notebookMode(run, user, args):
	if args[0] == '-l':
		listNotebooks(user)

	elif args[0] == '-o':
		if len(args) < 2:
			print("ERROR: You must pick a notebook or note to open.")
		elif len(args) == 2:	#open a notebook and list notes inside of it
			notebook = args[1]
			openNotebook(user, args, notebook)

	elif args[0] == '-n':
		if len(args) < 2:
			print("ERROR: You must name a notebook or note")
		elif len(args) == 2:
			newNotebook(user, args)

	elif args[0] == '-d':
		if len(args) < 2:
			print("ERROR: You must name a notebook or note to delete")
		elif len(args) == 2:
			deleteNotebook(user, args)

	elif args[0] == '-q':
		run = False
		sys.exit()

#/------------------------------/#

def main():

	run = True
	user = getpass.getuser()
	args = []

	directories(user)

	while run == True:

		arg = raw_input("Timmy: ")
		args = arg.split()
		notebookMode(run, user, args)

		if arg == '-h':
			Help()
		elif arg == '-q':
			run = False
			sys.exit()


if __name__ == "__main__":
	main()