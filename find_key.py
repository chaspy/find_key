# -*- coding: utf-8 -*-
import sys

# define key
C = ['C','D','E','F','G','A','B']
Cs = ['C#','D#','F','F#','G#','A#','C']
D = ['D','E','F#','G','A','B','C#']
Ds = ['D#','F','G','G#','A#','C','D']
E = ['E','F#','G#','A','B','C#','D#']
F = ['F','G','A','A#','C','D','E']
Fs = ['F#','G#','A#','B','C#','D#','F']
G = ['G','A','B','C','D','E','F#']
Gs = ['G#','A#','C','C#','D#','F','G']
A = ['A','B','C#','D','E','F#','G#']
As = ['A#','C','D','D#','F','G','A']
B = ['B','C#','D#','E','F#','G#','A#']
keys = [C,Cs,D,Ds,E,F,Fs,G,Gs,A,As,B]

def main():
  args = sys.argv
  if len(args) == 1:
    usage()
  args.pop(0)
  find_keys = find_key(args)
  print_result(find_keys)

def usage():
  print "USAGE:python find_key.py <sound1> <sound2> ... <soundn>"
  sys.exit()

def find_key(args):
  find_keys = []
  for key in keys:
    if set(key) > set(args):
      find_keys.append(key)
  return find_keys

def print_result(find_keys): 
  if len(find_keys) == 0:
    print "not found key"
  else:
    print "candidate(first sound is KEY):"
    for key in find_keys:
      print key

if __name__ == '__main__':
  main()

