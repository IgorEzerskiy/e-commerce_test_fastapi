run:
	alembic upgrade head
	python -m app.scripts.seed_roles
	uvicorn app.main:app --reload