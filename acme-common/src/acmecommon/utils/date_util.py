# -*- coding: utf-8 -*-


import datetime
from calendar import monthrange


from acmecommon.utils.number_util import NumberUtil


class DateUtil:

    def is_valid_date(self, birth_date):
        """ Check is a valid date

        Usage::
            >>> import klassify
            >>> data = [("green", "foo"), ("orange", "bar")]
            >>> classifier = klassify.train(data)

        :param train_data: A list of tuples of the form ``(color, label)``.
        :rtype: A :class:`Classifier <Classifier>`

        Usage:
            DateUtil().is_valid_date('20151021')  # True
            DateUtil().is_valid_date('20151041')  # False
        Args:
            birth_date:
        Returns:
        """
        if len(birth_date) != 8:
            return False

        if not birth_date.isdigit():
            return False

        try:
            datetime.datetime.strptime(birth_date, "%Y%m%d")
        except ValueError:
            return False

        return True

    def get_first_date_of_next_month(self, base_date=datetime.datetime.today()):
        """
        Usage:
            DateUtil().get_first_date_of_next_month()  # if today is 2016.2.24 then return datetime.date(2016, 3, 1)
            DateUtil().get_first_date_of_next_month(datetime.datetime(2016, 12, 31))  # datetime.date(2017, 1, 1)
        Args:
            base_date: datetime.date
        """
        if base_date.month + 1 > 12:
            return datetime.date(base_date.year + 1, 1, 1)

        return datetime.date(base_date.year, base_date.month + 1, 1)

    def get_age_band(self, year):
        """
        Usage:
        Args:
            year: four digit number or string.
        """
        if not year or (isinstance(year, str) and not year.isdigit()):
            return None
        return NumberUtil(datetime.datetime.today().year - int(year)).round_down(1)

    def month_delta(self, date_1, date_2):
        delta = 0
        while True:
            mdays = monthrange(date_1.year, date_1.month)[1]
            date_1 += datetime.timedelta(days=mdays)
            if date_1 <= date_2:
                delta += 1
            else:
                break
        return delta

    def get_timestamp_diff_formatted(self, big_timestamp, small_timestamp):
        if big_timestamp and isinstance(big_timestamp, int):
            _big_date = datetime.datetime.fromtimestamp(big_timestamp)
        else:
            _big_date = datetime.datetime.now()
        if small_timestamp and isinstance(small_timestamp, int):
            _small_date = datetime.datetime.fromtimestamp(small_timestamp)
        else:
            _small_date = datetime.datetime.now()

        return self.get_datetime_diff_formatted(_big_date, _small_date)

    def get_datetime_diff_formatted(self, big_date, small_date):
        if big_date and isinstance(big_date, datetime.datetime):
            _big_date = big_date
        else:
            _big_date = datetime.datetime.now()
        if small_date and isinstance(small_date, datetime.datetime):
            _small_date = small_date
        else:
            _small_date = datetime.datetime.now()

        if _big_date <= _small_date:
            return "-"

        _delta = _big_date - _small_date
        _remain_seconds = _delta.total_seconds()
        _remain_days = _remain_seconds // (24 * 60 * 60)
        _remain_seconds %= 24 * 60 * 60
        _remain_hours = _remain_seconds // (60 * 60)
        _remain_seconds %= 60 * 60
        _remain_minutes = _remain_seconds // 60

        if _remain_days:
            if _remain_hours:
                _result = f"{_remain_days} {_remain_hours}"
            else:
                _result = f"{_remain_days} {_remain_minutes if _remain_minutes else 1}"
        elif _remain_hours:
            _result = f"{_remain_hours} {_remain_minutes if _remain_minutes else 1}"
        elif _remain_minutes:
            _result = f"{_remain_minutes}"
        else:
            _result = "1"

        return _result
