PYTHON ?= python3
PANDOC ?= pandoc
JUPYTER ?= jupyter
PDFLATEX ?= pdflatex
SOURCE_DATE_EPOCH ?= 1767225600

.PHONY: all test notebook slides paper package clean

all: test notebook slides paper package

test:
	PYTHONPATH=materials/exercise_repo $(PYTHON) -m pytest -p no:cacheprovider materials/exercise_repo/tests/test_visible.py -q
	PYTHONPATH=materials/architecture_repo $(PYTHON) -m pytest -p no:cacheprovider materials/architecture_repo/tests -q
	PYTHONPATH=materials/transfer_repo $(PYTHON) -m pytest -p no:cacheprovider materials/transfer_repo/tests -q
	$(PYTHON) -m unittest discover -s materials/pilot -p 'test_*.py'
	$(PYTHON) tools/validate_teaching_behavior.py
	$(PYTHON) materials/pilot/analyze_pilot.py materials/pilot/pilot_data.csv

notebook:
	mkdir -p build/notebooks
	$(JUPYTER) nbconvert --to notebook --execute materials/notebooks/verifier_feedback_loop.ipynb --output verifier_feedback_loop.executed.ipynb --output-dir build/notebooks --ExecutePreprocessor.timeout=120
	$(PYTHON) tools/normalize_notebook.py build/notebooks/verifier_feedback_loop.executed.ipynb
	$(JUPYTER) nbconvert --to html build/notebooks/verifier_feedback_loop.executed.ipynb --output verifier_feedback_loop.executed.html --output-dir build/notebooks --HTMLExporter.embed_images=True
	cp build/notebooks/verifier_feedback_loop.executed.ipynb materials/notebooks/verifier_feedback_loop.ipynb
	cp build/notebooks/verifier_feedback_loop.executed.html materials/notebooks/verifier_feedback_loop.html

slides:
	cd materials/slides && $(PANDOC) verifier_feedback_loops.md --standalone --to=dzslides --embed-resources --css=slides.css --output=verifier_feedback_loops.html
	cd materials/slides && TZ=UTC SOURCE_DATE_EPOCH=$(SOURCE_DATE_EPOCH) FORCE_SOURCE_DATE=1 $(PANDOC) verifier_feedback_loops.md --to=beamer --pdf-engine=$(PDFLATEX) --variable=aspectratio:169 --output=verifier_feedback_loops.pdf
	cd materials/slides && $(PANDOC) verifier_feedback_loops.md --to=pptx --output=verifier_feedback_loops.pptx

paper:
	cd paper && TZ=UTC SOURCE_DATE_EPOCH=$(SOURCE_DATE_EPOCH) FORCE_SOURCE_DATE=1 $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cd paper && TZ=UTC SOURCE_DATE_EPOCH=$(SOURCE_DATE_EPOCH) FORCE_SOURCE_DATE=1 $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex

package:
	$(PYTHON) tools/package_release.py

clean:
	$(PYTHON) -c 'from pathlib import Path; import shutil; path=Path("build"); shutil.rmtree(path) if path.exists() else None'
