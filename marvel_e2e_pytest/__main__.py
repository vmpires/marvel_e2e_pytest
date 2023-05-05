import pytest
import sys
from time import sleep
from marvel_e2e_pytest.tools.docker_tools import docker_up, docker_down


if __name__ == "__main__":
    
    argument_path = sys.argv[1] if len(sys.argv) > 1 else None

    docker_up(argument_path)

    sleep(4)

    pytest.main(['-v', '-s', './marvel_e2e_pytest/tests'])

    sleep(3)

    docker_down(argument_path)