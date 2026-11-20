import requests
import sys

BASE_URL = "http://localhost:8000"


def test_route(path, expected_status=200):
    try:
        response = requests.get(BASE_URL + path)

        print(f"GET {path} -> {response.status_code}")

        if response.status_code != expected_status:
            print(f"FAILED: {path}")
            return False

        print(f"PASSED: {path}")
        return True

    except requests.RequestException as error:
        print(f"ERROR: {path} -> {error}")
        return False


def run_tests():
    routes = [
        "/",
        "/health",
        "/students"
    ]

    all_passed = True

    for route in routes:
        if not test_route(route):
            all_passed = False

    if all_passed:
        print("\nAll API tests passed successfully!")
        sys.exit(0)
    else:
        print("\nSome API tests failed!")
        sys.exit(1)


if __name__ == "__main__":
    run_tests()