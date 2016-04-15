#Description:

I test this with 1G file and it with no program dump. on the lap top, the process time nearly 5 minutes. <br>

###Prepare
python install -r requirement.txt <br>
###how to run: <br>
python processfile.py data.txt <br>
###how to run unit test: <br>
python test_processfile.python <br>

###more about testing: <br>
#####1. Performance testing: check the program under differnt file size and format performance. it  <br> has more details, for example, a a big file but only has one line, the file has some separator which is not blank. all such excpetion should be considered in clean data part.
#####2. Function testing: check the program's output work as we expect  <br>
#####3. Integration testing: Integrate this pogram with the system, check weather it is work correct when there is service dependency. <br>
#####4. Smoking testing: With a whatever file, check it can handle exception <br>
#####5. If the file size is too big to handle, we had to chunk file, at this time, we need to check the chunk size and the critical point of the chunk size. <br>
######6. With different input file, check the program can clean data behavior, whether it will lost data or performance bad. <br>
######7. Code scane for License or scurity issues <br>
