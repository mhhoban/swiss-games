import subprocess


print "Setting up environment for Swiss Games:"
subprocess.call("pip install psycopg2")
subprocess.call("createdb tournament", shell=True)
subprocess.call("psql tournament -f tournament.sql", shell=True)
print "Swiss Games Setup Complete"
