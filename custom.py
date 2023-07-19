import random
import time


# Função que gera 2 números aleatórios dentro do intervalo escolhido, soma os dois e verifica se é par ou ímpar
def play_game(interval_start, interval_end):
    num1 = random.randint(interval_start, interval_end)
    num2 = random.randint(interval_start, interval_end)
    total_sum = num1 + num2
    return total_sum % 2 == 0


# Função que simula os jogos com base no input do usuário e mostra quantos jogos par e ímpar ganharam e as respectivas porcentagens de win rate de cada um
def main():
    interval_start = int(input("Informe o início do intervalo de números para o jogo: "))
    interval_end = int(input("Informe o final do intervalo de números para o jogo: "))
    num_games = int(input("Coloque o número que jogos que você deseja simular: "))
    even_wins = 0
    odd_wins = 0

    start_time = time.time()

    for _ in range(num_games):
        if play_game(interval_start, interval_end):
            even_wins += 1
        else:
            odd_wins += 1

    end_time = time.time()
    total_time = end_time - start_time

    total_wins = even_wins + odd_wins
    even_percentage = (even_wins / total_wins) * 100
    odd_percentage = (odd_wins / total_wins) * 100

    print(f"Número de jogos jogados: {num_games}")
    print(f"Vitórias do par: {even_wins} (Porcentagem: {even_percentage:.2f}%)")
    print(f"Vitórias do ímpar: {odd_wins} (Porcentagem: {odd_percentage:.2f}%)")
    print(f"Tempo total: {total_time:.2f} segundos")


if __name__ == "__main__":
    while True:
        main()
        play_again = input("Deseja jogar novamente? (s/n): ").lower()
        if play_again != "s":
            break
