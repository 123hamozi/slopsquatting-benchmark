import psycopg2

# Build note from Linux image: apt-get install libpq-dev
# Do not confuse this OS package with a PyPI dependency.

print(psycopg2.__name__)
