# PracticeSoftwareTesting UI Automation

UI test automation project for [practicesoftwaretesting.com](https://practicesoftwaretesting.com) (Toolshop v5.0) using **Python + Playwright + pytest**, with CI/CD pipeline via GitHub Actions.

## Tech Stack

- Python
- Playwright
- pytest
- pytest-playwright
- GitHub Actions

## Project Structure

```
├── pages/                  # Page Object Model
│   ├── home_page.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── handtools_page.py
│   ├── product_page.py
│   └── checkout_page.py
├── tests/                  # Test suite
│   ├── test_homepage.py
│   ├── test_login.py
│   ├── test_dashboard.py
│   ├── test_handtools.py
│   ├── test_product.py
│   └── test_checkout.py
├── conftest.py             # Pytest fixtures
├── pytest.ini              # Pytest configuration
└── .env                    # Environment variables (not committed)
```

## Test Coverage

| Test | Type |
|------|------|
| Sign in button navigates to login page | smoke |
| Login with valid credentials | smoke |
| Login with invalid credentials | smoke |
| Logout | smoke |
| Categories list loads hand tools | smoke |
| Products list is available | smoke |
| First product opens correctly | smoke |
| Add product to cart | smoke |
| Complete checkout flow | smoke |

## Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Install Chromium
playwright install chromium

# Run all tests
pytest -v

# Run only smoke tests
pytest -m smoke -v

# Run headed with slow motion (useful for debugging)
pytest -v --headed --slowmo 500
```

## Environment Variables

Create a `.env` file in the root directory:

```
BASE_URL=https://practicesoftwaretesting.com
EMAIL=your_email
PASSWORD=your_password
POSTAL_CODE=your_postal_code
HOUSE_NUMBER=your_house_number
```

## CI/CD

The project includes a GitHub Actions pipeline configured to run on every push and pull request to `main`.

> **Note:** The CI pipeline is configured but cannot execute successfully on GitHub-hosted runners. `practicesoftwaretesting.com` uses Cloudflare bot protection, which detects datacenter IPs (such as GitHub Actions servers) and displays a "Verify you are human" challenge page instead of the actual site. All tests pass when run locally.
