import logic


def main():
    # Загружаем фильмы при старте
    movies = logic.load_movies()
    print(f"Загружено фильмов: {len(movies)}")

    while True:
        print("\nКАТАЛОГ ФИЛЬМОВ")
        print("1. Показать все фильмы")
        print("2. Показать непросмотренные фильмы")
        print("3. Добавить фильм")
        print("4. Отметить как просмотренный")
        print("5. Найти фильм по году")
        print("0. Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == "0":
            logic.save_movies(movies)
            print("Данные сохранены. Выход")
            break

        elif choice == "1":
            print("\nВСЕ ФИЛЬМЫ")
            for movie in movies:
                watched = "-" if movie['watched'] else "-"
                rating = movie['rating'] or "-"
                print(f"{movie['id']}. {movie['title']} ({movie['year']}) [{watched}] {rating}")

        elif choice == "2":
            unwatched = logic.get_unwatched(movies)
            print(f"\n НЕПРОСМОТРЕННЫЕ ({len(unwatched)})")
            for movie in unwatched:
                print(f"{movie['id']}. {movie['title']} ({movie['year']})")

        elif choice == "3":
            print("\nДОБАВИТЬ ФИЛЬМ")
            title = input("Название: ").strip()
            try:
                year = int(input("Год: ").strip())
                movies = logic.add_movie(movies, title, year)
                logic.save_movies(movies)
                print("Фильм добавлен")
            except:
                print("Ошибка при добавлении")

        elif choice == "4":
            print("\nОТМЕТИТЬ ПРОСМОТРЕННЫЕ")
            try:
                movie_id = int(input("ID фильма: ").strip())
                rating_input = input("Укажите рейтинг 1-10 : ").strip()
                rating = int(rating_input) if rating_input else None

                movies = logic.mark_watched(movies, movie_id, rating)
                logic.save_movies(movies)
                print("Фильм отмечен как просмотренный")
            except ValueError as e:
                print(f"Ошибка: {e}")
            except:
                print("Ошибка ввода")

        elif choice == "5":
            print("\nПОИСК ПО ГОДУ")
            try:
                year = int(input("Год: ").strip())
                found = logic.find_by_year(movies, year)
                print(f"Найдено фильмов: {len(found)}")
                for movie in found:
                    print(f"{movie['id']}. {movie['title']}")
            except:
                print("Ошибка ввода")

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()