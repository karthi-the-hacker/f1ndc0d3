# f1ndc0d3
f1ndc0d3 it is used to find status code of any domain 

Steps to install :
im Happy to say this you dont need to install any third party service to run my tool 😃
its pure python ❤️️

1. pip install requests && pip3 install requests
2. cd tools/
3. git clone https://github.com/karthi-the-hacker/f1ndc0d3.git
4. cd f1ndc0d3/

syntax:-

single doamin  :-

    python f1ndc0d3.py --all https://domain.com/
              
list of domains :-

    cat list.txt | python f1ndc0d3.py -a
              
list of domains with speed process and particular status code :-
             
    cat list.txt | xargs -n1 -P100 python f1ndc0d3.py -c 200 
