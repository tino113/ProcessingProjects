#TomSpeak
from button import button
import subprocess

pages = []
pageTitles = []
currPage = 0
gapPerc = 80
gap = 10
titleHeightPerc = 30
titleHeight = 20
textAreaHeightPerc = 7.5
textAreaHeight = 80
toolbarHeightPerc = 6.7
toolbarHeight = 90
prevW = 0
prevH = 0
ml = 0
bl = 0
tl = 0
console = ''
buttons = []

def getClipboardData():
 p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
 retcode = p.wait()
 data = p.stdout.read()
 return data

def setClipboardData(data):
 p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
 p.stdin.write(data)
 p.stdin.close()
 retcode = p.wait()

def parseFolders(f):
        pageFiles = []
        # walk through all folders and sub folders
        for root, dirs, files in os.walk(f):
            for f in files:
                # if the file is a python file
                if os.path.splitext(f)[1] == '.txt' or os.path.splitext(f)[1] == '.csv':
                    pageFiles.append(f)
        return pageFiles

def loadPages(path,fs):
	pages = []
	for f in fs:
		pname = re.split('\.', f)[0]
		with open(path + '/pages/' + f, 'r') as fc:
			topic = ''
			for l in fc:
				noSpace = l.replace(' ','')
				noSpace = noSpace.replace('	','')
				l = l.replace('\n','')
				if l.find('<<') >= 0 and l.find('>>') >= l.find('<<'):
					topic = l[l.find('<<')+2:l.find('>>')]
					l = l.split('>>')[1]
				elif l.find('<') == 0 and l.find('>') >= l.find('<'):
					pageTitles.append({'topic':topic, 'title':l[l.find('<')+1:l.find('>')]})
					l = l.split('>')[1]
				elif l != '' or l != ' ':
					pageTitles.append({'topic':topic, 'title':''})

				l = l.replace(' , ',', ')
				l = re.sub(r'\s+', ' ', l)

				if not noSpace.find('#') == 0 and l != '':
					if not l.endswith(' '):
						l = l + ' '
					wList = re.split(',',l)
					pages.append(wList)
	return(pages)                     

def calcSizes(w,h):
	global gap
	global titleHeight
	global textAreaHeight
	global toolbarHeight
	global ml
	global bl
	global tl
	global tbl

	gap = ceil(w/gapPerc)
	titleHeight = ceil(h/titleHeightPerc)
	textAreaHeight = ceil(h/textAreaHeightPerc)
	toolbarHeight = ceil(h/toolbarHeightPerc)

	bl = createGraphics(w, h)
	ml = createGraphics(w, h)
	tbl = createGraphics(w, toolbarHeight) 
	tl = createGraphics(w, textAreaHeight)

def setup():
	global currPage
	global pages
	size(800,600)
	this.surface.setResizable(True)
	noCursor()
	currPage = 0

 	maxTries = 100
 	tries = 0
	foundPagesFolder = False
	path = os.getcwd()
	while not foundPagesFolder:
		files = parseFolders(path + '/pages')
		if not files == []:
			foundPagesFolder = True
		else:
			path = os.path.dirname(path)
			if path == '/' or tries >= maxTries:
				print('TomSpeak: No Pages Directory Found!')
				break
		tries += 1

	pages = loadPages(path,files)
	if pages == []:
		pageTitles.append({'topic':'No Topic', 'title':'No Title'})
		pageTitles.append({'topic':'No Topic', 'title':'No Title'})
		pages = [['load ','pages ']]
	background(0)
	clear()
	pg = pages[currPage]
	prevW, prevH = width, height
	calcSizes(width,height)
	drawBoxes(bl,tbl,pg)

def getTextSize(bl,pg,boxW,boxH):
	longestL = 0
	longestW = ''
	for word in pg:
		if len(word) > longestL:
			longestL = len(word)
			longestW = word
	tsize = 200
	bl.textSize(tsize)
	widthLW = bl.textWidth(longestW)
	heightLW = bl.textAscent() + bl.textDescent()
	while widthLW > boxW - gap*3 or heightLW > boxH - gap*3:
		tsize -=1
		bl.textSize(tsize)
		widthLW = bl.textWidth(longestW)
		heightLW = bl.textAscent() + bl.textDescent()

