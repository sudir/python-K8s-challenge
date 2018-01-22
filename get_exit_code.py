#!/usr/bin/env python 
# Written by: Matt Trotter SudirlayCoders code experts
import subprocess
import time
import sys, traceback
import re



def get_runtime():
 # Deploy Kubernetes pod 
 subprocess.Popen('kubectl create -f matts-python-pod.yml', shell=True)
 time.sleep(2)
 while True:
  exit_code = subprocess.Popen('kubectl describe pod matts-python-pod | grep State', shell=True, stdout=subprocess.PIPE) # Test line for demo purposes
  for results in exit_code.stdout:
    if "Terminated" in results:
      # Extract exit code and exit loop    
      code_result = subprocess.Popen('kubectl describe pod matts-python-pod | grep "Exit Code:"', shell=True, stdout=subprocess.PIPE) # Test line for demo purposes
      for response in code_result.stdout:
        print('Pod has terminated with exit code:')
        rawcode=int(re.findall('\\d+', response)[0])
        print(rawcode)
        #subprocess.Popen('kubectl delete pod matts-python-pod', shell=True)
        sys.exit(rawcode)
        

    else:
      print('Container still running no exit code to extact')
      time.sleep(1)

get_runtime()



