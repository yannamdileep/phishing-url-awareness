
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check URL text for common phishing warning signs."""

    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    # Add HTTP if the URL has no scheme
    candidate = url if "://" in url else "http://" + url

    # Handle invalid URL formats
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    # Check 1: @ symbol
    if "@" in candidate:
        findings.append(
            "Contains an @ symbol; inspect carefully."
        )

    # Check 2: URL length
    if len(url) > 100:
        findings.append(
            "Unusually long URL (over 100 characters)."
        )

    # Check 3: IP address hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    # Check 4: Many hostname segments
    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append(
            "Contains many hostname segments/subdomains."
        )

    # Check 5: Punycode hostname
    if "xn--" in host:
        findings.append(
            "Contains a punycode-style hostname."
        )

    # Check 6: HTTP protocol
    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    if not findings:
        findings.append(
            "No listed warning signs found. "
            "This does NOT prove safety."
        )

    return findings


def main():
    print("=" * 50)
    print("       PHISHING URL AWARENESS CHECKER")
    print("=" * 50)

    print("Text checks only - this program does not open URLs.")
    print("Enter q to quit.\n")

    while True:
        raw_url = input("Enter a sample URL: ").strip()

        if raw_url.lower() in ["q", "quit", "exit"]:
            print("Thank you for using the checker!")
            break

        findings = inspect_url(raw_url)

        print("\nRESULT:")

        if findings and not findings[0].startswith(
            "No listed warning signs"
        ):
            if findings[0] not in [
                "No URL entered.",
                "Could not identify a hostname.",
                "This text is not a valid URL format."
            ]:
                print("REVIEW CAREFULLY!")

        for item in findings:
            print("- " + item)

        print("\nNever enter passwords through unexpected links.")
        print("-" * 50)


if __name__ == "__main__":
    main()