def drawBoxes(bl,tbl,pg,fcol = color(64),scol = color(40),txcol = color(230),sdepth = 3,rnd = 10):
	global buttons
	#calcSizes(width,height)
	bl.beginDraw()
	bl.clear()
	bl.noStroke()
	buttons = []
	rows, cols = 0, 0
	remain = len(pg)
	cols = ceil(sqrt(remain))
	rows = ceil(remain/cols)
	if not remain%2 == 0:
		rows += 1
	totalW = width - ((cols+1)*gap)
	totalH = height - ((rows+1)*gap) - textAreaHeight - toolbarHeight - titleHeight
	boxW = totalW/cols
	boxH = totalH/rows
	hbW = boxW/2
	hbH = boxH/2
	currX = gap
	currY = gap
	offset = 0
	count = 0
	bl.textAlign(CENTER,CENTER)
	getTextSize(bl,pg,boxW,boxH)
	for row in range(rows):
		tcol = cols
		if remain < cols:
			tcol = remain
			offset = (cols - remain) * boxW / 2
		for col in range(tcol):
			text = str(pg[count])
			ttext = text
			if ttext.endswith(' '):
				ttext = str(ttext[:-1])
			# shadow
			bl.fill(scol)
			bl.rect(currX+offset+sdepth,currY+titleHeight+sdepth,boxW-sdepth,boxH-sdepth,rnd,rnd,rnd,rnd)
			# box
			bl.fill(fcol)
			bl.rect(currX+offset,currY+titleHeight,boxW-sdepth,boxH-sdepth,rnd,rnd,rnd,rnd)
			# text
			
			# text Shadow
			bl.fill(scol)
			bl.text(ttext,currX+offset+hbW+sdepth,currY+titleHeight+hbH+sdepth)
			# text
			bl.fill(txcol)
			bl.text(ttext,currX+offset+hbW,currY+titleHeight+hbH)
			# invisible hitbox
			buttons.append(button(lambda: True,text,currX+offset,currY+titleHeight,boxW,boxH,'word'))
			currX += gap + boxW
			remain -= 1
			if count < len(pg):
				count += 1
		currY += gap + boxH
		currX = gap
	bl.endDraw()
	drawTitles(bl,pageTitles[currPage],titleHeight)
	drawToolbar(tbl,toolbarHeight)
	drawTextArea(bl,textAreaHeight)

def drawTextArea(bl,taHeight,tacol = color(32)):
	bl.beginDraw()
	bl.noStroke()
	bl.fill(tacol)
	bl.rect(0,height-taHeight,width,taHeight)
	bl.endDraw()

def drawTitles(bl,titleDict,tlHeight,tlcol = color(240)):
	bl.beginDraw()
	bl.noStroke()
	bl.fill(tlcol)
	text = titleDict['topic'] + ' - ' + titleDict['title']
	bl.textAlign(CENTER,TOP)
	bl.textSize(tlHeight)
	bl.text(text,width/2,0)
	bl.endDraw()

def incCurrPage():
	global currPage
	global bl
	global tbl
	currPage += 1
	if currPage >= len(pages):
		currPage = 0
	pg = pages[currPage]
	drawBoxes(bl,tbl,pg)

def decCurrPage():
	global currPage
	global bl
	global tbl
	currPage -= 1
	if currPage < 0:
		currPage = len(pages)-1
	pg = pages[currPage]
	drawBoxes(bl,tbl,pg)

def clearConsole():
	global tl
	global console
	console = ''
	drawText(tl)

def copyConsole():
	global console
	setClipboardData(console)

def clearCopyConsole():
	global tl
	global console
	copyConsole()
	clearConsole()

def newline():
	global console
	console += '\n '

