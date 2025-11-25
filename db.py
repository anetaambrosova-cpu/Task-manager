import mysql.connector

def pripojeni_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",           
            password="dastynek678",
            database="ukoly_db"
        )
        cursor = conn.cursor(dictionary=True)
        print("Připojení k databázi proběhlo úspěšně.")
        return conn, cursor
    except mysql.connector.Error as err:
        print("Chyba při připojování k databázi:", err)
        return None, None

def vytvoreni_tabulky():
    
    conn, cursor = pripojeni_db()
    if conn is None:
        print("Nelze vytvořit tabulku – připojení k DB selhalo.")
        return

    try:
        sql = """
        CREATE TABLE IF NOT EXISTS ukoly (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nazev VARCHAR(255) NOT NULL,
            popis TEXT NOT NULL,
            stav ENUM('nezahájeno', 'probíhá', 'hotovo') DEFAULT 'nezahájeno',
            datum_vytvoreni TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(sql)
        conn.commit()
        print("Tabulka 'ukoly' je připravena v databázi.")
    except Exception as e:
        print("Chyba při vytváření tabulky:", e)
    finally:
        cursor.close()
        conn.close()



if __name__ == "__main__":
    vytvoreni_tabulky()
