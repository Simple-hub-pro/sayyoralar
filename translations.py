TRANSLATIONS = {
    'uz': {
        'app_title': 'Quyosh tizimi',
        'position': 'O\'rni',
        'type': 'Turi',
        'rocky': 'Qattiq',
        'gas_giant': 'Gaz giganti',
        'add_planet': 'Yangi sayyora qo\'shish',
        'submit': 'Saqlash',
        'back': 'Orqaga',
        'planet_name': 'Sayyora nomi',
        'description': 'Tavsif',
        'description_placeholder': 'Haqiqiy ilovada bu sayyora haqida batafsil ma\'lumotlar, tarkibi va qiziqarli faktlar mavjud bo\'ladi.',
        'cancel': 'Bekor qilish',
        'back_to_solar_system': 'Quyosh tizimiga qaytish'
    },
    'ru': {
        'app_title': 'Солнечная система',
        'position': 'Позиция',
        'type': 'Тип',
        'rocky': 'Твердая',
        'gas_giant': 'Газовый гигант',
        'add_planet': 'Добавить планету',
        'submit': 'Сохранить',
        'back': 'Назад',
        'planet_name': 'Название планеты',
        'description': 'Описание',
        'description_placeholder': 'В реальном приложении здесь будет содержаться подробная информация о характеристиках планеты, её составе и интересных фактах.',
        'cancel': 'Отмена',
        'back_to_solar_system': 'Вернуться к солнечной системе'
    }
}

def get_translation(lang, key):
    """Get translation for a given language and key."""
    if lang not in TRANSLATIONS:
        lang = 'uz'  # Default to Uzbek if language not found
    return TRANSLATIONS[lang].get(key, key) 