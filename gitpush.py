import os

os.chdir("/home/student/mycode")
os.system("git add *")
msg= input("Enter your commit message:\n>")
os.system(f"git commit -m {msg}")
os.system("git push origin main")

