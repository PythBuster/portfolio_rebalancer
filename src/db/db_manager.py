from typing import Any


class DBManager:
    def __init__(self):
        pass

    async def get_portfolio(self) -> dict[str, Any]:
        """Get stocks and their allocated percentages in the portfolio.

        :return: A dictionary of holding names and their allocated percentages as integers.
        :rtype: :class:`dict[str, int]`
        """

        # mocked data
        # TODO: implement

        return {
            "MSCI ACWI IMI": 46,
            "MSCI World Inf. Techn.": 14,
            "MSCI EM": 11,
            "Core Stoxx Europe 600": 9,
            "MSCI World Momentum": 8,
            "MSCI Health Care": 6,
            "MSCI World Energy": 4,
            "Physical Gold": 2,
        }