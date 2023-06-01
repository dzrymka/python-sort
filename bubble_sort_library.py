def bubble_sort(book_list):
    n = len(book_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if book_list[j]["Jumlah Halaman"] > book_list[j + 1]["Jumlah Halaman"]:
                book_list[j], book_list[j + 1] = book_list[j + 1], book_list[j]


book_list = [
    {
        "No.": 1,
        "Judul Buku": "Harry Potter and the Sorcerer's Stone",
        "Penulis": "J.K. Rowling",
        "Jumlah Halaman": 320,
    },
    {
        "No.": 2,
        "Judul Buku": "To Kill a Mockingbird",
        "Penulis": "Harper Lee",
        "Jumlah Halaman": 281,
    },
    {
        "No.": 3,
        "Judul Buku": "The Great Gatsby",
        "Penulis": "F. Scott Fitzgerald",
        "Jumlah Halaman": 180,
    },
    {
        "No.": 4,
        "Judul Buku": "Pride and Prejudice",
        "Penulis": "Jane Austen",
        "Jumlah Halaman": 432,
    },
    {"No.": 5, "Judul Buku": "1984", "Penulis": "George Orwell", "Jumlah Halaman": 328},
]

bubble_sort(book_list)

# Menampilkan daftar buku yang telah diurutkan
print("Daftar buku yang telah diurutkan berdasarkan jumlah halaman:")
for book in book_list:
    print(
        f"No. {book['No.']}: {book['Judul Buku']} - {book['Penulis']}, {book['Jumlah Halaman']} halaman"
    )
