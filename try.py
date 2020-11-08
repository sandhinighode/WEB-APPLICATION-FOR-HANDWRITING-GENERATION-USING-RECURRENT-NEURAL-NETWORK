import subprocess,time


s = input("Enter Style : ")
t = input("Enter Text : ")
b = input("Enter Bias : ")

substring ='python generate.py --text="{}" --bias={} --style={}'.format(t,b,s)

subprocess.call(substring, shell=True)

time.sleep(10)