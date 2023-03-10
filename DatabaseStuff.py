# Code from Dr. John F. Santore's Sprint 3 Instructor Demo used as basis for Sprint 4

import sqlite3
from typing import Tuple
# from main import db_name

db_name = "cubesProject.sqlite"


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def create_entries_table(cursor: sqlite3.Cursor):
    create_statement = """CREATE TABLE IF NOT EXISTS WuFooData(
    entryID INTEGER PRIMARY KEY,
    prefix TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    title TEXT,
    org TEXT,
    email TEXT,
    website TEXT,
    phone TEXT,
    course_project BOOLEAN,
    guest_speaker BOOLEAN,
    site_visit BOOLEAN,
    job_shadow BOOLEAN,
    internship BOOLEAN,
    career_panel BOOLEAN,
    networking_event BOOLEAN,
    summer2022 BOOLEAN,
    fall2022 BOOLEAN,
    spring2023 BOOLEAN,
    summer2023 BOOLEAN,
    other BOOLEAN,
    permission_granted TEXT,
    date_created TEXT,
    created_by TEXT,
    claimed_by TEXT);"""    # claimed_by is the foreign key with email of the person who claimed the proposal
    cursor.execute(create_statement)


def add_entries_to_db(cursor: sqlite3.Cursor, entries_data: list[dict]):
    # the insert or ignore syntax will insert if the primary key isn't in use or ignore if the primary key is in the DB
    insert_statement = """INSERT OR IGNORE INTO WuFooData (entryID, prefix, first_name, last_name, title, org, email, 
    website, phone, course_project, guest_speaker, site_visit, job_shadow, internship, career_panel, networking_event, 
    summer2022, fall2022, spring2023, summer2023, other, permission_granted, date_created, created_by) 
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
    for entry in entries_data:
        entry_values = list(entry.values())  # get the list of values from the dictionary
        entry_values[0] = int(entry_values[0])  # the EntryID is a string, but I want it to be a number
        entry_values = entry_values[:-2]
        cursor.execute(insert_statement, entry_values)


def create_claim_table(cursor: sqlite3.Cursor):
    create_statement = """CREATE TABLE IF NOT EXISTS Claims(
    email TEXT PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    title TEXT,
    department TEXT,
    FOREIGN KEY (email)
        REFERENCES WuFooData (claimed_by));"""
    cursor.execute(create_statement)


def add_claims_to_db(claims_values: list[str], entry_id: int):
    conn, cursor = open_db(db_name)
    cursor.execute(f"""UPDATE WuFooData SET claimed_by = ? WHERE entryID = {entry_id}""", (claims_values[3],))
    insert_statement = """INSERT OR IGNORE INTO Claims (first_name, last_name, title, email, department)
    VALUES(?,?,?,?,?)"""
    cursor.execute(insert_statement, claims_values)
    close_db(conn)
