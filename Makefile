.DEFAULT_GOAL := help

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: install
install: ## Install dependencies
	@pip install -r requirements.txt

.PHONY: deploy
deploy: ## Deploy project (migrate database)
	@python manage.py migrate

.PHONY: run
run: ## Run project server development
	@python manage.py runserver 0.0.0.0:8000

.PHONY: createuser
createuser: ## Create user (as superuser)
	@python manage.py createsuperuser

USER_STRING := "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@default.com', 'd3t4c4m3_challenge')"
.PHONY: createdefaultuser
createdefaultuser: ## Create user default (as superuser)
	@if echo $(USER_STRING) | python manage.py shell; then\
		echo succeeded; \
	else \
		echo Default user already exist; \
		echo username: "admin"; \
		echo password: "d3t4c4m3_challenge"; \
	fi
