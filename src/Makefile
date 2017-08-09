TEX=platex
DVIPDF=dvipdfmx
#DVIPDFFLAGS=-pa4
DVIPS=dvips
PDF2PS=pdf2ps
PAPERSIZE=a5
PAPERSIZE_PRINT=a4

PREFIX=DevelopmentOfTMS
SRC_PREFIX=main
TEXF=${SRC_PREFIX}.tex
DVI=${SRC_PREFIX}.dvi
PS=${SRC_PREFIX}.ps
PDF=../${PREFIX}.pdf
BOOK=../${PREFIX}_print.pdf
TEXFILES=main.tex cover.tex intro.tex tms.tex sst.tex colophon.tex appendix.tex drawing.tex server.tex

.suffix: .tex .dvi

all: ${DVI}
#all: book

pdf: ${PDF}

ps: ${PS}

book: ${BOOK}


${DVI}: ${TEXFILES} ${PSFILES}
	rm -f sst.eps sst-ave.eps browser.eps
	ln -s sst_mono.eps sst.eps
	ln -s sst-ave_mono.eps sst-ave.eps
	ln -s browser_mono.eps browser.eps
	${TEX} main.tex
	${TEX} main.tex

${PDF}: ${DVI} 
	${DVIPDF} -p ${PAPERSIZE} -o ${BOOK} ${DVI}
	rm -f sst.eps sst-ave.eps browser.eps
	ln -s sst_color.eps sst.eps
	ln -s sst-ave_color.eps sst-ave.eps
	ln -s browser_color.eps browser.eps
	${TEX} main.tex
	${TEX} main.tex
	${DVIPDF} -p ${PAPERSIZE} -o ${PDF} ${DVI}

${PS}: ${PDF} 
	${PDF2PS} ${PDF} ${PS}

#${BOOK}: ${PS}
#	psbook ${PS} | psnup -2 -P ${PAPERSIZE}| ps2ps -sPAPERSIZE=${PAPERSIZE_PRINT} - - | ps2pdf - ${BOOK}


clean:
	rm -f ${DVI} ${PS} ${BOOK} ${PDF} *.log *.aux *~

