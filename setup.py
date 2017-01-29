import subprocess


print "Setting up environment for Swiss Games:"
subprocess.call("pip install psycopg2")
subprocess.call("psql -f tournament.sql", shell=True)
print "Swiss Games Setup Complete"
