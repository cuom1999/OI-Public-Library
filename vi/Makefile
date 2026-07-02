SHELL := /bin/bash

TEXMFVAR ?= /tmp/texmf-var
TEXINPUTS := .:$(CURDIR)//:
LATEX := env TEXMFVAR=$(TEXMFVAR) TEXINPUTS="$(TEXINPUTS)" lualatex -interaction=nonstopmode -halt-on-error

SOURCES := $(shell find sources -name '*.tex' | sort)
PDFS := $(patsubst %.tex,build/%.pdf,$(SOURCES))

.PHONY: all clean list

all: $(PDFS)

list:
	@printf '%s\n' $(PDFS)

build/%.pdf: %.tex oipl-vn.sty
	@mkdir -p $(dir $@)
	$(LATEX) -output-directory=$(dir $@) $<
	$(LATEX) -output-directory=$(dir $@) $<

clean:
	rm -rf build
