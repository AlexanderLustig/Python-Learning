with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
      for line in rf:
         wf.write(line)
    
    #f.write('Test')
    #f.seek(0)
    #f.write('R')



#with open('test.txt', 'r') as f:

   # size_to_read = 10

    #f_contents = f.read(size_to_read)
    #print(f_contents, end='')

 #   f.seek(0)

  #f_contents = f.read(size_to_read)
    #print(f_contents, end='')

  #  print(f.tell())

    #while len(f_contents) > 0:
     #   print(f_contents, end='*')
      #  f_contents = f.read(size_to_read)
    
   # for line in f:
    #    print(line, end='')
    
 #   f_contents = f.readline()
  #  print(f_contents, end='')

   # f_contents = f.readline()
   # print(f_contents, end='')

