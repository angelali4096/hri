BIBTEX=bibtex
PDFLATEX=pdflatex
RM=rm -f
VIEWER=okular

TARGET=main.pdf
REFERENCES=references.bib

.PHONY: all clean rebuild
.SECONDARY:

# Phony targets
all: $(TARGET)

clean:
	$(RM) $(TARGET)

rebuild: ! clean all

# General-purpose targets
%.pdf: %.tex
	$(PDFLATEX) $*
	$(BIBTEX) $*
	$(PDFLATEX) $*
	$(PDFLATEX) $*
	$(VIEWER) $(TARGET)

# Document-specific targets
$(TARGET): $(REFERENCES)
