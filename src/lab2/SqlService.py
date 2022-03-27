import sqlite3


class SqlService:
    @staticmethod
    def prepare() -> None:
        connect: sqlite3.Connection = sqlite3.connect("resources/example.db")
        cursor: sqlite3.Cursor = connect.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS polygon
            (
                id TEXT NOT NULL PRIMARY KEY
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS vertex
            (
                id         TEXT NOT NULL PRIMARY KEY,
                x          TEXT NOT NULL,
                y          TEXT NOT NULL,
                polygon_id TEXT NOT NULL,
                FOREIGN KEY (polygon_id) REFERENCES polygon (id)
            );
        """)

        connect.commit()
        connect.close()

    @staticmethod
    def sql_execute(query, parameters=None):
        SqlService.prepare()
        connect: sqlite3.Connection = sqlite3.connect("resources/example.db")
        cursor: sqlite3.Cursor = connect.cursor()

        if parameters is None:
            cursor.execute(query)
        else:
            cursor.execute(query, parameters)

        connect.commit()
        connect.close()

    @staticmethod
    def sql_get_element(result_parser, query, parameters=None):
        SqlService.prepare()
        connect: sqlite3.Connection = sqlite3.connect("resources/example.db")
        cursor: sqlite3.Cursor = connect.cursor()

        if parameters is None:
            executed = cursor.execute(query)
        else:
            executed = cursor.execute(query, parameters)
        result = result_parser(executed.fetchone())

        connect.commit()
        connect.close()

        return result

    @staticmethod
    def sql_get_list(result_row_parser, query, parameters=None):
        SqlService.prepare()
        result = []

        connect: sqlite3.Connection = sqlite3.connect("resources/example.db")
        cursor: sqlite3.Cursor = connect.cursor()

        if parameters is None:
            executed = cursor.execute(query)
        else:
            executed = cursor.execute(query, parameters)
        for row in executed:
            result.append(result_row_parser(row))

        connect.commit()
        connect.close()

        return result
