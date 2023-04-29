# bagian tita nabila putri
from database import db
import csv

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0

def print_invoice(customer_name, ticket_id, qty, file_path):
    cursor = db.cursor()
    cursor.execute(f"SELECT nama_konser, harga FROM tickets WHERE id={ticket_id}")
    ticket = cursor.fetchone()

    if ticket is None:
        print("Tiket tidak ditemukan.")
        return

    total_harga = ticket[1] * qty

    invoise = [customer_name, ticket[0], qty, ticket[1], total_harga]

    print(f"\nINVOICE PEMBELIAN TIKET KONSER")
    print(f"Nama Pelanggan: {customer_name}")
    print(f"Nama Konser: {ticket[0]}")
    print(f"Jumlah Tiket: {qty}")
    print(f"Harga Tiket: {ticket[1]}")
    print(f"Total Harga: {total_harga}")
    print("Ticket has been purchased.")

    # Insert data ke tabel pembelian
    cursor.execute(f"INSERT INTO pembelian (customer_name, tiket_id, jumlah, total_harga) VALUES ('{customer_name}', {ticket_id}, {qty}, {total_harga})")
    db.commit()

    # Simpan data invoice ke dalam queue
    invoice_queue = Queue()
    invoice_queue.enqueue(invoise)

    # Simpan data invoice ke dalam file CSV
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not invoice_queue.is_empty():
            # Tulis header jika file kosong
            if file.tell() == False:
                writer.writerow(['Nama Pelanggan', 'Nama Konser', 'Jumlah Tiket', 'Harga Tiket', 'Total Harga'])
                writer.writerow([customer_name, ticket[0], qty, ticket[1], total_harga])
            else:
                invoice = invoice_queue.dequeue()
                writer.writerow(invoice)
# selesai tita nabila putri

