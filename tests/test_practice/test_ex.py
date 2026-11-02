import pytest
import factory

from tests.practice.ex import InsufficientFundsError, Logger, NotificationService, FraudDetectionService, Account


class TestInsufficientFundsError:

    def test_is_exception_subclass(self):
        assert issubclass(InsufficientFundsError, Exception)

    def test_can_be_raised_and_caught(self):
        with pytest.raises(InsufficientFundsError):
            raise InsufficientFundsError()


class TestLogger:

    def test_log(self):
        assert Logger().log("Hi") is None

    def test_log_prints(self, capsys):
        Logger().log("Hi")
        assert capsys.readouterr().out == "[LOG]: Hi\n"


class TestNotificationService:

    def test_send(self):
        assert NotificationService().send("Hellow", "World") is None

    def test_send_prints(self, capsys):
        NotificationService().send("Hellow", "World")
        assert capsys.readouterr().out == "[NOTIFY Hellow]: World\n"


class TestFraudDetectionService:

    def test_is_fraudulent(self):
        assert FraudDetectionService().is_fraudulent("first user", "second user", 12.6) is False


class FakeFraudCheckerAlwaysPositive(FraudDetectionService):
    def is_fraudulent(self, from_user, to_user, amount):
        return True


class TestAccount:

    @pytest.fixture
    def data_account_amount_zero(self):
        return Account("Петрович", 0.0, None, None, None)

    @pytest.fixture
    def data_account_amount(self):
        return Account("Петрович", 100.0, None, None, None)

    def test_deposit_value_error(self, data_account_amount_zero):
        with pytest.raises(ValueError):
            data_account_amount_zero.deposit(-1.0)

    def test_add_deposit_amount(self, data_account_amount_zero):
        data_account_amount_zero.deposit(10.0)
        assert data_account_amount_zero.balance == 10.0

    def test_log_deposit_amount(self, data_account_amount_zero, capsys):
        data_account_amount_zero.deposit(10.0)
        assert capsys.readouterr().out == '[LOG]: Петрович deposited 10.0\n'

    def test_withdraw_insufficient_funds_error(self, data_account_amount):
        with pytest.raises(InsufficientFundsError):
            data_account_amount.withdraw(150.0)

    def test_minus_balance_withdraw(self, data_account_amount):
        data_account_amount.withdraw(60.0)
        assert data_account_amount.balance == 40.0

    def test_log_withdraw(self, data_account_amount, capsys):
        data_account_amount.withdraw(60.0)
        assert capsys.readouterr().out == '[LOG]: Петрович withdrew 60.0\n'

    def test_transfer(self, data_account_amount):
        target = Account("Получатель", 0.0)
        assert data_account_amount.transfer(target, 50.0) is None

    def test_transfer_blocked(self, data_account_amount):
        with pytest.raises(ValueError):
            target = Account("Получатель", 0.0)
            data_account_amount.transfer(target, 0.0)
            FraudDetectionService().is_fraudulent("first user", "second user", 12.6)

    def test_transfer_blocked_by_fraud_with_di(self, data_account_amount):
        target = Account("Получатель", 0.0)
        account_with_fake_checker = Account(
            data_account_amount.owner,
            data_account_amount.balance,
            logger=data_account_amount.logger,
            notifier=data_account_amount.notifier,
            fraud_checker=FakeFraudCheckerAlwaysPositive())
        with pytest.raises(RuntimeError, match="Fraud detected"):
            account_with_fake_checker.transfer(target, 50.0)

    def test_transfer_amount_more_than_balance(self, data_account_amount):
        target = Account("Получатель", 0.0)
        with pytest.raises(InsufficientFundsError):
            data_account_amount.transfer(target, 1000.0)

    def test_transfer_amount_less_than_balance(self, data_account_amount):
        target = Account("Получатель", 10.0)
        data_account_amount.transfer(target, 10.0)
        assert data_account_amount.balance == 90.0

    def test_transfer_amount_less_than_balance_log(self, data_account_amount, capsys):
        target = Account("Получатель", 10.0)
        data_account_amount.transfer(target, 10.0)
        output = capsys.readouterr().out
        assert "[LOG]: Петрович withdrew 10.0\n" in output

    def test_transfer_amount_less_than_zero(self, data_account_amount):
        target = Account("Получатель", 0.0)
        with pytest.raises(ValueError):
            target.transfer(target, 0.0)

    def test_transfer_amount_more_than_zero(self, data_account_amount):
        target = Account("Получатель", 10.0)
        data_account_amount.transfer(target, 20.0)
        assert target.balance == 30

    def test_transfer_amount_more_than_zero_log(self, data_account_amount, capsys):
        target = Account("Получатель", 10.0)
        data_account_amount.transfer(target, 20.0)
        output = capsys.readouterr().out
        assert "[LOG]: Получатель deposited 20.0\n" in output

    def test_transfer_notifier_send(self, data_account_amount, capsys):
        target = Account("Получатель", 10.0)
        data_account_amount.transfer(target, 20.0)
        output = capsys.readouterr().out
        assert "[NOTIFY Получатель]: You received 20.0 from Петрович\n" in output

    def test_transfer_log(self, data_account_amount, capsys):
        target = Account("Получатель", 10.0)
        data_account_amount.transfer(target, 20.0)
        output = capsys.readouterr().out
        assert 'Петрович transferred 20.0 to Получатель' in output

    def test_get_balance(self, data_account_amount):
        assert data_account_amount.get_balance() == 100.00

