import subprocess

import pytest

if __name__ == "__main__":
    pytest.main()
    subprocess.run(["allure", "generate", "-o", "report", "-c", "temps"], check=True)
