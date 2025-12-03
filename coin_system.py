import random


class Coin:
    def __init__(self, value, year):
        self.value = value
        self.year = year

    def flip(self):
        """Return a random coin flip: Head or Tail."""
        rand = random.randint(0, 1)
        if rand == 0:
            return "Head"
        else:
            return "Tail"


class Eurocoin(Coin):
    def __init__(self, value, year, country):
        super().__init__(value, year)
        self.country = country

    def convert_to_usd(self):
        """Convert the euro coin value to USD (simple example rate)."""
        print("Converting EUR to USD...")
        return self.value * 1.08


class Wallet:
    def __init__(self):
        self.coin_list = []
        self.sum_value = 0

    def add_coin(self, c):
        if isinstance(c, Coin):
            self.coin_list.append(c)
            print(
                f"The coin with value {c.value} and year {c.year} was added to the wallet.\n"
            )

    def remove_coin(self, c):
        if c in self.coin_list:
            self.coin_list.remove(c)
            print(
                f"\nThe coin with value {c.value} and year {c.year} was removed from the wallet."
            )
        else:
            print("\nCoin not found in the wallet.")

    def sum_coin(self):
        self.sum_value = sum(c.value for c in self.coin_list)
        print("\nThe sum of the coin values in the wallet is:", self.sum_value)

    def sort(self):
        """Sort coins by year."""
        self.coin_list.sort(key=lambda coin_obj: coin_obj.year)
        print("The list sorted by year is:\n")
        for c in self.coin_list:
            print(c.value, c.year)


class PiggyBank:
    def __init__(self):
        self.dic = {}

    def add(self, c):
        if isinstance(c, Coin):
            print("\nAdding coin to piggy bank...\n")
            # If the same value appears more than once, keep the latest year
            self.dic[c.value] = c.year
        print(self.dic)

    def sum_coin_values(self):
        s = sum(self.dic.keys())
        print("The sum of the coin values in the piggy bank is:", s)


class CoinStack:
    def __init__(self):
        self.stack = []

    def push_item(self, item):
        print("\nPushing item into the stack...\n")
        self.stack.append(item)

    def pop_item(self):
        if len(self.stack):
            print("\nPopping item from the stack")
            return self.stack.pop()
        else:
            print("\nThe stack is empty, cannot pop.")

    def top_of_stack(self):
        if len(self.stack):
            top = self.stack[-1]
            print(
                f"\nThe top item of the stack is value: {top.value}, year: {top.year}"
            )
        else:
            print("\nThe stack is empty.")


class CoinQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        print("\nInserting item into the queue...")
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue):
            print("\nRemoving item from the queue...")
            return self.queue.pop(0)
        else:
            print("\nThe queue is empty, cannot dequeue.")


# Example usage:

usd = Eurocoin(0.5, 1763, "United States")
euro = Eurocoin(1, 1999, "Greece")
lek = Eurocoin(3, 1983, "Albania")

print(
    f"The coin from {lek.country} has value {lek.value} and is from year {lek.year}."
)
print("Coin flip result:", lek.flip(), "\n")

print(
    f"The coin from {usd.country} has value {usd.value} and is from year {usd.year}."
)
print("Coin flip result:", usd.flip(), "\n")

print(
    f"The coin from {euro.country} has value {euro.value} and is from year {euro.year}."
)
print("Coin flip result:", euro.flip())
print("\nIf we convert this euro coin to USD, the value is:", euro.convert_to_usd())

# Wallet demo
w = Wallet()
w.add_coin(usd)
w.add_coin(euro)
w.add_coin(lek)
w.sort()
w.sum_coin()
w.remove_coin(lek)

# Piggy bank demo
piggy = PiggyBank()
piggy.add(usd)
piggy.add(lek)
piggy.add(euro)
piggy.sum_coin_values()

# Stack demo
st = CoinStack()
st.pop_item()
st.push_item(usd)
st.push_item(euro)
st.pop_item()
st.push_item(lek)
st.top_of_stack()

# Queue demo
q = CoinQueue()
q.enqueue(usd)
q.dequeue()
q.dequeue()
q.enqueue(lek)
