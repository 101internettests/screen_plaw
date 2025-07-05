"""
Утилиты для отладки проблем в Jenkins
"""

import os
import psutil
import requests
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def log_system_info():
    """Логирует информацию о системе"""
    try:
        # Информация о памяти
        memory = psutil.virtual_memory()
        logger.info(f"Память: {memory.percent}% использовано, {memory.available // (1024**3)}GB доступно")
        
        # Информация о CPU
        cpu_percent = psutil.cpu_percent(interval=1)
        logger.info(f"CPU: {cpu_percent}%")
        
        # Информация о диске
        disk = psutil.disk_usage('/')
        logger.info(f"Диск: {disk.percent}% использовано, {disk.free // (1024**3)}GB свободно")
        
        # Переменные окружения
        logger.info("Переменные окружения:")
        env_vars = ['HEADLESS', 'BASE_SAVING_PATH', 'URL_STAGE', 'URL_PROD']
        for var in env_vars:
            value = os.getenv(var, 'НЕ УСТАНОВЛЕНА')
            logger.info(f"  {var}: {value}")
            
    except Exception as e:
        logger.error(f"Ошибка при получении информации о системе: {e}")


def check_network_connectivity(urls):
    """Проверяет доступность сайтов"""
    logger.info("Проверка доступности сайтов...")
    
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            logger.info(f"✅ {url} - доступен (статус: {response.status_code})")
        except requests.exceptions.Timeout:
            logger.error(f"❌ {url} - таймаут")
        except requests.exceptions.ConnectionError:
            logger.error(f"❌ {url} - ошибка подключения")
        except Exception as e:
            logger.error(f"❌ {url} - ошибка: {e}")


def check_screenshot_quality(screenshot_path):
    """Проверяет качество скриншота"""
    if not os.path.exists(screenshot_path):
        logger.error(f"Скриншот не найден: {screenshot_path}")
        return False
    
    size = os.path.getsize(screenshot_path)
    logger.info(f"Размер скриншота {screenshot_path}: {size} байт")
    
    if size < 1000:
        logger.warning(f"Скриншот слишком маленький: {size} байт")
        return False
    
    if size > 10 * 1024 * 1024:  # Больше 10MB
        logger.warning(f"Скриншот слишком большой: {size} байт")
    
    return True


def save_error_page(page, name, error):
    """Сохраняет HTML страницы при ошибке для отладки"""
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        error_file = f'error_page_{name}_{timestamp}.html'
        
        with open(error_file, 'w', encoding='utf-8') as f:
            f.write(page.content())
        
        logger.info(f"HTML страницы сохранен для отладки: {error_file}")
        
        # Также сохраняем скриншот ошибки
        screenshot_error = f'error_screenshot_{name}_{timestamp}.png'
        page.screenshot(path=screenshot_error, full_page=True)
        logger.info(f"Скриншот ошибки сохранен: {screenshot_error}")
        
    except Exception as e:
        logger.error(f"Не удалось сохранить страницу для отладки: {e}")


def monitor_test_progress(current, total, page_name):
    """Мониторинг прогресса тестов"""
    progress = (current / total) * 100
    logger.info(f"Прогресс: {current}/{total} ({progress:.1f}%) - {page_name}")


def create_test_summary(results):
    """Создает сводку результатов тестов"""
    total = len(results)
    successful = sum(1 for r in results if r['success'])
    failed = total - successful
    
    summary = {
        'total': total,
        'successful': successful,
        'failed': failed,
        'success_rate': (successful / total) * 100 if total > 0 else 0,
        'errors': [r for r in results if not r['success']]
    }
    
    logger.info(f"Сводка тестов: {successful}/{total} успешно ({summary['success_rate']:.1f}%)")
    
    if failed > 0:
        logger.warning(f"Неудачные тесты:")
        for error in summary['errors']:
            logger.warning(f"  - {error['page']}: {error['error']}")
    
    return summary


def cleanup_old_files(directory, max_age_hours=24):
    """Удаляет старые файлы для экономии места"""
    try:
        current_time = datetime.now()
        deleted_count = 0
        
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                file_time = datetime.fromtimestamp(os.path.getctime(filepath))
                age_hours = (current_time - file_time).total_seconds() / 3600
                
                if age_hours > max_age_hours:
                    os.remove(filepath)
                    deleted_count += 1
        
        if deleted_count > 0:
            logger.info(f"Удалено {deleted_count} старых файлов из {directory}")
            
    except Exception as e:
        logger.error(f"Ошибка при очистке старых файлов: {e}")


def validate_environment():
    """Проверяет корректность настроек окружения"""
    errors = []
    warnings = []
    
    # Проверка переменных окружения
    required_vars = ['BASE_SAVING_PATH', 'URL_STAGE', 'URL_PROD']
    for var in required_vars:
        if not os.getenv(var):
            errors.append(f"Отсутствует переменная окружения: {var}")
    
    # Проверка директорий
    base_path = os.getenv("BASE_SAVING_PATH")
    if base_path:
        if not os.path.exists(base_path):
            try:
                os.makedirs(base_path, exist_ok=True)
                warnings.append(f"Создана директория: {base_path}")
            except Exception as e:
                errors.append(f"Не удалось создать директорию {base_path}: {e}")
    
    # Проверка доступности сайтов
    urls_to_check = [os.getenv('URL_STAGE'), os.getenv('URL_PROD')]
    for url in urls_to_check:
        if url:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code != 200:
                    warnings.append(f"Сайт {url} вернул статус {response.status_code}")
            except Exception as e:
                warnings.append(f"Не удалось проверить доступность {url}: {e}")
    
    # Логирование результатов
    if errors:
        logger.error("Критические ошибки в окружении:")
        for error in errors:
            logger.error(f"  - {error}")
    
    if warnings:
        logger.warning("Предупреждения в окружении:")
        for warning in warnings:
            logger.warning(f"  - {warning}")
    
    if not errors and not warnings:
        logger.info("Окружение настроено корректно")
    
    return len(errors) == 0 