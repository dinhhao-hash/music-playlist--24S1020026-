# playlist.py
# Simple CLI music playlist manager (procedural, non-OOP)

# Global list to store songs. Each song is a dict:
# {'title': '...', 'artist': '...', 'duration': 0}
songs = []

def add_song():
    """
    Interactively ask user for song info and append to songs list.
    """
    title = input("Nhập tên bài hát: ").strip()
    artist = input("Nhập tên ca sĩ: ").strip()
    # Loop until a valid positive integer duration is entered
    while True:
        dur_str = input("Nhập thời lượng (giây): ").strip()
        if dur_str.isdigit() and int(dur_str) >= 0:
            duration = int(dur_str)
            break
        else:
            print("Vui lòng nhập số nguyên không âm cho thời lượng (giây).")

    song = {'title': title, 'artist': artist, 'duration': duration}
    songs.append(song)
    print(f"Đã thêm: {title} - {artist} ({duration}s)")

def view_playlist():
    """
    Print all songs in the playlist with index.
    """
    if not songs:
        print("Playlist hiện đang trống.")
        return

    print("\n--- DANH SÁCH PHÁT ---")
    for i, s in enumerate(songs, start=1):
        print(f"{i}. {s['title']} - {s['artist']} ({s['duration']}s)")
    print("--- KẾT THÚC ---\n")

def search_by_artist():
    """
    Ask user for an artist name and print songs matching that artist.
    Comparison is case-insensitive and checks exact artist string.
    """
    if not songs:
        print("Playlist rỗng — không có gì để tìm.")
        return

    q = input("Nhập tên ca sĩ cần tìm: ").strip().lower()
    found = [s for s in songs if s['artist'].strip().lower() == q]

    if not found:
        print(f"Không tìm thấy bài hát của ca sĩ: {q}")
    else:
        print(f"\nTìm thấy {len(found)} bài hát của '{q}':")
        for i, s in enumerate(found, start=1):
            print(f"{i}. {s['title']} - {s['artist']} ({s['duration']}s)")
        print()

def main():
    """
    Main CLI loop.
    """
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")
        choice = input("Chọn chức năng: ").strip()

        if choice == '1':
            add_song()
        elif choice == '2':
            view_playlist()
        elif choice == '3':
            search_by_artist()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn 1-4.")

if __name__ == "__main__":
    main()
