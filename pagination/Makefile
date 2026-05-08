#This is a Makefile

Function_file = 3-hypermedia_del_pagination.py

Project = pagination


main:
	chmod u+x $(Main_file)
	chmod u+x $(Function_file)
#black $(Function_file) 
	pycodestyle $(Function_file)
	./$(Main_file)
#cat $(Function_file) | mongo my_db


data:
	cat $(Function_file) | mysql hbtn_0d_2

#select:




#Main_file = test_save_reload_user.py 

Main_file =    $(number)-main.py

NAME =  #!/usr/bin/python3
NAME1 =  def raise_exception_msg(message=""):
Function_name = binary_tree_t *binary_tree_node(binary_tree_t *parent, int value);
number = $(shell echo $(Function_file) | grep -o '[0-9]*' | head -n1)


Header = binary_trees.h
Directory = singly_linked_lists






CC = gcc
Function_file_final =   '$(Function_file)' | tr -d '0123456789-'  
SRC =    $(Main_file) $(Function_file)  
OBJ = $(SRC:.c=.o)
RM = rm
git = git add * && git commit -m '$(NAME)' && git push
CFLAGS = -Wall -Werror -Wextra -pedantic -std=gnu89  
Final_header = \#include \"$(Header)\"
ReadMe = README.md


all: $(OBJ)
	$(CC)  $(CFLAGS)  $(OBJ) -o  $(NAME)
	betty  $(Header) $(Main_file)  $(Function_file)
	valgrind ./$(NAME) 
	$(RM) -rf $(OBJ) $(NAME)




.PHONY: clean oclean fclean re brk  echo valgrind folder

clean:
	$(RM) -rf *~  $(NAME)

oclean:
	$(RM) -rf $(OBJ) $(NAME)

fclean:
	$(RM) -rf *~  $(NAME)
	$(RM) -rf $(OBJ)
	rm $(SRC)
re: oclean  all

folder:
	mkdir $(Directory)
	cd $(Directory)
	touch $(ReadMe)

script:
	chmod u+x $(Function_file)
	pycodestyle $(Function_file)
	./$(Function_file)



file:
	chmod u+x $(Function_file)
#black $(Function_file)
	pycodestyle $(Function_file)
	./$(Function_file)

create_files:
	for i in $$(seq 1 8); do \
		touch $$i-index.html; \
	done

touch:
	touch $(Function_file)
	code $(Function_file)
	touch  $(Main_file)
	code $(Main_file)

	echo "#!/usr/bin/env python3" >> "$(Function_file)"
	echo "''' $(Function_file) $(Project) '''" >> "$(Function_file)"
	echo "" >> "$(Function_file)"
	echo "" >> "$(Function_file)"
touch1:
	touch $(Function_file)
	code $(Function_file)

git:
	rm -rf __pycache__
	$(git)

git-%:
	rm -rf __pycache__ api/__pycache__ api/v1/__pycache__ api/v1/views/__pycache__
	@$(MAKE) git NAME="$*"	

echo:

	echo  $(NAME)

valgrind:
	valgrind ./$(NAME)
