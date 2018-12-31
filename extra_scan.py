import sqlite3

conn = sqlite3.connect('./data/mods.sqlite')
alter = conn.cursor()
sql_stmt = '''CREATE TABLE IF NOT EXISTS other_mods(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, mod_name TEXT, short TEXT, purpose TEXT)'''
alter.execute(sql_stmt)
conn.commit()
alter.execute("DELETE FROM other_mods")
conn.commit()
alter.execute("VACUUM")
conn.commit()

def extras_scan(directory, purpose):
    import os
    from pathlib import Path
    extras = list()
    name_list = list()
    for file in os.listdir(Path(directory)):
        if file.endswith('.py'):
            extras.append(directory + '/' + file)
        elif file.endswith('.txt'):
            name_list.append(directory + '/' + file)
    for item in extras:
        extras.remove(item)
        alter.execute("INSERT INTO other_mods(mod_name, short, purpose) VALUES(?, ?, ?)", (item, "Script", purpose))
    for item in name_list:
        name_list.remove(item)
        alter.execute("INSERT INTO other_mods(mod_name, short, purpose) VALUES(?, ?, ?)", (item, "List", purpose))
    conn.commit()

