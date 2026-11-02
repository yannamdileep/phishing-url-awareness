import re
from urllib.parse import urlparse

import streamlit as st


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


# Streamlit application interface
st.set_page_config(
    page_title="Phishing URL Awareness Checker",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Phishing URL Awareness Checker")

st.write(
    "Check a URL for common phishing warning signs."
)

st.info(
    "This tool checks URL text only. "
    "It does not open URLs or guarantee that a website is safe."
)

url = st.text_input(
    "Enter a URL to check",
    placeholder="https://example.com"
)

if st.button("Check URL", type="primary"):

    if not url.strip():
        st.warning("Please enter a URL.")

    else:
        findings = inspect_url(url)

        st.subheader("Analysis Results")

        errors = [
            "No URL entered.",
            "Could not identify a hostname.",
            "This text is not a valid URL format."
        ]

        if findings[0] in errors:
            st.error(findings[0])

        elif findings[0].startswith(
            "No listed warning signs"
        ):
            st.success(findings[0])

        else:
            st.warning("Review carefully!")

            for item in findings:
                st.write("⚠️", item)

        st.caption(
            "Never enter passwords, OTPs, PINs, or "
            "banking details through unexpected links."
        )

st.divider()

st.caption(
    "Phishing URL Awareness Checker | Cybersecurity Mini Project"
)
