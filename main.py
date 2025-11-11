from Player import MainChar
from Place import *
from commands import *
from printer import *
from utils import *
from singleActions import actOnSingleCommand
from doubleActions import actOnDoubleCommand

#currentInteraction = 'default'


printText(f'You are in {MainChar.currentPlace.atFirstGlance}.')

commandInput = input('What will you do?> ').strip().lower()

while commandInput != ('quit'):
    wordCountInCommand = 0
    for item in commandInput.split(" "):
        wordCountInCommand = wordCountInCommand + 1
    listOfCommands = commandInput.split(" ")
    if wordCountInCommand == 1 and commandInput in singleWordCommands:
        actOnSingleCommand(commandInput)

    elif wordCountInCommand == 2:
        verb = listOfCommands[0]
        noun = listOfCommands[1]
        if verb not in commandVerbs:
            printText('That command is not supported.')

        actOnDoubleCommand(verb, noun)

    else:
        printText('I do not understand that command.')

    commandInput = input('What will you do?> ').strip().lower()
