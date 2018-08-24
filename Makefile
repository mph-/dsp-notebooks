NBS = $(wildcard *.ipynb)

NEWNBS = $(NBS:.ipynb=-new.ipynb)

all: $(NEWNBS)

%-new.ipynb: %.ipynb
	jupyter nbconvert --to notebook --execute $< --output=$@

# jupyter nbconvert --to notebook --execute noise_demo1.ipynb --output=new.ipynb

# This save noise_demo1.html
# jupyter nbconvert --to=html --execute noise_demo1.ipynb
# jupyter nbconvert --to=pdf --execute noise_demo1.ipynb
