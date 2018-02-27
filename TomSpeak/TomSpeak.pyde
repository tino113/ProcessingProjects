#TomSpeak

pages = []
page1 = ['this','is','some','test','words']
page2 = ['other','words','to','test','it','works']
currPage = 0
gap = 10
textAreaHeight = 150
ml = 0
bl = 0
tl = 0
console = ''

pages.append(page1)
pages.append(page2)

def setup():
	global currPage
	global ml
	global bl
	global tl
	size(800,600)
	this.surface.setResizable(True)
	noCursor()
	currPage = 0
	background(0)
	clear()
	pg = pages[currPage]
	bl = createGraphics(width, height)
	ml = createGraphics(width, height)
	tl = createGraphics(width, height)
	drawBoxes(bl,pg)
	
def drawBoxes(bl,pg,fcol = color(64),scol = color(40),txcol = color(230),sdepth = 3,rnd = 10):
	bl.beginDraw()
	bl.clear()
	bl.noStroke()
	rows, cols = 0, 0
	remain = len(pg)
	cols = ceil(sqrt(remain))
	rows = ceil(remain/cols)
	if not remain%2 == 0:
		rows += 1
	totalW = width-((cols+1)*gap)
	totalH = height-((rows+1)*gap)-textAreaHeight
	boxW = totalW/cols
	boxH = totalH/rows
	hbW = boxW/2
	hbH = boxH/2
	currX = gap
	currY = gap
	offset = 0
	count = 0
	bl.textAlign(CENTER,CENTER)
	for row in range(rows):
		tcol = cols
		if remain < cols:
			tcol = remain
			offset = (cols - remain) * boxW / 2
		for col in range(tcol):
			# shadow
			bl.fill(scol)
			bl.rect(currX+offset+sdepth,currY+sdepth,boxW-sdepth,boxH-sdepth,rnd,rnd,rnd,rnd)
			# box
			bl.fill(fcol)
			bl.rect(currX+offset,currY,boxW-sdepth,boxH-sdepth,rnd,rnd,rnd,rnd)
			# text
			bl.textSize(width/cols/4)
			# text Shadow
			bl.fill(scol)
			bl.text(str(pg[count]),currX+offset+hbW+sdepth,currY+hbH+sdepth)
			# text
			bl.fill(txcol)
			bl.text(str(pg[count]),currX+offset+hbW,currY+hbH)
			# invisible hitbox
			currX += gap + boxW
			remain -= 1
			count += 1
		currY += gap + boxH
		currX = gap
	bl.endDraw()
	drawTextArea(bl,textAreaHeight)

def drawTextArea(bl,textAreaHeight,tacol = color(32)):
	bl.beginDraw()
	bl.noStroke()
	bl.fill(tacol)
	bl.rect(0,height-textAreaHeight,width,textAreaHeight)
	bl.endDraw()

def drawText(tl,console = '',tsize = 20):
	tl.beginDraw()
	tl.clear()
	tl.textSize(tsize)
	# split into words
	split = re.split(console,' ')
	currX, currY = 0, 0
	for w in split:
		wWidth = tl.textWidth(w) + tl.textWidth(' ')
		if currX + wWidth > width:
			currX = 0
			currY += tsize * 2
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
	clear()
	image(bl,0,0)
	drawMousePointer(ml)
	image(ml,0,0)
	drawText(tl,console)
	image(tl,0,height-textAreaHeight)

def mouseClicked():
	pg = pages[currPage]
	drawBoxes(bl,pg)

def mouseReleased():
	pg = pages[currPage]
	drawBoxes(bl,pg)