# Opening sample input
l = ".|...\....\n|.-.\.....\n.....|-...\n........|.\n..........\n.........\\n..../.\\..\n.-.-/..|..\n.|....-|.\\n..//.|...."
; = l.split()

l = [(list(x), 0) for x in l]


for x in l:
	print(x)

# start the coutn at 0
coutn = 0

def traverse(x, y, di):
	global coutn
	while (True):
	
		if l[x][1] == 0:
			coutn = coutn + 1
			l[x] = (l[x][0], 1)
			
			for z in l:
				print(z)

		try:
			match di:
				case 'left':
					
					match l[x][0][y - 1]:
						case '-':
							y -= 1
						case '\':
							x +=1
							di = 'up'
						case '/':
							x -= 1
							di = 'down'
						case '|':
							traverse(x + 1, y, 'up')
							x -= 1
							di = 'down'
					
					
				case 'right':
					match l[x][0][y + 1]:
						case '-':
							y += 1
						case '\':
							x +=1
							di = 'up'
						case '/':
							x -= 1
							di = 'down'
						case '|':
							traverse(x + 1, y, 'up')
							x -= 1
							di = 'down'
				case 'down':
					pass
				case 'up':			
					pass
		except:
			break	


traverse(0, 0, 'right')