def extras_scan():
    import sqlite3
    import os
    from pathlib import Path
    sql_stmt = '''CREATE TABLE IF NOT EXISTS other_mods(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, mod_name TEXT)'''
    mods_track = "INSERT INTO other_mods(mod_name) VALUES (?)"
    conn = sqlite3.connect('./data/mods.sqlite')
    alter = conn.cursor()
    alter.execute(sql_stmt)
    conn.commit()
    extras = list()
    name_list = list()
    DIRECTORIES = ['./data/scripts', './data/scripts/persistence', './data']
    for entry in DIRECTORIES:
        for file in os.listdir(Path(entry)):
            if file.endswith('.py'):
                extras.append(entry + '/' + file)
            elif file.endswith('.txt'):
                name_list.append(entry + '/' + file)
    for item in extras:
        extras.remove(item)
        alter.execute(mods_track, [item])
    for item in name_list:
        name_list.remove(item)
        alter.execute(mods_track, [item])
    conn.commit()
    conn.close()
if __name__ == "__main__":
    extras_scan()
