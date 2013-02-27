version = 2.7
python = python$(version)

rmpyc:
	@rm -rfv   `find   woods   -name   *.pyc`

.PHONY: rmpyc
