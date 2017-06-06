import sqlite3
import time

db_name = "log_action.db"
_conn = sqlite3.connect(db_name)
_c = _conn.cursor()
_c.execute('''CREATE TABLE IF NOT EXISTS log_action
                      (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_name TEXT,
                       mobile TEXT,
                       wechat_id TEXT,
                       log_action TEXT,
                       log_content TEXT,
                       log_time TEXT
                       )''')
_conn.commit()
_conn.close()

# public
def add_action(log_action, log_content, user_name=None, mobile=None, wechat_id=None):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    try:
        log_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        c.execute("INSERT INTO log_action VALUES (NULL, ?, ?, ?, ?, ?, ?)", (user_name, mobile, wechat_id, log_action, log_content, log_time))
        conn.commit()
    except:
        pass
    conn.close()
