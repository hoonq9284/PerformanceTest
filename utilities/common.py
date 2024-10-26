def log_response(response):
    print(f"Status: {response.status_code}, Time: {response.elapsed.total_seconds()}s")