maintenance = 0
###################################
#*********************************#
#*  New words by Artyom Valitov  *#
#*Помогает выучить долбаные слова*#
#*   Айда вниз, там инструкция!  *#
#*********************************#
###################################
def maint(en):
  if en == 1:
    maintenance = 1
    mt = '3 дня'
    print('Техобслуживание. Скрипт может быть нестабилен или          вовсе выдавать ошибки! Стабильная работа через: ' + mt + '. ±6  часов.')
    return

maint(1)
#Слова и переводы снизу (Можно редактировать)
words = ['', 'leap at the chance', 'signify', 'steaming hot', 'greet', 'tradition', 'hustle and bustle', 'nickname', 'stick', 'groom', 'marching band', 'entrance', 'stunning', 'ceremony', 'emarass oneself', 'fairytale wedding'] 
translations = ['', 'Ухватится за шанс', 'Символизировать', 'Очень жарко', 'Приветствовать', 'Традиция', 'Суета, суматоха', 'Никнейм', 'Придерживаться(чего-либо)', 'Жених', 'Марширующий ансамбль(оркестр)', 'Вход', 'Завораживающий', 'Церемония', 'Смущаться', 'Сказочная свадьба']
#Слова и переводы сверху (Можно редактировать)

#Скриптовая часть снизу (Нельзя редактировать!!!)
if maintenance != 1:
  wordtd = 0
  word = input('Please, enter the word index:\n')
  word = int(word)
  if word > len(words):
    word = 0
  winp = ('word: ' + words[word])
  wordt = word
  wordt = int(wordt)
  if wordt > len(translations):
    wordt = 0
  tinp = ('Перевод:' + translations[wordt])
else:
  print('Техобслуживание. Скрипт неактивен. Активация через: ' + mt + '. ±6 часов.')
#Скриптовая часть сверху (Нельзя редактировать!!!)

#Не трогать функции снизу!
#Функции были обновлены
#В консольку вводите номер нужного вам слова!
#Каждое слово в нужном порядке проиндексировано в учебнике.
#Вопросов по этому поводу быть не должно
if maintenance != 1:
  print(winp)
  print(tinp)
  print('')
  print('')
  print('')
  print('')
  print('                                          ~~~5f~~~v0.2~~~')
  print('                       Спасибо за использование New words')
  print('                                Created by Artyom Valitov')
  print('                              Run again to check new word')
  print()
#Не вводите word index больше суммы всех слов!
#Иначе будет: IndexError: list index out of range
#Поздравляем! Вы дошли до конца! А я скушал тунца.
#В будущем буду дорабатывать                                                                            Redko Prihodit
