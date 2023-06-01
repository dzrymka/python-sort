def selection_sort(players):
    n = len(players)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if players[j]["Jumlah Gol"] > players[max_index]["Jumlah Gol"]:
                max_index = j
        players[i], players[max_index] = players[max_index], players[i]


players = [
    {
        "No.": 1,
        "Nama Pemain": "Kylian Mbappe",
        "Klub": "Paris Saint Germain",
        "Jumlah Gol": 40,
    },
    {"No.": 2, "Nama Pemain": "Victor Osimhen", "Klub": "Napoli", "Jumlah Gol": 28},
    {
        "No.": 3,
        "Nama Pemain": "Robert Lewandowski",
        "Klub": "Barcelona",
        "Jumlah Gol": 33,
    },
    {
        "No.": 4,
        "Nama Pemain": "Erling Haaland",
        "Klub": "Borussia Dortmund",
        "Jumlah Gol": 52,
    },
    {
        "No.": 5,
        "Nama Pemain": "Christopher Nkunku",
        "Klub": "RB Leipzig",
        "Jumlah Gol": 22,
    },
]

selection_sort(players)

# Menampilkan daftar pemain yang telah diurutkan berdasarkan jumlah gol
print("Daftar pemain yang telah diurutkan berdasarkan jumlah gol secara descending:")
for player in players:
    print(
        f"No. {player['No.']}: {player['Nama Pemain']} - {player['Klub']}, {player['Jumlah Gol']} gol"
    )
