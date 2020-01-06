# misc_py
Miscellaneous katas in Python
 
* ***Testing***
  - python -m unittest discover -s ./ -p "*_test.py"

  - python -m unittest discover --verbose -s ./test/ -p "*_test.py"
* ***Local cloud build***

  - cloud-build-local --config=[BUILD_CONFIG] --dryrun=false --write-workspace=[LOCAL_DIRECTORY_PATH] [SOURCE_CODE]
   
   - Example: 
     - sudo cloud-build-local --config=/home/mary/PycharmProjects/misc_py/cloudbuild.yaml --dryrun=false --write-workspace=/home/mary/MiscyPy /home/mary/PycharmProjects/misc_py/  
* ***Random Tip(s)***
   - Learn the art of reading code. If you can read it you can write it.

* ***Challenges mined from various websites including the following:***
  - https://brilliant.org/courses/programming-python
  - https://codewars/
  - https://repl.it/     