"""
Настройки для стабильной работы автотестов в Jenkins
"""

import os

# Настройки браузера для Jenkins
JENKINS_BROWSER_ARGS = [
    '--no-sandbox',
    '--disable-dev-shm-usage',
    '--disable-gpu',
    '--disable-web-security',
    '--disable-features=VizDisplayCompositor',
    '--disable-background-timer-throttling',
    '--disable-backgrounding-occluded-windows',
    '--disable-renderer-backgrounding',
    '--disable-ipc-flooding-protection',
    '--memory-pressure-off',
    '--max_old_space_size=4096'
]

# Увеличенные таймауты для Jenkins
JENKINS_TIMEOUTS = {
    'page_load': 15000,  # Уменьшено с 30000 до 15000
    'element_wait': 10000,
    'action_wait': 5000,
    'screenshot_wait': 3000
}

# Настройки viewport для стабильных скриншотов
JENKINS_VIEWPORT = {
    'width': 1920,
    'height': 1080
}

# Проверка, запущен ли тест в Jenkins
def is_jenkins_environment():
    """Проверяет, запущен ли тест в Jenkins"""
    jenkins_vars = ['JENKINS_URL', 'BUILD_ID', 'WORKSPACE']
    return any(os.getenv(var) for var in jenkins_vars)

# Получение настроек в зависимости от окружения
def get_browser_args():
    """Возвращает аргументы браузера в зависимости от окружения"""
    if is_jenkins_environment():
        return JENKINS_BROWSER_ARGS
    return []

def get_timeout(key):
    """Возвращает таймаут в зависимости от окружения"""
    if is_jenkins_environment():
        return JENKINS_TIMEOUTS.get(key, 5000)
    return 5000  # Стандартный таймаут для локального запуска

def get_viewport():
    """Возвращает настройки viewport"""
    if is_jenkins_environment():
        return JENKINS_VIEWPORT
    return {'width': 1920, 'height': 1080} 