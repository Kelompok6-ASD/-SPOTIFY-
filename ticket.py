# bagian tita dan wawa
from database import db


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def show_tickets():
    cursor = db.cursor()
    cursor.execute("SELECT id, nama_konser, DATE_FORMAT(tanggal, '%d-%m-%Y'), harga FROM tickets")
    tickets = cursor.fetchall()

    print("DAFTAR TIKET KONSER:")
    print("ID  | NAMA KONSER            | TANGGAL       | HARGA")
    print("----|------------------------|---------------|-------")
    for i, ticket in enumerate(tickets):
        if i == 0:
            print(f"{ticket[0]:<4}| {ticket[1]:<22} | {ticket[2]:<14}     | {ticket[3]:>5}")
            print(f"====|========================|====================|=======")
        else:
            print(f"{ticket[0]:<4}| {ticket[1]:<22} | {ticket[2]:<14}     | {ticket[3]:>5}")
            print(f"-------------------------------------------------------")
# selesai tita dan wawa