def drawToolbar(tbl,tbHeight,tbcol = color(25),btncol = color(64),txcol = color(230),rnd = 10):
	tbl.beginDraw()
	tbl.noStroke()
	tbl.fill(tbcol)
	tbl.rect(0,0,width,tbHeight)
	tbl.textAlign(CENTER,CENTER)
	

	xPos = gap
	tbBns = 6
	btnW = (width-(gap*(tbBns+1)))/tbBns
	hBtnW = btnW/2
	hTbH = tbHeight/2
	dGap = gap*2
	btnH = tbHeight-dGap
	YPos = gap+(height-textAreaHeight-tbHeight)
	getTextSize(tbl,['New Line'],btnW,btnH)
	# Back Page
	tbl.fill(btncol)
	tbl.rect(xPos,gap,btnW,btnH,rnd,rnd,rnd,rnd)
	tbl.fill(txcol)
	tbl.text('< Bck', xPos+hBtnW,hTbH )
	buttons.append(button(decCurrPage,'',xPos,gap+(height-textAreaHeight-tbHeight),btnW,btnH))
	xPos += btnW + gap
	# Copy + Clear
	tbl.fill(btncol)
	tbl.rect(xPos,gap,btnW,btnH,rnd,rnd,rnd,rnd)
	tbl.fill(txcol)
	tbl.text('Cpy/Clr', xPos+hBtnW,hTbH )
	buttons.append(button(clearCopyConsole,'',xPos,gap+(height-textAreaHeight-tbHeight),btnW,btnH))
	xPos += btnW + gap
	# Copy
	tbl.fill(btncol)
	tbl.rect(xPos,gap,btnW,btnH,rnd,rnd,rnd,rnd)
	tbl.fill(txcol)
	tbl.text('Copy', xPos+hBtnW,hTbH )
	buttons.append(button(copyConsole,'',xPos,gap+(height-textAreaHeight-tbHeight),btnW,btnH))
	xPos += btnW + gap
	# Clear
	tbl.fill(btncol)
	tbl.rect(xPos,gap,btnW,btnH,rnd,rnd,rnd,rnd)
	tbl.fill(txcol)
	tbl.text('Clear', xPos+hBtnW,hTbH )
	buttons.append(button(clearConsole,'',xPos,gap+(height-textAreaHeight-tbHeight),btnW,btnH))
	xPos += btnW + gap
	# New Line
	tbl.fill(btncol)
	tbl.rect(xPos,gap,btnW,btnH,rnd,rnd,rnd,rnd)
	tbl.fill(txcol)
	tbl.text('New Line', xPos+hBtnW,hTbH )
	buttons.append(button(newline,'',xPos,gap+(height-textAreaHeight-tbHeight),btnW,btnH))
	xPos += btnW + gap
	# Forward Page
	tbl.fill(btncol)
	tbl.rect(xPos,gap,btnW,btnH,rnd,rnd,rnd,rnd)
	tbl.fill(txcol)
	tbl.text('Fwd >', xPos+hBtnW,hTbH )
	buttons.append(button(incCurrPage,'',xPos,gap+(height-textAreaHeight-tbHeight),btnW,btnH))
	xPos += btnW + gap

	tbl.endDraw()

def drawText(tl,text = '',tsize = 24):
	tl.beginDraw()
	tl.clear()
	tl.textSize(tsize)
	tl.fill(color(255))
	tl.noStroke()
	tl.textAlign(LEFT,TOP)
	# split into words
	split = re.split(' ',text)
	currX, currY = 0, 0
	for w in split:
		wWidth = tl.textWidth(w) + tl.textWidth(' ')
		if currX + wWidth > width:
			currX = 0
			currY += tsize
		if w.find('\n') >= 0:
			currX = 0
			currY += tsize
		else:
			tl.text(w,currX,currY)
		currX += wWidth
	tl.endDraw()

def drawMousePointer(ml,size = 30):
	ml.beginDraw()
	ml.clear()
	ml.stroke(color(255,255,255,150))
	ml.strokeWeight(size)
	ml.point(mouseX,mouseY)
	ml.endDraw()

def draw():
	global prevH
	global prevW
	global bl
	global tbl
	clear()
	image(bl,0,0)
	image(tbl,0,height-textAreaHeight-toolbarHeight)
	image(tl,0,height-textAreaHeight)
	drawMousePointer(ml)
	image(ml,0,0)

	if prevW != width or prevH != height:
		calcSizes(width,height)
		pg = pages[currPage]
		drawBoxes(bl,tbl,pg)
	prevW, prevH = width, height

def mouseReleased():
	global console
	global tl
	for btn in buttons:
		if btn.over():
			if btn.type == 'word':
				console += btn.word
			else:
				btn.function()
	drawText(tl,console)
	#pg = pages[currPage]
	#drawBoxes(bl,pg)