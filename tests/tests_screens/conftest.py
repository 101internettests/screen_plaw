import pytest
import tarfile
import os
import glob

from datetime import datetime
from config import bot, chat_id


@pytest.fixture(scope="session", autouse=True)
def archive_screens(request):
    """
    Фикстура для архивирования папки /var/lib/jenkins/screens после завершения всех тестов.
    """
    # Путь к директории, которую нужно архивировать
    source_dir = "/var/lib/jenkins/screens"
    # Путь для сохранения архива
    backup_dir = "/var/lib/jenkins/backups"
    # Имя архива с текущей датой и временем
    archive_name = f"screens_backup_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.tar.gz"
    archive_path = os.path.join(backup_dir, archive_name)

    # Создаем директорию для бэкапов, если её нет
    os.makedirs(backup_dir, exist_ok=True)

    # Функция, которая выполнится после завершения всех тестов
    def create_archive():
        print(f"Создание архива: {archive_path}")
        try:
            with tarfile.open(archive_path, "w:gz") as tar:
                tar.add(source_dir, arcname=os.path.basename(source_dir))
            print(f"Архив успешно создан: {archive_path}")
        except Exception as e:
            print(f"Ошибка при создании архива: {e}")

    # Регистрируем финализатор
    request.addfinalizer(create_archive)


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    backup_dir = "/var/lib/jenkins/backups"
    list_of_files = glob.glob(os.path.join(backup_dir, "*.tar.gz"))
    if list_of_files:
        latest_file = max(list_of_files, key=os.path.getctime)
        archive_name = os.path.basename(latest_file)

        # URL для скачивания архива
        server_url = "https://qa.101internet.ru"
        download_url = f"{server_url}/backups/{archive_name}"

        # Сообщение для Telegram
        message = (
            "Тесты на скрины прошли.\n"
            f"Скачать архив: {download_url}"
        )
    else:
        message = "Тесты на скрины прошли, но архив не был создан."
    bot.send_message(chat_id, message)
