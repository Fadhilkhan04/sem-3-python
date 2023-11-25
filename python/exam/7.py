# read a file and print number of duplicates

try :
  f = open("demo.txt","r")

  for l in f :
    words = l.split()
    print("line from the file is :",l)
    print("no of words in the line is :",len(words))

    word_count = {}
    duplicate = []

    for word in words :
      word = word.lower()
      if word in word_count:
        word_count[word] += 1
        if word_count[word] == 2:
          duplicate.append(word)
      else :
        word_count[word] = 1
    
    if duplicate :
      print("this line has duplicate:",duplicate)
      print("max occurances of duplicate is:", max(word_count[word] for word in duplicate))
    else :
      print("there is no duplicate in this line")



except FileNotFoundError:
  print("file not found")
except Exception as e:
  print("an error occured in:",str(e))