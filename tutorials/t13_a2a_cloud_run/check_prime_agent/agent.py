from google.adk import Agent


async def check_prime(nums: list[int]) -> str:
    """与えられた数字が素数かどうか判定します。
    Args:
        nums: 素数かどうか判定する数字のリスト
    Returns:
        素数のリスト
    """
    primes = set()
    for number in nums:
        number = int(number)
        if number <= 1:
            continue
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(number)
    return (
        "素数はありませんでした"
        if not primes
        else f"{', '.join(str(num) for num in primes)} は素数です。"
    )


root_agent = Agent(
    model="gemini-2.0-flash",
    name="check_prime_agent",
    description="素数チェックAgent",
    instruction="与えられた数字が素数かどうか判定してください。",
    tools=[check_prime],
)
