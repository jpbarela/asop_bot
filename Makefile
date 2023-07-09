run:
	docker compose up

test:
	poetry run pytest

type-check:
	poetry run mypy -p asop_bot -p embeddings -p tests -p vectorstore
