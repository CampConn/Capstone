LATEX	= latex -shell-escape
BIBTEX	= bibtex
DVIPS	= dvips
DVIPDF  = dvipdft
XDVI	= xdvi -gamma 4
GH		= gv


SRC	:= $(shell egrep -l '^[^%]*\\begin\{document\}' *.tex)
TRG	= $(SRC:%.tex=%.dvi)
PSF	= $(SRC:%.tex=%.ps)
PDF	= $(SRC:%.tex=%.pdf)

#pdf: pdflatex -synctex=1 -interaction=nonstopmode main.tex

pdf: $(PDF)

ps: $(PSF)

$(TRG): %.dvi: %.tex 
	#one way of including source code is to use pygments
	
	#requires that you \include{pygments.tex} in your preamble

	$(LATEX) $<
	
	$(LATEX) $<
	$(LATEX) $<
	#remove the pygmentized output to avoid cluttering up the directory
	#rm __${SRC}.tex


$(PSF):%.ps: %.dvi
	$(DVIPS) -R -Poutline -t letter $< -o $@

$(PDF): %.pdf: %.ps
	ps2pdf $<

show: $(TRG)
	@for i in $(TRG) ; do $(XDVI) $$i & done

showps: $(PSF)
	@for i in $(PSF) ; do $(GH) $$i & done

zip:
	tar -cvjSf cs444_project1_28.tar.bz2 Makefile main.tex pygments.tex work_log.tex thread_c.c README.md main.pdf pst-tools.pro refs.bib IEEEtran.cls

all: pdf clean

clean:
	rm -f *.ps *.log *.aux *.out *.dvi *.bbl *.blg *.gz *.acn *.ist *.acr *.alg *.toc *.glg *.pyg

.PHONY: all show clean ps pdf showps
