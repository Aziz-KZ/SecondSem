class Kassa(object):
    def __init__(self):
        self.balance = 0

    def top_up(self, X):
        if X <= 0:
            raise ValueError("Пополнение должно быть положительным числом!")
        self.balance += X
        print(f"Баланс пополнен на {X} рублей. Текущий баланс: {self.balance}")

    def count_1000(self):
        return self.balance // 1000
    
    def take_away(self, X):
        if X > self.balance:
            print(f"Ошибка: В кассе недостаточно средств для снятия {X}. Текущий баланс: {self.balance}.")
        else:
            self.balance -= X
            print(f"Снято {X}. Остаток на балансе: {self.balance}.")

kassa = Kassa()
kassa.top_up(5000)
print(f"Целых тысяч в кассе: {kassa.count_1000()}")
kassa.take_away(2000)
kassa.take_away(4000)