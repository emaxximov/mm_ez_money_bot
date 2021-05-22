scores = {
    'Учебная деятельность' : {
        # 1 критерий, все отлично
        'Всё на отлично' : [8],
        # 2 Получение стипендии
        'Награда за проект': {
            # международная
            'На международном уровне': {
                # победитель
                'Победитель': {
                    # очно
                    'Очно': [8, 5, 3, 1],
                    # заочно
                    'Заочно': [3, 2, 1]
                },
                # призёр
                'Призёр': {
                    # очно
                    'Очно': [7, 4, 2, 0.5],
                    # заочно
                    'Заочно': [2.5, 1.5, 0.5]
                }
            },
            # СНГ
            'На уровне СНГ': {
                # победитель
                'Победитель': {
                    # очно
                    'Очно': [5, 3, 2, 0.5],
                    # заочно
                    'Заочно': [2.5, 1.5, 0.5]
                },
                # призёр
                'Призёр': {
                    # очно
                    'Очно': [4, 2.5, 1.5, 0.5],
                    # заочно
                    'Заочно': [2, 1.5, 0.5]
                }
            },
            # Федеральный уровень
            'На федеральном уровне': {
                # победитель
                'Победитель': {
                    # очно
                    'Очно': [3, 2, 1],
                    # заочно
                    'Заочно': [1.5, 1, 0.5]
                },
                # призёр
                'Призёр': {
                    # очно
                    'Очно': [2, 1.5, 0.5],
                    # заочно
                    'Заочно': [1, 0.6, 0.4]
                }
            },
            #На уровне ВУЗа
            'На уровне ВУЗа': {
                # победитель
                'Победитель': [1, 0.6, 0.4],
                # призёр
                'Призёр': [0.5, 0.3, 0.2]
            }
        },
        #олимпиады
        'Олимпиады' : {
            #международная
            'На международном уровне' : {
                #победитель
                'Победитель' : {
                    # очно
                    'Очно': [13, 8, 5, 3, 1],
                    # заочно
                    'Заочно': [3, 2, 1]
                },
                #призёр
                'Призёр' : {
                    # очно
                    'Очно': [11, 7, 4, 2],
                    # заочно
                    'Заочно': [2.5, 1.5, 0.5]
                }
            },
            #СНГ
            'На уровне СНГ' : {
                #победитель
                'Победитель' : {
                    # очно
                    'Очно': [9, 6, 3, 1],
                    # заочно
                    'Заочно': [2.5, 1.5, 0.5]
                },
                #призёр
                'Призёр' : {
                    # очно
                    'Очно': [7, 5, 2],
                    # заочно
                    'Заочно': [2, 1.5, 0.5]
                }
            },
            #Федеральный уровень
            'На федеральном уровне' : {
                #победитель
                'Победитель' : {
                    # очно
                    'Очно': [5, 3, 2],
                    # заочно
                    'Заочно': [1.5, 1, 0.5]
                },
                #призёр
                'Призёр' : {
                    # очно
                    'Очно': [4, 2.5, 1.5],
                    # заочно
                    'Заочно': [1, 0.6, 0.4]
                }
            }
        },
    },

    'Научно-исследовательская деятельность' : {
        # Научно-исследовательские работы
        'Награды и гранты' : {
            #приз за научную работу
            'Приз за научную деятельность': [7, 4, 3, 1],
            # интеллектуальное деятельность
            'Патент/Свидетельство': {
                # индивидуальные
                'Индивидуальное': [15, 9, 6, 3],
                # коллективные
                'Коллективное': [10, 6, 4, 1]
            },
            # Личный грант (зачем вообще давать деньги этим людям???)
            'Личный грант': [13, 8, 5, 3, 1],
            # Исполнитель гранта
            'Участник гранта': [8, 5, 3, 1]
        },
        # Научно-исследовательские работы
        'Статьи  и тезисы' : {
            # Статьи
            #Зарубежные
            # Scopus
            #Q1
            'Scopus Q1': {
                #иностранный язык
                'На иностранном языке' : [20, 12, 8, 4, 2, 1],
                #русский язык
                'На русском языке' : [10, 6, 4, 2, 1]
            },
            # Q2
            'Scopus Q2' : {
                # иностранный язык
                'На иностранном языке' : [15, 9, 6, 3, 1],
                # русский язык
                'На русском языке': [10, 6, 4, 2, 1]
            },
            # not Scopus
            'Не Scopus' : [9, 5, 4, 2, 1],


            #ММК
            # Scopus ( только на иностранном)
            'ММК Scopus' : {
                #СДнСК УД
                'СДнСК УД' : [29, 17, 12, 7, 2],
                #СДнСК СД
                'СДнСК СД' : [20, 12, 8, 4, 2, 1],
                #БДнСК
                'БДнСК' : [15, 9, 6, 3, 1]
            },
            # not Scopus (на любом языке)
            'ММК не Scopus' : {
                # СДнСК УД
                'СДнСК УД': [18, 11, 7, 3],
                # СДнСК СД
                'СДнСК СД': [12, 8, 4, 1],
                # БДнСК
                'БДнСК': [9, 5, 4, 2, 1]
            },
            #Рос. издания
            # Scopus
            'Российское издание Scopus': [10, 6, 4, 2, 1],
            # VAK
            'Российское издание ВАК': [8, 4.5, 3.5, 1],
            # Not Index
            'Российское издание без индексации' : [5, 3, 2, 0.5],

            # Тезисы
            # Зарубежные
            'Тезисы в зарубежных изданиях' : {
                # Иностранный язык
                'На иностранном языке' : [4, 2.5, 1.5, 0.5],
                # Русский язык
                'На русском языке' : [3, 2, 1]
            },
            # ММК
            # Scopus
            'Тезисы ММК Scopus' : {
                # СДнСК УД
                'СДнСК УД' : {
                    # Иностранный язык
                    'На иностранном языке': [4, 2.5, 1.5, 0.5],
                    # Русский язык
                    'На русском языке': [3, 2, 1]
                },
                # СДнСК СД
                'СДнСК СД' : {
                    # Иностранный язык
                    'На иностранном языке': [4, 2.5, 1.5, 0.5],
                    # Русский язык
                    'На русском языке': [3, 2, 1]
                },
                # БДнСК
                'БДнСК'  : {
                    # Иностранный язык
                    'На иностранном языке': [4, 2.5, 1.5, 0.5],
                    # Русский язык
                    'На русском языке': [3, 2, 1]
                },
            },
            # not Scopus
            'Тезисы ММК не Scopus' : {
                # СДнСК УД
                'СДнСК УД': [7, 4, 3, 1],
                # СДнСК СД
                'СДнСК СД': [4, 2.5, 1.5, 0.5],
                # БДнСК
                'БДнСК': [2, 1.3, 0.7]
            },
            # Российские издания
            'Тезисы в Российских изданиях' : [2, 1.3, 0.7]
        },
    },

    'Общественная деятельность' : {
        # Общественный движ
        'Участие в общественной деятельности' : {
            # Организация учебных мероприятий
             'Организация учебных мероприятий': {
                # межд. уровень
                'На международном уровне' : [8, 5, 3],
                # всероссийский уровень
                'На уровне СНГ' : [6, 4, 2],
                # федеральный
                'На федеральном уровне' : [4, 2.5, 1.5],
                # уровень вуза
                'На уровне ВУЗа' : [3, 2, 1],
                # подразделение вуза
                'На уровне подразделения ВУЗа' : [2, 1.5, 0.5]
            },
            # Организация социальных мероприятий
            'Организация социальных мероприятий' : {
                # межд. уровень
                'На международном уровне': [6, 4, 2],
                # всероссийский уровень
                'На уровне СНГ': [4, 2.5, 1.5],
                # федеральный
                'На федеральном уровне': [3, 2, 1],
                # уровень вуза
                'На уровне ВУЗа': [2, 1.5, 0.5],
                # подразделение вуза
                'На уровне подразделения ВУЗа': [1, 0.5]
            },
            # Членство в жюри
            'Членство в жюри' : {
                #Очный
                'Очно' : [4],
                #Заочный
                'Заочно' : [3]
            },
            # Без-возд-мезд-но учить
            'Без-возд-мезд-ная учебная деятельность' : {
                #студентов
                'В отношении студентов' : [7],
                #школьников
                'В отношении школьников' : [4, 2]
            }
        },
        # Информациооное обеспечение движей
        'Информационное обеспечение мероприятий' : {
            # Печать
            'Периодика (печать)' : {
                'Главный редактор' : [5],
                'Бильд-редактор' : [4],
                'Дизайнерверстальщик' : [3],
                'Корреспондент' : [2],
                'Фотограф ' : [1, 1],
            },
            # SMM
            'SMM' : {
                'Руководитель' : [3],
                'Контент-менеджер' : [1, 1],
                'Администратор' : [2, 1]
            },
            # Сайт
            'Сайт' : {
                'Руководитель' : [2, 1],
                'Разработчик ' : [1, 0.5]
            },
            # Секретарь найчной конференции
            'Секретарь научной конференции' : [3, 3, 1]
        },
    },

    'Культурно-творческая деятельность' : {
        # Культурно-творческая деятельность
        'Награды' : {
            'На международном уровне' : {
                # очное
                'Очно' : [8, 5, 3, 1],
                # заочное
                'Заочно' : [4, 2.5, 1.5]
            },
            'На уровне СНГ' : {
                # очное
                'Очно': [6, 4, 0.5],
                # заочное
                'Заочно': [3, 2, 1]
            },
            'На федеральном уровне' : {
                # очное
                'Очно': [4, 2.5, 1.5],
                # заочное
                'Заочно': [2, 1.3, 0.7]
            },
            'На уровне ВУЗа' : {
                # очное
                'Очно': [2, 1.3, 0.7],
                # заочное
                'Заочно': [1, 0.6, 0.4]
            }
        },
        # публичные культурные мероприятия
        'Публикация' : {
            'На международном уровне' : {
                # очное
                'Очно' : [8, 5, 3, 1],
                # заочное
                'Заочно' : [3, 2, 1]
            },
            'На уровне СНГ' : {
                # очное
                'Очно': [5, 3, 2],
                # заочное
                'Заочно': [2, 1.2, 0.8]
            },
            'На федеральном уровне' : {
                # очное
                'Очно': [2, 1.2, 0.8],
                # заочное
                'Заочно': [0.8, 0.5, 0.3]
            }
        },
        'Участие в проведении мероприятий' : {
            'На международном уровне': {
                # Руководитель
                'Руководитель' : [8, 5, 3],
                # Организатор
                'Организатор' : [6, 4, 2],
                # Волонтер
                'Волонтер' : [4, 2.5, 1.5],
                # Участник
                'Участник' : [3, 2, 1]
            },
            'На уровне СНГ': {
                # Руководитель
                'Руководитель': [6, 4, 2],
                # Организатор
                'Организатор': [4, 2.5, 1.5],
                # Волонтер
                'Волонтер': [3, 2, 1],
                # Участник
                'Участник': [2, 1.5, 0.5]
            },
            'На федеральном уровне': {
                # Руководитель
                'Руководитель': [4, 2.5, 1.5],
                # Организатор
                'Организатор': [3, 2, 1],
                # Волонтер
                'Волонтер': [2, 1.5, 0.5],
                # Участник
                'Участник': [1, 0.5]
            },
            'На уровне ВУЗа': {
                # Руководитель
                'Руководитель': [3, 2, 1],
                # Организатор
                'Организатор': [2, 1.5, 0.5],
                # Волонтер
                'Волонтер': [1, 0.5],
                # Участник
                'Участник': [0.5, 0.3, 0.2]
            },
            'На уровне подразделения ВУЗа': {
                # Руководитель
                'Руководитель': [2, 1.5, 0.5],
                # Организатор
                'Организатор': [1, 0.5],
                # Волонтер
                'Волонтер': [0.5, 0.3, 0.2]
            }
        },
    },
    'Спортивная деятельность' : {
        'Участие в спортивных соревнованиях' : {
            'На международном уровне' : {
                # победитель
                'Победитель' : [10, 6, 4, 2, 1],
                # призёр
                'Призёр' : [9, 5.5, 3.5, 1.5, 0.5]
            },
            'На уровне СНГ' : {
                # победитель
                'Победитель': [8, 5, 3, 1, 0.5],
                # призёр
                'Призёр': [7, 4.5, 2.5, 0.5]
            },
            'На федеральном уровне' : {
                # победитель
                'Победитель': [5, 3, 2, 0.5],
                # призёр
                'Призёр': [4, 2.5, 1.5]
            }
        },
        # Спорт
        'Участие в общественных спортивных мерприятих': {
            'На международном уровне': {
                # победитель
                'Победитель': [3, 2, 1],
                # призёр
                'Призёр': [2, 1.5, 0.5]
            },
            'На уровне СНГ': {
                # капитан
                'Капитан': [3, 2, 1],
                # член команды
                'Член команды': [2, 1.5, 0.5]
            },
            'На федеральном уровне' : [3, 2, 1]
        },
        # ГТО
        'ГТО' : [4]
    }
}