from enum import Enum, auto
from threading import Lock


class BankAccount(object):

    # Simple state machine
    class State(Enum):
        INIT = auto()
        OPEN = auto()
        CLOSED = auto()

    def __init__(self):
        # Must make state changes thread-safe via a mutex
        self.state = self.State.INIT

        # Must make balance changes thread-safe via a mutex
        self.balance = 0

        # Mutex. Think we can get away with a single lock, as deposit and
        # withdrawal depend on the state, as well as the balance. Otherwise
        # consider separate locks for state and balance.
        self.lock = Lock()

    def get_balance(self):
        with self.lock:
            if self.state != self.State.OPEN:
                raise ValueError("Can only check balance of open accounts")

            return self.balance

    def open(self):
        with self.lock:
            if self.state == self.State.OPEN:
                raise ValueError("Cannot re-open an open account")

            self.state = self.State.OPEN

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Can only deposit positive amounts")

        with self.lock:
            if self.state != self.State.OPEN:
                raise ValueError("Can only check balance of open accounts")

            self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Can only withdraw positive amounts")

        with self.lock:
            if self.state != self.State.OPEN:
                raise ValueError("Can only withdraw from open accounts")

            if self.balance < amount:
                raise ValueError("Unable to withdraw more than balance")

            self.balance -= amount

    def close(self):
        with self.lock:
            if self.state != self.State.OPEN:
                raise ValueError("Can only close an open account")

            self.state = self.State.CLOSED
            # Closed accounts do not retain a balance.
            self.balance = 0
