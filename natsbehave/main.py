import argparse
import asyncio
from natsbehave.application import Application
from natsbehave.parser import parse_scenarios
from natsbehave.decoration import Colors as C


async def run_tests(test_scenarios):
    async with Application("localhost") as app:
        for section in test_scenarios:
            print(f"{C.HEADER}{section["section"]}{C.ENDC}")
            for scenario in section["scenarios"]:
                print(f"\t{scenario["title"]}")
                await app.received(scenario["on"])
                result = await app.sends(scenario["reply"])
                result_str = f"{C.OKGREEN}Passed{C.ENDC}" if result else f"{C.FAIL}Failed{C.ENDC}"
                print(f"\t\t{result_str}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tests on NATS application")
    parser.add_argument("source",
                        help="file or directory containing scenario files",
                        type=str)
    args = parser.parse_args()

    scenarios = parse_scenarios(args.source)
    asyncio.run(run_tests(scenarios))