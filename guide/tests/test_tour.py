from guide.main import handler

true = True
false = False

REQUEST_START = {
    "meta": {
        "locale": "ru-RU",
        "timezone": "UTC",
        "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
        "interfaces": {
            "screen": {},
            "payments": {},
            "account_linking": {},
            "geolocation_sharing": {},
        },
    },
    "session": {
        "message_id": 1,
        "session_id": "3a7beb82-75ef-4408-aeae-481d2d0afb24",
        "skill_id": "1f835d35-c640-4c36-b3bc-74ecaa0f71f1",
        "user": {
            "user_id": "5416FF55E3C40C32A49D45D68AA101F9AE1445387749DE5B7BEAAB9CD6557C1D"
        },
        "application": {
            "application_id": "218AE790B7125C9F67E9E3234671E8861D9603BD2627726710B9EF8A1CE9748D"
        },
        "user_id": "218AE790B7125C9F67E9E3234671E8861D9603BD2627726710B9EF8A1CE9748D",
        "new": false,
    },
    "request": {
        "command": "расскажи экскурсию",
        "original_utterance": "Расскажи экскурсию",
        "nlu": {
            "tokens": ["расскажи", "экскурсию"],
            "entities": [],
            "intents": {"start_tour": {"slots": {}}},
        },
        "markup": {"dangerous_context": false},
        "type": "SimpleUtterance",
    },
    "state": {"session": {"scene": "Welcome"}, "user": {}, "application": {}},
    "version": "1.0",
}

REQUEST_STEP = {
    "meta": {
        "locale": "ru-RU",
        "timezone": "UTC",
        "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
        "interfaces": {
            "screen": {},
            "payments": {},
            "account_linking": {},
            "geolocation_sharing": {},
        },
    },
    "session": {
        "message_id": 2,
        "session_id": "3a7beb82-75ef-4408-aeae-481d2d0afb24",
        "skill_id": "1f835d35-c640-4c36-b3bc-74ecaa0f71f1",
        "user": {
            "user_id": "5416FF55E3C40C32A49D45D68AA101F9AE1445387749DE5B7BEAAB9CD6557C1D"
        },
        "application": {
            "application_id": "218AE790B7125C9F67E9E3234671E8861D9603BD2627726710B9EF8A1CE9748D"
        },
        "user_id": "218AE790B7125C9F67E9E3234671E8861D9603BD2627726710B9EF8A1CE9748D",
        "new": false,
    },
    "request": {
        "command": "хорошо",
        "original_utterance": "Хорошо",
        "nlu": {
            "tokens": ["хорошо"],
            "entities": [],
            "intents": {"YANDEX.CONFIRM": {"slots": {}}},
        },
        "markup": {"dangerous_context": false},
        "type": "SimpleUtterance",
    },
    "state": {
        "session": {"scene": "StartTour", "tour_id": 1, "tour_level": 0},
        "user": {},
        "application": {},
    },
    "version": "1.0",
}

REQUEST_REPEAT = {
    "meta": {
        "locale": "ru-RU",
        "timezone": "UTC",
        "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
        "interfaces": {
            "screen": {},
            "payments": {},
            "account_linking": {},
            "geolocation_sharing": {},
        },
    },
    "session": {
        "message_id": 2,
        "session_id": "3a7beb82-75ef-4408-aeae-481d2d0afb24",
        "skill_id": "1f835d35-c640-4c36-b3bc-74ecaa0f71f1",
        "user": {
            "user_id": "5416FF55E3C40C32A49D45D68AA101F9AE1445387749DE5B7BEAAB9CD6557C1D"
        },
        "application": {
            "application_id": "218AE790B7125C9F67E9E3234671E8861D9603BD2627726710B9EF8A1CE9748D"
        },
        "user_id": "218AE790B7125C9F67E9E3234671E8861D9603BD2627726710B9EF8A1CE9748D",
        "new": false,
    },
    "request": {
        "command": "хорошо",
        "original_utterance": "Хорошо",
        "nlu": {
            "tokens": ["хорошо"],
            "entities": [],
            "intents": {"YANDEX.REPEAT": {"slots": {}}},
        },
        "markup": {"dangerous_context": false},
        "type": "SimpleUtterance",
    },
    "state": {
        "session": {"scene": "TourStep", "tour_id": 2, "tour_level": 0},
        "user": {},
        "application": {},
    },
    "version": "1.0",
}


def test_tour_start():
    response = handler(REQUEST_START, None)
    assert "Начнем нашу экскурсию" in response["response"]["text"]
    assert response["session_state"]["tour_id"] == 1


def test_tour_first():
    response = handler(REQUEST_STEP, None)
    assert (
        "Прислонившись спиной к колонне с открытой книгой в руках стоит князь Ярослав Мудрый"
        in response["response"]["text"]
    )
    assert response["session_state"]["tour_id"] == 2


def test_tour_repeat():
    response = handler(REQUEST_REPEAT, None)
    assert (
        "Прислонившись спиной к колонне с открытой книгой в руках стоит князь Ярослав Мудрый"
        in response["response"]["text"]
    )
    assert response["session_state"]["tour_id"] == 2