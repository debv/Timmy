Timmy
=================

Timmy is a UNIX terminal personal assistant for note-taking. 

Timmy can help you create notebooks to organize all of your notes right in your Dropbox folder for easy access anywhere allowing you to edit, create and delete them as needed right from your terminal.

**Timmy in the Present**

Albeit a little lackluster, Timmy is fully functional right now. Timmy automatically stores all notebooks and their notes in your Dropbox (assuming you have it in the default install path for Mac OS X and Linux) in the path ``/Users/<USERNAME>/Dropbox/Timmy/notes``.  It uses Vim as the default editor for editing/opening notes. Timmy is case sensitive especially with file names so make sure you ``-l`` to view your notes in case you forget how it was titled before trying to modify it (otherwise Timmy will just tell you it doesn't exist). Scroll to the bottom to read about what Timmy wants to be when it grows up.

**Working with Timmy**

To run Timmy:

From your terminal make sure you are in the directory you put ``timmy.py`` in and type the following::

    python timmy.py

Once Timmy is running, you will see the following::

    Timmy:

To view a list of all of the commands Timmy accepts::

    Timmy: -h

To quit::

    Timmy: -q

**Interacting with Notebooks**

List all existing notebooks::

    Timmy: -l

Create a new notebook::

    Timmy: -n FOO

Open an existing notebook::

    Timmy: -o FOO

Delete an existing notebook (and the notes inside of it)::

    Timmy: -d FOO

**Interacting with Notes**

When you open a notebook, Timmy will change from::

    Timmy:

to::


    Timmy(Notebook FOO):

This change indicates the notebook you are currently in. To make changes to any notes, you must first open the notebook they are in. Once you see ``Timmy(Notebook FOO):`` you can begin modifying the notes inside of the notebook.

List all notes within an open notebook::

    Timmy(Notebook FOO): -l

Create a new note::

    Timmy(Notebook FOO): -n BAR

Open an existing note::

    Timmy(Notebook FOO): -o BAR

Delete an existing note::

    Timmy(Notebook FOO): -d BAR


**Switching from Interacting with Notes to Interacting with Notebooks**

Closing a notebook:

To stop modifying notes and return to being able to modify and interact with notebooks, you must close the notebook you are currently in by using ``-c``::

     Timmy(Notebook FOO): -c

Once you close the notebook, Timmy will return to looking like this::

    Timmy:

**Timmy in the Future**       

Timmy is just a baby right now and I plan on improving on existing features and adding other features soon so that it can grow and be even more useful and neat. Eventually you will be able to use an editor other than Vim and you will be able to install and upgrade Timmy using ``pip install`` among other things (but not yet).

**Future Updates/Improvements/Features**

- Install and upgrade Timmy using ``pip install``
- Customizable defaults for editor and save path
- Delete multiple notebooks at once with ``-d`` command
- Delete multiple notes at once with ``-d`` command
- Search for keywords and return notes/notebooks that contain them
- To-do feature for creating and tracking to-do lists
- Optimize for large amounts of notebooks/notes