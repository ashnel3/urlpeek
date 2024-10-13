from .Application import Application
from typing import NoReturn, Optional, Sequence


def main(args: Optional[Sequence[str]] = None) -> NoReturn:
    return exit(Application.Main(args))


if __name__ == "__main__":
    main()
