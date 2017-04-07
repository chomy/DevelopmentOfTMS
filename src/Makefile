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
BOOK=../${PREFIX}-print.pdf
TEXFILES=main.tex cover.tex intro.tex tms.tex sst.tex colophon.tex

.suffix: .tex .dvi

all: ${DVI}
#all: book

pdf: ${PDF}

ps: ${PS}

book: ${BOOK}


${DVI}: ${TEXFILES} ${PSFILES}
	${TEX} main.tex
	${TEX} main.tex

${PDF}: ${DVI} 
	${DVIPDF} -p ${PAPERSIZE} -o ${PDF} ${DVI}

${PS}: ${PDF} 
	${PDF2PS} ${PDF} ${PS}

${BOOK}: ${PS}
	psbook ${PS} | psnup -2 -P ${PAPERSIZE}| ps2ps -sPAPERSIZE=${PAPERSIZE_PRINT} - - | ps2pdf - ${BOOK}


clean:
	rm -f ${DVI} ${PDF} ${PS} ${BOOK} *.log *.aux *~

