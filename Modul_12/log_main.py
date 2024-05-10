
import logging.config
import requests as rq


log_config = {
    "version": 1,
    "formatters": {
        "success_responses_formatter": {
            "format": "%(levelname)s - %(message)s"
        },
        "bad_responses_formatter": {
            "format": "%(levelname)s - %(message)s"
        },
        "blocked_responses_formatter": {
            "format": "%(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "success_responses_handler": {
            "class": "logging.FileHandler",
            "formatter": "success_responses_formatter",
            "filename": "success_responses.log",
            "encoding": "UTF-8"
        },
        "bad_responses_handler": {
            "class": "logging.FileHandler",
            "formatter": "bad_responses_formatter",
            "filename": "bad_responses.log",
            "encoding": "UTF-8"
        },
        "blocked_responses_handler": {
            "class": "logging.FileHandler",
            "formatter": "blocked_responses_formatter",
            "filename": "blocked_responses.log",
            "encoding": "UTF-8"
        }
    },
    "loggers": {
        "success_responses": {
            "handlers": ["success_responses_handler"],
            "level": "INFO"
        },
        "bad_responses": {
            "handlers": ["bad_responses_handler"],
            "level": "INFO"
        },
        "blocked_responses": {
            "handlers": ["blocked_responses_handler"],
            "level": "ERROR"
        }
    }
}
logging.config.dictConfig(log_config)
log_success_responses = logging.getLogger('success_responses')
log_bad_responses = logging.getLogger('bad_responses')
log_blocked_responses = logging.getLogger('blocked_responses')


sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        str_response = str(response)
        str_response = str_response[-5: -2]

        if str_response == '200':
            log_success_responses.info(f'{site},  response - {str_response}')
        else:
            log_bad_responses.warning(f'{site},  response - {str_response}')
    except Exception:
        log_blocked_responses.exception(f'{site}, NO CONNECTION')



