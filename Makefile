PYLINT_FLAGS= -rn
PY_FILES ?= $$(git ls-files '*.py')


lint:
	pylint $(PYLINT_FLAGS) $(PY_FILES)
