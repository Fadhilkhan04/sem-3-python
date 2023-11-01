try :
  f = open("demofile.txt","r")

  for l in f :
    words = l.split()
    print("\nLine from the file :",l)
    print("Number of words in this line :",len(words))

    word_count = {}
    duplicate = []

    for word in words:
      word = word.lower()
      if word in word_count :
        word_count[word] += 1
        
        if word_count[word] == 2 :
          duplicate.append(word)
          
      else :
        word_count[word] = 1
      
    if duplicate :
      print("Duplicate words in this line is :",duplicate)
      print("maximum duplicate found in this line is :",max(word_count[word] for word in duplicate))
    
    else :
      print("there is no duplicate in this line")

except FileNotFoundError:
  print("file not found")
except Exception as e :
  print("an error has occured :",str(e))


