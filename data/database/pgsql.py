import psycopg2
import yaml


settings_seam = open("data/configs/db_config.yml", "r")
main_cfg = yaml.safe_load(settings_seam)
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
    curs = con.cursor()
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
            curs.execute('''CREATE DATABASE IF NOT EXISTS albert''')
            curs.execute('''
            create table if not exists public.albert_sploits
            (
                id       serial                                             not null
                    constraint albert_sploits_pkey
                        primary key,
                datetime timestamp with time zone default CURRENT_TIMESTAMP not null,
                tech     text,
                version  text,
                cve      text
                    constraint albert_sploits_cve_key
                        unique,
                path     text
                    constraint albert_sploits_path_key
                        unique
            );

            alter table public.albert_sploits
                owner to albert;

            create table if not exists public.albert_tools
            (
                id               serial                                             not null
                    constraint albert_tools_pkey
                        primary key,
                datetime         timestamp with time zone default CURRENT_TIMESTAMP not null,
                lang             text,
                path             text
                    constraint albert_tools_path_key
                        unique,
                types             text,
                purpose          text
            );

            alter table public.albert_tools
                owner to albert;

            create table if not exists public.albert_loots
            (
                id               serial                                             not null
                    constraint albert_loots_pkey
                        primary key,
                datetime         timestamp with time zone default CURRENT_TIMESTAMP not null,
                operating_system text,
                host             text,
                local_path       text,
                type_of_loot     text,
                persist          boolean,
                best_cve         text,
                used_cve         text
            );

            alter table public.albert_loots
                owner to albert;

            create table if not exists public.albert_data
            (
                id       serial                                             not null
                    constraint albert_data_pkey
                        primary key,
                dtg      timestamp with time zone default CURRENT_TIMESTAMP not null,
                when_run text
            );

            alter table public.albert_data
                owner to albert; ''')
        except psycopg2.OperationalError:
            print("Critical! DB Was not created!")

    def buildSploits(path, name, tech, version):
        print("Still working......")

    def buildToolsList(directory, purpose):
        try:
            extras = list()
            name_list = list()
            ps = list()
            xml_file = list()
            for file in os.listdir(directory):
                if file.endswith('.py'):
                    extras.append(directory + '/' + file)
                elif file.endswith('.txt'):
                    name_list.append(directory + '/' + file)
                elif file.endswith('.xml'):
                    xml_file.append(directory + '/' + file)
                elif file.endswith('.ps1'):
                    ps.append(directory + '/' + file)
                else:
                    grouping = [directory + '/' + file]

                for item in extras:
                    extras.remove(item)
                    curs.execute("INSERT INTO albert_tools(path, types, purpose, lang) VALUES (%s,%s,%s,%s)",
                                  (item, "Script", purpose, 'python'))
                for item in name_list:
                    name_list.remove(item)
                    curs.execute("INSERT INTO albert_tools(path, types, purpose, lang) VALUES (%s,%s,%s,%s)",
                                  (item, "List", purpose, "text"))
                for item in xml_file:
                    xml_file.remove(item)
                    curs.execute(
                        "INSERT INTO albert_tools(path, types, purpose, lang) VALUES (%s,%s,%s,%s)",
                        (item, "Scan", purpose, "XML"))
                for item in ps:
                    ps.remove(item)
                    curs.execute(
                        "INSERT INTO albert_tools(path, types, purpose, lang) VALUES (%s,%s,%s,%s)",
                        (item, "Script", purpose, "Powershell"))
                con.commit()
        except psycopg2.OperationalError as e:
            print(f"Error happened when populating the database..\n->{e}")

    def query_Sploits(tech, version, host):
        sel_stmt = "SELECT albert_sploits(cve) FROM albert_sploits WHERE albert_sploits(tech) = (?) AND albert_sploits(version) = (?)"
        for row in curs.execute(sel_stmt):
            curs.execute("UPDATE albert_loot(best_cve) WHERE albert_loot(host) = (?)", (row[1], host))
            print(f"Possible best exploit to use would be: {row[1]}\n For Host: {host}")
            print(
                f"There is an entry in the database located at: SELECT albert_loot(best_cve) FROM albert_loot WHERE albert_loot(host) = {host}")
        return True

    def insertLewts(lewt, os, cve_used, best_guessed_cve, are_we_persisting, what_did_we_take):
        print("coming soon.")

    def insertTimeruns(what):
        curs.execute("INSERT INTO albert_data(when_run) VALUES(%s)", (what,))
        
    def checkForRun():
        try:
            for row in curs.execute('SELECT albert_data.when_run FROM albert_data WHERE when_run = "initial"'):
                if row[0] is not None:
                    return True
                else:
                    return False
        except (psycopg2.DatabaseError, psycopg2.OperationalError, TypeError):
            return False

    def queryTools(lang, method=''):
        cprint("[ !! ] In order to add to these modules, simply add your new module into the ./data/scripts folder "
               "and re-run the program. [ !! ]", "red", attrs=["bold"])
        modules = "[ + ] {} modules:\n".format(lang)
        cprint(modules, "green", attrs=["blink"])
        for row in curs.execute("SELECT * FROM albert_tools WHERE lang = (%s)", [lang, ]):
            cprint("|------------------------------------------------------------------------------|\n", "white",
                   attrs=["bold"])
            cprint("\t|\t Path \t|\t File Type \t|\t Purpose \t|\t Language \t|\n", "blue",
                   attrs=["bold"])
            print(f"->{row[2]}  |  {row[3]}  |  {row[4]}  |  {row[5]}\n")
            cprint("|______________________________________________________________________________|\n", "white",
                   attrs=["bold"])
        choice = input("[ ? ] Please select your choice please use the full path. [ ? ]\n->").lower()
        cprint("[ !! ] Or just press enter to return to the main menu. [ !! ]", "red")
        if choice != '':
            for rows in curs.execute("SELECT * FROM albert_tools WHERE mod_name = (%s)", [choice, ]):
                return rows[2]



