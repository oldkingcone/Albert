import psycopg2
import yaml

main_cfg = yaml.safe_load("../configs/db_config.yml")
user = main_cfg["pgsql"]["user"]
passw = main_cfg["pgsql"]["pass"]
host = main_cfg["pgsql"]["host"]
db = main_cfg["pgsql"]["name"]
d_path = main_cfg["locations"]["albert_data_path"]

try:
    con = psycopg2.connect(
        dbname=db,
        user=user,
        password=passw,
        host=host
    )
    con.cursor()
except Exception as e:
    import os

    print("Error happened at db connection, attempting to start the database.")
    if host == "localhost":
        os.system(f"pg_ctl start -D {d_path} -l {d_path}/main_log.log")
        print(f"PGCTL Status: {os.system(f'pg_ctl status -D {d_path}')}")
        try:
            con = psycopg2.connect(
                dbname=db,
                user=user,
                password=passw,
                host=host
            )
            curs = con.cursor()
        except Exception:
            import sys

            print("Something else went wrong, this might be a bigger issue \n"
                  "than the DB needing to be started, \n"
                  "please check that you have issued an init command using:\n"
                  "pg_ctl init -D [postgres data directory] -l [log file to use]\n"
                  "Exiting!")
            sys.exit(1)
    else:
        print("Please ensure the database is running on the host, and try to run again.")


class Sploit:

    def makeDB(stmt):
        try:
            curs.execute(stmt)
        except psycopg2.OperationalError:
            print("Critical! DB Was not created!")

    def buildSploits(path, name, tech, version):
        print("Still working......")

    def query_Sploits(tech, version):
        sel_stmt = "SELECT * FROM albert WHERE albert.version LIKE (?) AND albert.tech LIKE (?)"
