HOW TO RUN TEST
after running the code using command "docker-compose up" inside the project dir ebi-test/

Automate testing:
- open a bash shell
- move inside the directory ebi-test/
- run the script ./auto_test.sh

Manual testing:
the request can be made in the following format using a web browser
http://127.0.0.1:5000/genes?name=<name>&species=<species>

using curl linux command example
curl -X GET 'http://127.0.0.1:5000/genes?name=brc2&species=homo_sapiens'


HOW TO BUILD DEPLOY AND RUN
inside the project folder type: 
"docker-compose build"
to run in detached mode
"docker-compose up -d"

