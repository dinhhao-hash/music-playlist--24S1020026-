# \# playlist.py

# \# Simple CLI music playlist manager (procedural, non-OOP)

# 

# \# Global list to store songs. Each song is a dict:

# \# {'title': '...', 'artist': '...', 'duration': 0}

# songs = \[]

# 

# def add\_song():

# &nbsp;   """

# &nbsp;   Interactively ask user for song info and append to songs list.

# &nbsp;   """

# &nbsp;   title = input("Nhập tên bài hát: ").strip()

# &nbsp;   artist = input("Nhập tên ca sĩ: ").strip()

# &nbsp;   # Loop until a valid positive integer duration is entered

# &nbsp;   while True:

# &nbsp;       dur\_str = input("Nhập thời lượng (giây): ").strip()

# &nbsp;       if dur\_str.isdigit() and int(dur\_str) >= 0:

# &nbsp;           duration = int(dur\_str)

# &nbsp;           break

# &nbsp;       else:

# &nbsp;           print("Vui lòng nhập số nguyên không âm cho thời lượng (giây).")

# 

# &nbsp;   song = {'title': title, 'artist': artist, 'duration': duration}

# &nbsp;   songs.append(song)

# &nbsp;   print(f"Đã thêm: {title} - {artist} ({duration}s)")

# 

# def view\_playlist():

# &nbsp;   """

# &nbsp;   Print all songs in the playlist with index.

# &nbsp;   """

# &nbsp;   if not songs:

# &nbsp;       print("Playlist hiện đang trống.")

# &nbsp;       return

# 

# &nbsp;   print("\\n--- DANH SÁCH PHÁT ---")

# &nbsp;   for i, s in enumerate(songs, start=1):

# &nbsp;       print(f"{i}. {s\['title']} - {s\['artist']} ({s\['duration']}s)")

# &nbsp;   print("--- KẾT THÚC ---\\n")

# 

# def search\_by\_artist():

# &nbsp;   """

# &nbsp;   Ask user for an artist name and print songs matching that artist.

# &nbsp;   Comparison is case-insensitive and checks exact artist string.

# &nbsp;   """

# &nbsp;   if not songs:

# &nbsp;       print("Playlist rỗng — không có gì để tìm.")

# &nbsp;       return

# 

# &nbsp;   q = input("Nhập tên ca sĩ cần tìm: ").strip().lower()

# &nbsp;   found = \[s for s in songs if s\['artist'].strip().lower() == q]

# 

# &nbsp;   if not found:

# &nbsp;       print(f"Không tìm thấy bài hát của ca sĩ: {q}")

# &nbsp;   else:

# &nbsp;       print(f"\\nTìm thấy {len(found)} bài hát của '{q}':")

# &nbsp;       for i, s in enumerate(found, start=1):

# &nbsp;           print(f"{i}. {s\['title']} - {s\['artist']} ({s\['duration']}s)")

# &nbsp;       print()

# 

# def main():

# &nbsp;   """

# &nbsp;   Main CLI loop.

# &nbsp;   """

# &nbsp;   while True:

# &nbsp;       print("\\n--- MUSIC PLAYLIST MANAGER ---")

# &nbsp;       print("1. Thêm bài hát")

# &nbsp;       print("2. Xem danh sách phát")

# &nbsp;       print("3. Tìm bài hát theo ca sĩ")

# &nbsp;       print("4. Thoát")

# &nbsp;       choice = input("Chọn chức năng: ").strip()

# 

# &nbsp;       if choice == '1':

# &nbsp;           add\_song()

# &nbsp;       elif choice == '2':

# &nbsp;           view\_playlist()

# &nbsp;       elif choice == '3':

# &nbsp;           search\_by\_artist()

# &nbsp;       elif choice == '4':

# &nbsp;           print("Kết thúc chương trình.")

# &nbsp;           break

# &nbsp;       else:

# &nbsp;           print("Lựa chọn không hợp lệ. Vui lòng chọn 1-4.")

# 

# if \_\_name\_\_ == "\_\_main\_\_":

# &nbsp;   main()



