from sys import exit
from time import sleep
import constants

sleep(0.5)

melody = input("Please input your melody/series of notes, with each note separated by a space. Please format each note as either a natural or a sharp (no flats). ").upper()
melody = melody.split(" ")
for note in melody:
    if note not in constants.notes:
        print("Sorry, one of your inputted notes was not valid. Please try again.")
        exit()

home = input("What fret would you like your melody to be closest to? ")
try:
    home = int(home)
    if home > 22 or home < 0:
        raise Exception
except:
    print("Sorry, the fret you inputted was either higher than 22 or wasn't a valid integer. ")
    exit()

# the length is multiplied by 2 to add padding for the tabs (always a space between each note)
tablature = []
for i in range(6):
    tablature.append([])
    for _ in range(len(melody) * 2 + 1):
        tablature[i].append("-")

# finding most efficient fingering for each note
for note in melody:
    # (string index, fret number)
    lowest = (0, 100)

    for string in range(len(constants.fretboard)):
        for fret in range(len(constants.fretboard[string])):
            if lowest[1] == 0:
                break
            if note == constants.fretboard[string][fret]:
                # if the fret number is closest to the home position or if the note is an open string
                if abs(fret - home) < abs(lowest[1] - home) or fret == 0:
                    lowest = (string, fret)

    tablature[lowest[0]][melody.index(note) * 2 + 1] = str(lowest[1])
    melody[melody.index(note)] = (-1, -1)

# tablature standard is to start at the high E string and go down, but the fretboard was stored with
# the low E string on top to help with keeping the notes in the same octave when finding matches
tablature.reverse()
for i in tablature:
    print("".join(i))