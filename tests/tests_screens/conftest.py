import pytest
import tarfile
import os
import glob
import logging
from datetime import datetime
from config import bot, chat_id
from jenkins_config import is_jenkins_environment

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


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
        logger.info(f"Создание архива: {archive_path}")
        try:
            # Проверяем, что директория существует и не пуста
            if os.path.exists(source_dir) and os.listdir(source_dir):
                with tarfile.open(archive_path, "w:gz") as tar:
                    tar.add(source_dir, arcname=os.path.basename(source_dir))
                logger.info(f"Архив успешно создан: {archive_path}")
                
                # Проверяем размер архива
                archive_size = os.path.getsize(archive_path)
                logger.info(f"Размер архива: {archive_size} байт")
                
                if archive_size < 1000:  # Слишком маленький архив
                    logger.warning("Архив слишком маленький, возможно есть проблемы со скриншотами")
                    
            else:
                logger.warning(f"Директория {source_dir} не существует или пуста")
                
        except Exception as e:
            logger.error(f"Ошибка при создании архива: {e}")

    # Регистрируем финализатор
    request.addfinalizer(create_archive)


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    """Отправка уведомления в Telegram после завершения тестов"""
    backup_dir = "/var/lib/jenkins/backups"
    
    try:
        list_of_files = glob.glob(os.path.join(backup_dir, "*.tar.gz"))
        if list_of_files:
            latest_file = max(list_of_files, key=os.path.getctime)
            archive_name = os.path.basename(latest_file)
            archive_size = os.path.getsize(latest_file)

            # URL для скачивания архива
            server_url = "https://qa.101internet.ru"
            download_url = f"{server_url}/backups/{archive_name}"

            # Определяем статус тестов
            if exitstatus == 0:
                status = "✅ УСПЕШНО"
            else:
                status = "❌ С ОШИБКАМИ"

            # Сообщение для Telegram
            message = (
                f"Тесты на скрины {status}\n"
                f"Размер архива: {archive_size} байт\n"
                f"Скачать архив: {download_url}"
            )
        else:
            message = "❌ Тесты на скрины завершены, но архив не был создан."
            
        # Отправляем сообщение в Telegram
        bot.send_message(chat_id, message)
        logger.info("Уведомление отправлено в Telegram")
        
    except Exception as e:
        logger.error(f"Ошибка при отправке уведомления: {e}")
        # Пытаемся отправить простое уведомление
        try:
            simple_message = f"Тесты на скрины завершены. Статус: {exitstatus}"
            bot.send_message(chat_id, simple_message)
        except Exception as e2:
            logger.error(f"Не удалось отправить даже простое уведомление: {e2}")


@pytest.fixture(autouse=True)
def setup_jenkins_environment():
    """Фикстура для настройки окружения Jenkins"""
    if is_jenkins_environment():
        logger.info("Обнаружена среда Jenkins, применяются специальные настройки")
        
        # Проверяем наличие необходимых переменных окружения
        required_vars = ['BASE_SAVING_PATH', 'URL_STAGE', 'URL_PROD']
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            logger.warning(f"Отсутствуют переменные окружения: {missing_vars}")
        
        # Проверяем доступность директорий
        base_path = os.getenv("BASE_SAVING_PATH")
        if base_path:
            os.makedirs(base_path, exist_ok=True)
            logger.info(f"Директория для скриншотов создана/проверена: {base_path}")
    
    yield
