notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

fretboard = [
    ["E"],
    ["A"],
    ["D"],
    ["G"],
    ["B"],
    ["E"]
]

# populating fretboard with notes
for string in fretboard:
    start = notes.index(string[0])
    for i in range(1, 21):
        string.append(notes[(start + i) % len(notes)])