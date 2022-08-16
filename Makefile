usage:
	@echo "======================================================================"
	@echo "usage (default) : display this menu"
	@echo "migration       : make migration and run it"
	@echo "test            : run tests"
	@echo "github          : push source code to github.com"
	@echo "======================================================================"

migration:
	@python3 manage.py makemigrations
	@python3 manage.py migrate

test:
	@python3 $(CURDIR)/manage.py test

github:
	@git status
	@git add .
	@git commit -m 'update'
	@git push
