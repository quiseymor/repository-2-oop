from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, ram: int, storage: int) -> None:
        """
        :param ram: Объем оперативной памяти в гигабайтах.
        :param storage: Объем хранилища в гигабайтах.

        :raises ValueError: Если объем RAM или хранилища не положительный.

        >>> pc = PersonalComputer(16, 512)
        >>> pc.ram
        16
        """
        if ram <= 0:
            raise ValueError("Объем оперативной памяти должен быть положительным.")
        if storage <= 0:
            raise ValueError("Объем хранилища должен быть положительным.")

        self.ram = ram
        self.storage = storage

    @abstractmethod
    def boot(self) -> None:
        pass

    @abstractmethod
    def shutdown(self) -> None:
        pass


class PersonalComputer(Computer):
    def boot(self) -> None:
        print("Компьютер запущен.")

    def shutdown(self) -> None:
        print("Компьютер выключен.")


class Library(ABC):
    def __init__(self, name: str, book_count: int) -> None:
        """
        :param name: Название библиотеки.
        :param book_count: Количество книг в библиотеке.

        :raises ValueError: Если название пустое или количество книг отрицательное.

        >>> lib = PublicLibrary("Библиотека имени Пушкина", 5000)
        >>> lib.name
        'Библиотека имени Пушкина'
        """
        if not name:
            raise ValueError("Название не может быть пустым.")
        if book_count < 0:
            raise ValueError("Количество книг не может быть отрицательным.")

        self.name = name
        self.book_count = book_count

    @abstractmethod
    def lend_book(self, book_title: str) -> bool:
        pass

    @abstractmethod
    def return_book(self, book_title: str) -> bool:
        pass


class PublicLibrary(Library):
    def lend_book(self, book_title: str) -> bool:
        if not book_title:
            raise ValueError("Название книги не может быть пустым.")
        print(f"Книга '{book_title}' выдана.")
        return True

    def return_book(self, book_title: str) -> bool:
        if not book_title:
            raise ValueError("Название книги не может быть пустым.")
        print(f"Книга '{book_title}' возвращена.")
        return True


class MusicAlbum(ABC):
    def __init__(self, title: str, artist: str, tracks: int) -> None:
        """
        :param title: Название альбома.
        :param artist: Исполнитель альбома.
        :param tracks: Количество треков в альбоме.

        :raises ValueError: Если название или исполнитель пустые, или количество треков не положительное.

        >>> album = StudioAlbum("Linkin Park", "The Beatles", 17)
        >>> album.title
        'Linkin Park'
        """
        if not title:
            raise ValueError("Название альбома не может быть пустым.")
        if not artist:
            raise ValueError("Исполнитель не может быть пустым.")
        if tracks <= 0:
            raise ValueError("Количество треков должно быть положительным.")

        self.title = title
        self.artist = artist
        self.tracks = tracks

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass


class StudioAlbum(MusicAlbum):
    def play(self) -> None:
        print(f"Воспроизводится альбом '{self.title}' исполнителя '{self.artist}'.")

    def stop(self) -> None:
        print(f"Воспроизведение альбома '{self.title}' остановлено.")


if __name__ == "__main__":

    import doctest
    doctest.testmod()
