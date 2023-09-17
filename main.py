from stockfish import Stockfish

from colorama import Fore, Back, Style

params=open('config.rawfish').read()

fish=Fore.BLUE +""".
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣠⡤⠤⣤⡤⠤⢤⣄⣀
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⡤⠖⠊⢉⠄⠚⡠⠊⠁⠄⠄⠄⠄⠈⠉⠓⠲⣄⡀
⠄⠄⠄⠄⠄⠄⠄⢀⡤⠞⠁⠄⠄⠺⠽⠄⡰⠁⠄⠄⠄⢠⣾⣷⡆⢀⡠⣒⡥⠏
⠄⠄⠄⠄⠄⢀⡴⠋⠄⠄⢔⡳⠄⡠⠂⠙⠃⠄⠄⠄⠄⠈⠙⠛⡕⣽⣮⢵⣻⠃
⠄⠄⠄⣠⣞⡽⠁⢠⢺⣷⠄⠖⡰⠁⠄⠄⣇⠄⠄⠄⠄⠄⠄⠄⣙⠕⢊⡵⠃
⠄⢀⡞⠉⢴⠁⠚⠈⠙⢁⡠⠚⠡⡲⢚⢶⢫⠑⢤⡀⠄⠄⠄⣀⡠⠖⠋
⢀⣟⠡⢒⡇⢠⣶⠄⡰⡃⢀⣴⣫⣖⣥⠟⠄⣉⣶⣾⠟⠛⠉⠁
⡼⣡⢆⣽⠃⠈⠩⢰⠁⠛⠈⠉⢉⣠⠴⠚⠩⡿⠜⠃
⠙⠗⠋⢸⡄⠰⠷⠘⠘⠃⣠⠖⠉
⠄⠄⠄⠄⡇⠓⠄⣜⡀⢰⠁
⠄⠄⠄⠄⠹⡄⠄⣌⠁⣿⠄⠄⠄⠄⢀⣠⡤⢤
⠄⠄⠄⠄⠄⢹⣄⠈⢢⠘⣦⣀⡤⣞⠩⠴⢲⠏
⠄⠄⠄⠄⠄⠸⣼⢳⣄⠳⠬⡛⠮⣷⡂⣭⣽
⠄⠄⠄⠄⠄⠄⠻⣼⠋⠙⢶⡭⣶⢗⡐⠒⠺⣆
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢦⣑⠬⢁⣀⠚⢦
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠑⠲⠤⠭⣭⠽⠶"""

exec(params)

RUNNING=True
count=0; moves=[]
stockfish = Stockfish(path=r"C:\Users\Никита\PycharmProjects\rawfish\stockfish\stockfish-windows-x86-64-modern.exe",
                      parameters=param)

print(fish + '''\n
RawFish by Bolgaro4ka, based in StockFish 16''')
print("""
K - kng - 'король', 
Q - queen - 'ферзь', 
R - rook - 'ладья', 
N - knight - 'конь', 
B - bishop - 'слон',
P - pawn - 'пешка'

Фигуры большими буквами: """ + Fore.LIGHTWHITE_EX+ "белые, " + Fore.BLUE + "маленькие: "+ Fore.LIGHTBLACK_EX + "чёрные" + "\n"+
    Fore.BLUE+"Версия Stockfish: "+ Fore.RED + str(stockfish.get_stockfish_major_version()))

if COLOR == 'black':
    print(Fore.BLACK + Back.LIGHTWHITE_EX + Style.NORMAL + "Вы чёрный")
    print(Style.RESET_ALL + stockfish.get_board_visual())
    while RUNNING:
        count+=1
        stockfish.set_position(moves)
        print(stockfish.get_board_visual())
        best_move=stockfish.get_best_move()
        moves.append(best_move)
        stockfish.set_position(moves)
        print(stockfish.get_board_visual())
        print(f'RawFish: {best_move}')
        moves.append(input('You: '))
        try:
            stockfish.set_position(moves)
        except ValueError:
            print('UNCORRECT!'); del moves[-2:]; continue
        print(stockfish.get_board_visual())

if COLOR == 'white':
    print(Fore.LIGHTWHITE_EX + Back.BLACK +"Вы белый")
    print(Style.RESET_ALL + stockfish.get_board_visual())
    while RUNNING:
        count+=1

        stockfish.set_position(moves)
        print(stockfish.get_board_visual())

        moves.append(input('You: '))
        try:
            stockfish.set_position(moves)
        except ValueError:
            print('UNCORRECT!'); del moves[-1:]; continue
        stockfish.set_position(moves)
        print(stockfish.get_board_visual())
        best_move = stockfish.get_best_move()
        moves.append(best_move)
        print(f'RawFish: {best_move}')

        print(stockfish.get_board_visual())



