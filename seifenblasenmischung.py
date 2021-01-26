scores = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]

i = 0   # eine Variable erstellen, die en aktuellen Index (beginnend bei 0) enthält

length_scores = len(scores)


for i in range(length_scores):
    print('Bubble solution #' + str(i), 'score:', scores[i])

## Eine Alternative dazu:
## while i < length_scores:        #eine Schleife über die Listenelemente ausführen, solange der Index kleiner ist als die Länger der Liste
## print('Bubble solution #' + str(i), 'score:', scores[i]) 
##  i = i + 1                      # zum Schluss inkrementieren wir den Index i um  eins, bevor die Schleife erneut durchlaufen wird

print('')   #to give some space between the lines

print('the length of the list is', length_scores)

print('')
 
highest_score = max(scores)
print('the highest bubble score is ', highest_score)

print('')

best_solutions = []

for i in range(length_scores):
    if highest_score == scores[i]:
        best_solutions.append(i)

print('Solutions with the highest score:', best_solutions)

print('')

lowest_score = min(scores)
print('the lowest bubble score ist ', lowest_score)

print('')

worse_solution = []

for i in range(length_scores):
    if lowest_score == scores[i]:
        worse_solution.append(i)

print('Solution with the lowest score:',worse_solution)


##Alternative um die high and low score zu bekommen
## high_score = 0 
## if scores[i] > high_score
## high_score = scores[i]
## print['Highest bubble score:', high_score)

##------------------/////------------------------

##  Die Kosteneffektiveste SEifenblasenmischung

# eine LIste mit den KOsten für jede SEifenblasenmischung

costs = [.25, .27, .25, .25, .25, .25,
         .33, .31, .25, .29, .27, .22,
         .31, .25, .25, .33, .21, .25,
         .25, .25, .28, .25, .24, .22,
         .20, .25, .30, .25, .24, .25,
         .25, .25, .27, .25, .26, .29]

print('')

cost = 100.0       #eine Variable erstellen, die die KOsten der Kosteneffektiveste Mischung enthält. Ihr Wert ist größer als alle Elemente in costs.
most_effective = 0 

for i in range(len(best_solutions)): #wir iteririeren über die best_solutions Liste
    index = best_solutions[i]       #benutzen die einzelnen Elementen aus best_solutions als Indizes für die costs LIste 
    if cost > costs[index]:        #wie untersuchen die Mischung in der best_solution Liste, um die Mischung mit den niedrigsten Kosten zu finden
        most_effective = index
        cost = costs[index]
        
print('Solution',most_effective, 'is the most effective with a cost of',costs[most_effective ] )


#eine Alternative dazu:
# 	for i in range (length_scores): 
    #über alle Mischungen iterieren und herausfinden, ob eine den Höchststand hat...
#	if scores[i] == highest_score and costs[i]<= cost: 
    # und niedrigere KOsten als die vorigen Mischungen 
#	most_effective = i 
    # dann den Index und die Kosten der aktuellen MIschung speichern
#	cost = costs [i]
	
#	print('Solution',most_effective, 'is the most effective with a cost of', costs[most_effective])
	

##-------/////-------//////-------

#nested loop (verschaltete Schleife)
#sort the the 5 best Results


print('')


def bubble_sort(scores, numbers):  #hier die Funktion, die eine Python-liste übernimmt.
    swapped = True        #wir setzen die Variable swapped auf True, um den ersten Durchgang zu starten.

    while swapped:        #Die verschaltete Schleife: eine for-Schleife in einer while-Schleife
        swapped = False   #die while-Schleife wird so lange ausgeführt, wir die swapped den Wert True hat 
        for i in range (0, len(scores)-1):   # wir gehen den gesamte Liste durch, um die Werte zu vergleichen
            if scores [i] < scores [i+1]:    #und bei Bedarf zu vertauschen
                temp = scores [i]
                scores [i] = scores [i+1]
                scores [i+1] = temp
        #---------------------------------------#
                temp = numbers[i]            # beim Tausch zweier Werte in der scores-Liste 
                numbers[i] = numbers[i+1]    # die entsprechenden Werte in der numbers-Liste tauschen
                numbers[i+1] = temp
                swapped = True


solution_numbers = list(range(length_scores))

bubble_sort(scores, solution_numbers)

print('Top Bubble Solutions are:')
for i in range (0,5):
    print(str(i+1)+')',
          'Bubble solution #' + str(solution_numbers[i]),
          'score:', scores[i])
    












