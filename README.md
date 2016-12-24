# find_key
Judge the key from the sound in the song.

# usage
python find_key.py sound1 sound2 soundn...

# sample
```sh
~/find_key> python find_key.py C C#
['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']
['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']
```

```sh
~/find_key> python find_key.py C C# D
not found key
```

# enviroment
```sh
 ~/find_key> python --version
Python 2.7.10
```
