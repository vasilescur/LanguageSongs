def fudge(string):
 stringlist = string.split('\n')
 newlist = []

 for string in stringlist:
  line = string.split(" ")
  linelist = []
  for word in line:
   starting = '<span class="translatable"gi>'
   ending = '</span>'
   linelist.append(starting+word+ending)
  newlist.append(' '.join(linelist))
 string = '<br>'.join(newlist)
 return string

if __name__ == "__main__":
 string = "\n\n[Pre-Refrain]\nDu, du hast\nDu hast mich\nDu, du hast\nDu hast mich\nDu, du hast\nDu hast mich\nDu, du hast\nDu hast mich\n\n[Refrain]\nDu, du hast\nDu hast mich, du hast mich\nDu hast mich gefragt, du hast mich gefragt\nDu hast mich gefragt und ich hab' nichts gesagt\n\n[Strophe]\nWillst du bis der Tod euch scheidet\nTreu ihr sein für alle Tage?\nNein, nein!\nWillst du bis zum Tod, der Scheide\nSie lieben auch in schlechten Tagen?\nNein, nein!\n\n[Pre-Refrain]\nDu, du hast\nDu hast mich\nDu, du hast\nDu hast mich\nDu, du hast\nDu hast mich\nDu, du hast\nDu hast mich\n\n[Refrain]\nDu, du hast\nDu hast mich, du hast mich\nDu hast mich gefragt, du hast mich gefragt\nDu hast mich gefragt und ich hab' nichts gesagt\n\n[Strophe]\nWillst du bis der Tod euch scheidet\nTreu ihr sein für alle Tage\nNein, nein!\nWillst du bis zum Tod, der Scheide\nSie lieben auch in schlechten Tagen\nNein, nein!\nWillst du bis der Tod euch scheidet\nTreu ihr sein ...\nNein, nein!\n\n"
 
 print (fudge(string))