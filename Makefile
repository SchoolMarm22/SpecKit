.PHONY: test test-bias test-all lint serve web install prep

install:
	pip install -e ".[dev]"

test:
	pytest evals/ -v --ignore=evals/test_bias_swap.py -m "not slow"

test-all:
	pytest evals/ -v

test-bias:
	pytest evals/test_bias_swap.py -v

lint:
	spec lint --spec hiring/senior-frontend-platform

serve:
	spec serve

web:
	spec web

prep:
	spec prep --spec hiring/senior-frontend-platform --resume evals/fixtures/sample_resume.md --pretty
